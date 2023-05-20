from django.urls import path
from .views import index,quiz,results,display_all_patients,music,RelativeView,success_url,streamlit_view,chatroom,random_tweet_view,patient_details

urlpatterns = [
    path('',index,name='home'),
    path('quiz/', quiz, name='quiz'),
    path('results/', results, name='results'),
    path('doctor/display_all_patients', display_all_patients, name='display_all_patients'),
    path('music/',music,name='music'),
    path('relative_info/',RelativeView.as_view(),name='RelativeView'),
    path('success_url/',success_url,name='success_url'),
    path('streamlit/', streamlit_view, name='streamlit'),
    path('chatroom/',chatroom,name='chatroom'),
    path('mood/',random_tweet_view,name='mood'),
    path('patient_details/<str:email>/',patient_details,name='patient_details')
]

