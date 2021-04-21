from django.contrib import admin
from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    # path('projects/<int:pk>', views.ActivityDetailView.as_view(), name='project-detail'),
    path('education/', views.ResourceListView.as_view(), name='education'),
    path('resources/<int:pk>', views.ActivityDetailView.as_view(), name='resource-detail'),
    path('gallery/', views.gallery, name='gallery'),
]
