from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import Organization, Employee, Assignment, AssignmentAllocation
from rest_framework import serializers
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

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
        'assignments': '/assignments/',
        'assignment-allocations': reverse('assignmentallocation-list', request=request, format=format),
    })

# ViewSets
class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssignmentAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AssignmentAllocation.objects.all()
    serializer_class = AssignmentAllocationSerializer

# Native Django views for assignments
@csrf_exempt
@require_http_methods(["GET"])
def assignment_list(request):
    assignments = Assignment.objects.all()
    assignments_data = []
    
    for assignment in assignments:
        assignments_data.append({
            'id': assignment.id,
            'title': assignment.title,
            'description': assignment.description,
            'start_date': assignment.start_date.isoformat(),
            'end_date': assignment.end_date.isoformat(),
            'status': assignment.status
        })
    
    return JsonResponse({
        'status': 'success',
        'data': assignments_data
    }, safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def assignment_detail(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        
        # Get all allocations for this assignment
        allocations = AssignmentAllocation.objects.filter(assignment=assignment)
        allocations_data = []
        
        for allocation in allocations:
            employee = allocation.employee
            allocations_data.append({
                'id': allocation.id,
                'employee': {
                    'id': employee.id,
                    'full_name': f"{employee.user.first_name} {employee.user.last_name}",
                    'designation': employee.designation,
                    'employee_type': employee.employee_type
                },
                'start_date': allocation.start_date.isoformat(),
                'end_date': allocation.end_date.isoformat(),
                'status': allocation.status
            })
        
        data = {
            'id': assignment.id,
            'title': assignment.title,
            'description': assignment.description,
            'start_date': assignment.start_date.isoformat(),
            'end_date': assignment.end_date.isoformat(),
            'status': assignment.status,
            'allocations': allocations_data
        }
        
        return JsonResponse({
            'status': 'success',
            'data': data
        })
        
    except Assignment.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Assignment not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

# Native Django views for employees
@csrf_exempt
@require_http_methods(["GET"])
def employee_list(request):
    employees = Employee.objects.all()
    employees_data = []
    
    for employee in employees:
        employees_data.append({
            'id': employee.id,
            'user': {
                'id': employee.user.id,
                'first_name': employee.user.first_name,
                'last_name': employee.user.last_name,
                'email': employee.user.email,
            },
            'designation': employee.designation,
            'employee_type': employee.employee_type,
            'date_joined': employee.date_joined.isoformat(),
            'organization': {
                'id': employee.organization.id,
                'name': employee.organization.name,
            }
        })
    
    return JsonResponse(employees_data, safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def employee_detail(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        
        # Get all assignments for this employee
        allocations = AssignmentAllocation.objects.filter(employee=employee)
        assignments_data = []
        
        for allocation in allocations:
            assignment = allocation.assignment
            assignments_data.append({
                'id': assignment.id,
                'title': assignment.title,
                'description': assignment.description,
                'start_date': assignment.start_date.isoformat(),
                'end_date': assignment.end_date.isoformat(),
                'status': assignment.status,
                'allocation_id': allocation.id,
                'allocation_status': allocation.status
            })
        
        employee_data = {
            'id': employee.id,
            'user': {
                'id': employee.user.id,
                'first_name': employee.user.first_name,
                'last_name': employee.user.last_name,
                'email': employee.user.email,
            },
            'designation': employee.designation,
            'employee_type': employee.employee_type,
            'date_joined': employee.date_joined.isoformat(),
            'organization': {
                'id': employee.organization.id,
                'name': employee.organization.name,
            },
            'assignments': assignments_data
        }
        
        return JsonResponse(employee_data)
        
    except Employee.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Employee not found'
        }, status=404)
