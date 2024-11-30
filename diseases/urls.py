from django.urls import path
from . import views

urlpatterns = [
    path('diseases/', views.get_diseases),
    path('diseases/<int:disease_id>/', views.get_disease_detail, name='get_disease_detail'),
    path('upload-json/', views.upload_json),
]
