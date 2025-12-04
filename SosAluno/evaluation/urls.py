from django.urls import path
from . import views

urlpatterns = [
    path("avaliar/<int:professor_id>/", views.evaluate_professor, name="evaluate_professor"),
    path("ranking/", views.ranking_view, name="ranking"),
    path("professor/<int:professor_id>/", views.professor_detail, name="professor_detail"),
]