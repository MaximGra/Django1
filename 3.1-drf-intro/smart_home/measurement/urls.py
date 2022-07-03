from django.urls import path

from measurement.views import SensorsListView, MeasurementsListView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorsListView.as_view()),
    path('measurements/', MeasurementsListView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
]