from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('activity-logs/', views.activityLogs, name='task-list'),
    path('member-activity/<int:pk>/', views.memberActivityLog, name='task-detail'),
    path('log-delete/<int:pk>/', views.memberLogDelete, name='task-delete'),
]