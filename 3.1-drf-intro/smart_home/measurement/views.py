from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementsListSerializer, SensorsListSerializer


class SensorsListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsListSerializer

    def post(self, request):
        data = request.data
        one_sensor = Sensor.objects.create(name=data['name'], description=data['description'])
        one_sensor.save()
        ser = SensorDetailSerializer(one_sensor)
        return Response(ser.data)


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        one_sensor = self.get_object()
        data = request.data
        one_sensor.name = data.get("name", one_sensor.name)
        one_sensor.description = data.get("description", one_sensor.description)
        one_sensor.save()
        ser = SensorDetailSerializer(one_sensor)
        return Response(ser.data)


class MeasurementsListView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsListSerializer

    def post(self, request):
        data = request.data
        sensor = Sensor.objects.get(id=data['sensor_id'])
        one_measurement = Measurement.objects.create(sensor_id=sensor, temperature=data['temperature'])
        one_measurement.save()
        ser = MeasurementsListSerializer(one_measurement)
        return Response(ser.data)