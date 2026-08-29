from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')), 
]