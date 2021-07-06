from django.urls import path
from .views import activation

urlpatterns = [
    path('activate/<str:uid>/<str:token>', activation)
]
