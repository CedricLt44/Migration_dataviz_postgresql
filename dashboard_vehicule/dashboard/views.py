from django.shortcuts import render
from .models_legacy import RawEntretiens
from django.db.models import Sum
import plotly.express as px
from django.utils.safestring import mark_safe

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

    # Répartition des coûts par opération
    costs_by_operation = (
        entretien_data.values('operation')
        .annotate(total_cost=Sum('cost'))
        .order_by('-total_cost')
    )
    if not immat:
        # Si aucune immatriculation n'est sélectionnée, on prend les 5 premières opérations
        costs_by_operation = costs_by_operation[:5]

    operation_fig = px.pie(
        names=[item['operation'] for item in costs_by_operation],
        values=[item['total_cost'] for item in costs_by_operation],
        
    )
    operation_chart = mark_safe(operation_fig.to_html(full_html=False))

# barplot des coûts totaux par immatriculation

    # barplot des coûts totaux par immatriculation (top 8) avec axes inversés
    bar_fig = px.bar(
        x=[item['total_cost'] for item in entretien_data.values('immat').annotate(total_cost=Sum('cost')).order_by('-total_cost')[:8]],  # Axe X : coûts totaux
        y=[item['immat'] for item in entretien_data.values('immat').annotate(total_cost=Sum('cost')).order_by('-total_cost')[:8]],  # Axe Y : immatriculations
        orientation='h'  # Orientation horizontale
    )
    # Supprimer les titres des axes
    bar_fig.update_xaxes(title=None)  # Supprimer le titre de l'axe X
    bar_fig.update_yaxes(title=None)  # Supprimer le titre de l'axe Y


    bar_fig.update_yaxes(categoryorder='total ascending')


    operation_histogram = mark_safe(bar_fig.to_html(full_html=False))



    return render(request, 'dashboard/data.html', {
        'entretien_data': entretien_data,
        'distinct_immat': distinct_immat,  # Passer les immatriculations distinctes au template
        'distinct_operations': distinct_operation,  # Passer les opérations distinctes au template
        'total_cost': formatted_total_cost,  # Passer le coût total au template
        'operation_chart': operation_chart,  # Graphique des opérations
        'operation_histogram': operation_histogram,  # Graphique des opérations
    })
