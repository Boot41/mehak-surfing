from django.contrib import admin
from .models import Organization, Employee, Assignment, AssignmentAllocation
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone')
    search_fields = ('name', 'description')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'employee_type', 'designation', 'date_joined')
    list_filter = ('organization', 'employee_type')
    search_fields = ('user__username', 'designation')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')

@admin.register(AssignmentAllocation)
class AssignmentAllocationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'assignment', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'employee__organization')
    search_fields = ('employee__user__username', 'assignment__title')