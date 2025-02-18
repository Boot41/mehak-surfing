from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Employee(models.Model):
    EMPLOYEE_TYPES = [
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('CONTRACT', 'Contract'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES)
    designation = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.designation}"

class Assignment(models.Model):
    STATUS_CHOICES = [
        ('NOT_STARTED', 'Not Started'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_STARTED')

    def __str__(self):
        return self.title

class AssignmentAllocation(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.employee} - {self.assignment}"