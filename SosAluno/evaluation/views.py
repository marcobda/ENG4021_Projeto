from django.shortcuts import render, get_object_or_404
# from .models import Professor # Descomente quando for usar

def evaluate_professor(request, professor_id):
    """View para a página de avaliação de um professor."""
    # professor = get_object_or_404(Professor, pk=professor_id)
    return render(request, 'evaluation/evaluate.html')

def ranking_view(request):
    """View para a página de ranking."""
    return render(request, 'evaluation/ranking.html')

def professor_detail(request, professor_id):
    """View para a página de detalhes do professor e suas avaliações."""
    return render(request, 'evaluation/professor_detail.html')