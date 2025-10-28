from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),               # Frontend
    path('predict/', views.predict_survival, name='predict_survival'),  # API
]

