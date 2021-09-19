from .models import *
from .serializer import *
from rest_framework import generics
import requests, json
from rest_framework.response import Response
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .document import *
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend


# Create your views here.

class Elastic_Demo_View(generics.ListAPIView):
    queryset = ElasticDemo.objects.all()
    serializer_class = Elastic_Demo_Serializer


class PublishDocumentView(DocumentViewSet):
    document = ElasticDemoDocument
    serializer_class = Elastic_Document_Serializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]

    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
        'title',
        'content',
    )
    filter_fields = {
        'title': 'title',
        'content': 'content'
    }
