from django.urls import path
from accounts_app.views import (
    RegisterUserFV
)


app_name = 'accounts_app'

urlpatterns = [
    path('register_user/', RegisterUserFV.as_view(), name='register_user')
]