from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models_legacy import RawEntretiens
# Create your views here.
def data_view(request):
    """
    vue de mes donnée de la table postgres
    via models_legacy.py.
    """
  #  affichez la page de données
    entretien_data = RawEntretiens.objects.all()

    return render(request, 'dashboard/data.html', {'entretien_data': entretien_data})