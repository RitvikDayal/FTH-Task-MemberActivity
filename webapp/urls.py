from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('activity-logs/', views.activityLogs, name='task-list'),
    path('member-activity/<str:pk>/', views.memberActivityLog, name='task-detail'),
    path('log-delete/<str:pk>/', views.memberLogDelete, name='task-delete'),
]