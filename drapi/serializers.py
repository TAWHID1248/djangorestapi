from rest_framework import serializers
from .models import Aiquest

class AiquestSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=25)
    course_name = serializers.CharField(max_length=20)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()

    def create(self, validated_data):
        return Aiquest.objects.create(**validated_data)