from rest_framework import serializers
from .models import *
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .document import *


class Elastic_Demo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ElasticDemo
        fields = '__all__'


class Elastic_Document_Serializer(DocumentSerializer):
    class Meta:
        model = ElasticDemo
        document = ElasticDemoDocument

        fields = ('title', 'content')

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
