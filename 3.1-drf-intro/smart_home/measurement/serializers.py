from rest_framework import serializers

from .models import Sensor, Measurement


class MeasurementsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

class SensorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementsListSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = '__all__'