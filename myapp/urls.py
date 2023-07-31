from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job_listings/', views.job_listings, name='job_listings'),
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'),
]
