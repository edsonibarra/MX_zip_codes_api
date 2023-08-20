from rest_framework import serializers

from .models import ZipCodes


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCodes
        fields = "__all__"  # Serialize all fields of the Book model
