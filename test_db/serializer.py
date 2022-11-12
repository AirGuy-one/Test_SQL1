from rest_framework import serializers
from .models import TestData, TestDataRelation


class TestDataSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(method_name='likes_count_method')

    class Meta:
        model = TestData
        fields = ('id', 'title', 'population', 'mayor', 'likes_count')

    def likes_count_method(self, instance):
        return TestDataRelation.objects.filter(city=instance, like=True).count()


class TestDataRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDataRelation
        fields = ('city', 'like', 'city_on_bookmarks', 'rate')



