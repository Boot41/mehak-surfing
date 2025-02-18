from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import Organization, Employee, Assignment, AssignmentAllocation
from rest_framework import serializers

# Create your views here.

# Serializers
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1  # This will include the full user and organization details

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentAllocation
        fields = '__all__'
        depth = 1  # This will include the full employee and assignment details

# Root API View
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'organizations': reverse('organization-list', request=request, format=format),
        'employees': reverse('employee-list', request=request, format=format),
        'assignments': reverse('assignment-list', request=request, format=format),
        'assignment-allocations': reverse('assignmentallocation-list', request=request, format=format),
    })

# ViewSets
class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssignmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AssignmentAllocation.objects.all()
    serializer_class = AssignmentAllocationSerializer
