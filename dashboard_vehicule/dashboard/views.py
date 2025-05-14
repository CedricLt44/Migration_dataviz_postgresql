from django.shortcuts import render
from .models_legacy import RawEntretiens
from django.db.models import Sum

import locale
# locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')  # Pour Linux/Mac
locale.setlocale(locale.LC_ALL, '')  # Windows utilise la locale système

def data_view(request):
    """
    Vue de mes données de la table PostgreSQL via models_legacy.py.
    Permet de filtrer les données selon l'immatriculation et le type d'opération.
    Affiche les immatriculations distinctes et les opérations distinctes.
    """
    # Récupération de toutes les données
    entretien_data = RawEntretiens.objects.all()

    # Filtrer selon l'immatriculation si un paramètre 'immat' est présent dans l'URL
    immat = request.GET.get('immat')
    if immat:
        entretien_data = entretien_data.filter(immat=immat)

    # Extraction des immatriculations distinctes
    distinct_immat = RawEntretiens.objects.values_list('immat', flat=True).distinct()

    # Filtrer selon le type d'operation
    operation = request.GET.get('operation')
    if operation:
        entretien_data = entretien_data.filter(operation=operation)
    
    # Opérations distinctes (tri avec None après le vide)
    distinct_operation = list(
        RawEntretiens.objects.values_list('operation', flat=True).distinct()
    )
    distinct_operation.sort(key=lambda x: (x is not None, x))

    # Calcul du montant total des coûts
    total_cost = entretien_data.aggregate(Sum('cost'))['cost__sum'] or 0
    # Format avec espace comme séparateur de milliers et deux chiffres après la virgule
    formatted_total_cost = f"{total_cost:,.2f}".replace(',', ' ').replace('.', ',')

    return render(request, 'dashboard/data.html', {
        'entretien_data': entretien_data,
        'distinct_immat': distinct_immat,  # Passer les immatriculations distinctes au template
        'distinct_operations': distinct_operation,  # Passer les opérations distinctes au template
        'total_cost': formatted_total_cost,  # Passer le coût total au template
    })
