from django.urls import path
from views_hero import BlackWidow, HulkView, IronManView

urlpatterns = [
    path('hulk',        HulkView.as_view()),
    path('ironman',     IronManView.as_view()),
    path('blackwidow',  BlackWidow.as_view()),
]