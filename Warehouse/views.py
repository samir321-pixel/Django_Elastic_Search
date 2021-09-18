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

    def list(self, request, *args, **kwargs):
        data = requests.get(
            "https://newsapi.org/v2/everything?q=tesla&from=2021-08-18&sortBy=publishedAt&apiKey=80c34928d4ee48f98cae556930233e78")
        payload = json.loads(data.text)
        for data in payload.get('articles'):
            ElasticDemo.objects.create(
                title=data.get('title'),
                content=data.get('description')
            )
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


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
    filter_fields  = {
        'title': 'title',
        'content': 'content'
    }
