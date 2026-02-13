from django.urls import path

from .views import payment_process_view, payment_callback_view

app_name='payment'

urlpatterns = [
    path('process/', payment_process_view, name='payment_process'),
    path('callback/', payment_callback_view, name='payment_callback'),
]