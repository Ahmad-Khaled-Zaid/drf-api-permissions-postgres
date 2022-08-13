from django.urls import path
from .views import ReservationListView,ReservationDetailView


urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation_list'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
]