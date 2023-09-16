# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# sensor_app/views.py
from rest_framework import generics
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class TemperatureMeasurementListCreateView(generics.ListCreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer


class TemperatureMeasurementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer


class CreateSensorView(generics.CreateAPIView):
    serializer_class = SensorSerializer


class CreateTemperatureMeasurementView(generics.CreateAPIView):
    serializer_class = TemperatureMeasurementSerializer
