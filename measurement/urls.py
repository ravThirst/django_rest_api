from django.urls import path

from django.urls import path
from .views import (
    SensorListCreateView, SensorDetailView, TemperatureMeasurementListCreateView,
    TemperatureMeasurementDetailView, CreateSensorView, CreateTemperatureMeasurementView
)

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', TemperatureMeasurementListCreateView.as_view(), name='measurement-list-create'),
    path('measurements/<int:pk>/', TemperatureMeasurementDetailView.as_view(), name='measurement-detail'),
    path('create-sensor/', CreateSensorView.as_view(), name='create-sensor'),
    path('create-measurement/', CreateTemperatureMeasurementView.as_view(), name='create-measurement'),
]
