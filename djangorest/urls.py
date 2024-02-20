
from django.contrib import admin
from django.urls import path, include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('aiinfo/', views.aiquest_info),
    path('aiinfo/<int:pk>', views.aiquest_ins),
    path('aicreate/', views.aiquest_create, name='aicreate'),
]
