from django.urls import path
from .views import index,quiz,results,display_all_patients,music

urlpatterns = [
    path('',index,name='home'),
    path('quiz/', quiz, name='quiz'),
    path('results/', results, name='results'),
    path('doctor/display_all_patients', display_all_patients, name='display_all_patients'),
    path('music/',music,name='music'),
]
