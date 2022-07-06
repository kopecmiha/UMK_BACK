from django.urls import path
from .views import ListOfCompetences, upload_file

urlpatterns = [
    path('list_of_competences/', ListOfCompetences.as_view()),
    path('upload_file/', upload_file)
]