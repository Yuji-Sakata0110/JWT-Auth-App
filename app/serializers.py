from typing import Any
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields: str = "__all__"


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data) -> Any:
        raise NotImplementedError()

    def update(self, instance, validated_data) -> Any:
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data) -> Any:
        raise NotImplementedError()

    def update(self, instance, validated_data) -> Any:
        raise NotImplementedError()
