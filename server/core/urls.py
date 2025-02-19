"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schema.views import (
    OrganizationViewSet,
    EmployeeViewSet,
    AssignmentAllocationViewSet,
    api_root,
    assignment_list,
    assignment_detail,
    employee_list,
    employee_detail
)
from django.views.generic import RedirectView

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'assignment-allocations', AssignmentAllocationViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # Redirect root to API
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Native Django assignment endpoints
    path('api/assignments/', assignment_list, name='assignment-list'),
    path('api/assignments/<int:assignment_id>/', assignment_detail, name='assignment-detail'),
    # Native Django employee endpoints
    path('api/employees/', employee_list, name='employee-list'),
    path('api/employees/<int:employee_id>/', employee_detail, name='employee-detail'),
]
