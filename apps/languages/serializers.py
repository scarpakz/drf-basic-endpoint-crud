from rest_framework import serializers
from .models import(
    Language,
)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        # fields = ('id', 'name', 'paradigm')
        fields = "__all__"