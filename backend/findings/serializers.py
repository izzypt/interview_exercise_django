from rest_framework import serializers
from findings.models import FindingsModel, ScanModel

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanModel
        fields = ('value',)
    
    def to_representation(self, instance):
        # ModelSerializer serializes a model instance to a dictionary-like object, we need to override that behavior because we want to return a string for each scan.
        # to_representation allows to define how the object should be serialized and what data should be included in the serialized representation.
        return instance.value

class FindingsSerializer(serializers.ModelSerializer):
    scans = ScanSerializer(many=True)
    
    class Meta:
        model = FindingsModel
        fields = ('id', 'definition_id', 'target_id', 'url', 'path', 'method', 'scans')