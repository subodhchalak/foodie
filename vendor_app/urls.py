from django.urls import path
from vendor_app.views import (
    RegisterVendorCV
)

app_name = 'vendor_app'

urlpatterns = [
    path('register_vendor', RegisterVendorCV.as_view(), name='register_vendor')
]