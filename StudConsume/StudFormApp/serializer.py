from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
