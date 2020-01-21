from rest_framework import serializers
from . import models


class StudSerializer(serializers.ModelSerializer):

    class Meta:
        fields ='__all__'
        #fields=('id', 'Name','Age','Gender','Country','created_at', 'updated_at','isActive')
        model = models.StudDB

