from django.urls import path
from .views import requestChargingStations, startChargeFromBooking, getSocket, resetSocket
urlpatterns = [
  path("OCPI/getChargingStations", requestChargingStations),
  path("OCPI/startChargeFromBooking", startChargeFromBooking),
  path("OCPI/getSocket/<str:pk>/", getSocket),
  path("OCPI/resetSocket/<str:pk>/", resetSocket)
]