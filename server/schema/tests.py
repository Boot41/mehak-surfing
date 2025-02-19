from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Assignment, Organization, Employee, AssignmentAllocation
from datetime import date, timedelta
import json

# Create your tests here.

class AssignmentAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create test data
        self.organization = Organization.objects.create(
            name="Test Org",
            description="Test Description",
            address="Test Address",
            contact_email="test@example.com",
            contact_phone="1234567890"
        )
        
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            password="testpass123"
        )
        
        # Create an employee
        self.employee = Employee.objects.create(
            user=self.user,
            organization=self.organization,
            employee_type="FULL_TIME",
            designation="Developer",
            date_joined=date.today()
        )
        
        # Create test assignments
        self.assignments = []
        for i in range(3):
            assignment = Assignment.objects.create(
                title=f"Test Assignment {i+1}",
                description=f"Test Description {i+1}",
                start_date=date.today(),
                end_date=date.today() + timedelta(days=30),
                status="NOT_STARTED"
            )
            self.assignments.append(assignment)
        
        # Create an assignment allocation
        self.allocation = AssignmentAllocation.objects.create(
            employee=self.employee,
            assignment=self.assignments[0],
            start_date=date.today(),
            end_date=date.today() + timedelta(days=30),
            status="PENDING"
        )

    def test_assignment_list_success(self):
        """Test successful retrieval of all assignments"""
        response = self.client.get('/api/assignments/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(len(data['data']), 3)  # We created 3 assignments
        
        # Verify the structure of returned data
        first_assignment = data['data'][0]
        self.assertIn('id', first_assignment)
        self.assertIn('title', first_assignment)
        self.assertIn('description', first_assignment)
        self.assertIn('start_date', first_assignment)
        self.assertIn('end_date', first_assignment)
        self.assertIn('status', first_assignment)

    def test_assignment_detail_success(self):
        """Test successful retrieval of a single assignment with allocations"""
        assignment_id = self.assignments[0].id
        response = self.client.get(f'/api/assignments/{assignment_id}/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        
        # Verify assignment data
        assignment_data = data['data']
        self.assertEqual(assignment_data['id'], assignment_id)
        self.assertEqual(assignment_data['title'], 'Test Assignment 1')
        
        # Verify allocations
        self.assertIn('allocations', assignment_data)
        self.assertEqual(len(assignment_data['allocations']), 1)
        
        # Verify allocation data structure
        allocation = assignment_data['allocations'][0]
        self.assertIn('employee', allocation)
        self.assertEqual(allocation['employee']['full_name'], 'Test User')
        self.assertEqual(allocation['status'], 'PENDING')

    def test_assignment_detail_not_found(self):
        """Test requesting a non-existent assignment"""
        non_existent_id = 9999
        response = self.client.get(f'/api/assignments/{non_existent_id}/')
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Assignment not found')

    def test_assignment_list_empty(self):
        """Test assignment list when no assignments exist"""
        # Delete all assignments
        Assignment.objects.all().delete()
        
        response = self.client.get('/api/assignments/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(len(data['data']), 0)

    def test_assignment_detail_with_multiple_allocations(self):
        """Test assignment detail with multiple employee allocations"""
        # Create another user and employee
        user2 = User.objects.create_user(
            username="testuser2",
            first_name="Test2",
            last_name="User2",
            email="testuser2@example.com",
            password="testpass123"
        )
        
        employee2 = Employee.objects.create(
            user=user2,
            organization=self.organization,
            employee_type="PART_TIME",
            designation="Designer",
            date_joined=date.today()
        )
        
        # Allocate the same assignment to another employee
        AssignmentAllocation.objects.create(
            employee=employee2,
            assignment=self.assignments[0],
            start_date=date.today(),
            end_date=date.today() + timedelta(days=15),
            status="ACTIVE"
        )
        
        response = self.client.get(f'/api/assignments/{self.assignments[0].id}/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertEqual(len(data['data']['allocations']), 2)
        
        # Verify both allocations are present
        allocation_statuses = [a['status'] for a in data['data']['allocations']]
        self.assertIn('PENDING', allocation_statuses)
        self.assertIn('ACTIVE', allocation_statuses)

    def test_invalid_assignment_id_format(self):
        """Test requesting assignment with invalid ID format"""
        response = self.client.get('/api/assignments/invalid_id/')
        self.assertEqual(response.status_code, 404)

    def test_assignment_list_method_not_allowed(self):
        """Test unsupported HTTP methods for assignment list"""
        # Test POST request
        response = self.client.post('/api/assignments/')
        self.assertEqual(response.status_code, 405)
        
        # Test PUT request
        response = self.client.put('/api/assignments/')
        self.assertEqual(response.status_code, 405)
        
        # Test DELETE request
        response = self.client.delete('/api/assignments/')
        self.assertEqual(response.status_code, 405)
