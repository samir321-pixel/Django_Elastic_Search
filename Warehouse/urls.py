from .views import *
from django.urls import path

urlpatterns = [
    path('Elastic_Demo/', Elastic_Demo_View.as_view()),
    path('search/', PublishDocumentView.as_view({'get': 'list'}))
]
