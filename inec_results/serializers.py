from rest_framework import serializers
from .models import AnnouncedPuResults
from .models import PollingUnit


class AnnouncedPuResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncedPuResults
        fields = '__all__'


class PollingUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingUnit
        fields = '__all__'



class NewPollingUnitResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncedPuResults
        fields = '__all__'



