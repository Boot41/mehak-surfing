from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from schema.models import Organization, Employee, Assignment, AssignmentAllocation
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create organization
        org = Organization.objects.create(
            name='Tech Innovators Inc.',
            description='Leading technology solutions provider',
            address='123 Innovation Street, Silicon Valley, CA',
            contact_email='contact@techinnovators.com',
            contact_phone='(555) 123-4567'
        )

        # Create users and employees
        employees_data = [
            {
                'username': 'john.doe',
                'email': 'john.doe@techinnovators.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'employee_type': 'FULL_TIME',
                'designation': 'Senior Developer'
            },
            {
                'username': 'jane.smith',
                'email': 'jane.smith@techinnovators.com',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'employee_type': 'FULL_TIME',
                'designation': 'Project Manager'
            },
            {
                'username': 'bob.wilson',
                'email': 'bob.wilson@techinnovators.com',
                'first_name': 'Bob',
                'last_name': 'Wilson',
                'employee_type': 'CONTRACT',
                'designation': 'UI/UX Designer'
            }
        ]

        for emp_data in employees_data:
            user = User.objects.create_user(
                username=emp_data['username'],
                email=emp_data['email'],
                first_name=emp_data['first_name'],
                last_name=emp_data['last_name'],
                password='password123'  # Demo password, should be changed in production
            )
            
            Employee.objects.create(
                user=user,
                organization=org,
                employee_type=emp_data['employee_type'],
                designation=emp_data['designation'],
                date_joined=timezone.now().date()
            )

        # Create assignments
        assignments_data = [
            {
                'title': 'Website Redesign',
                'description': 'Redesign company website with modern UI/UX',
                'status': 'IN_PROGRESS',
                'duration_days': 30
            },
            {
                'title': 'Mobile App Development',
                'description': 'Develop iOS and Android mobile applications',
                'status': 'NOT_STARTED',
                'duration_days': 60
            },
            {
                'title': 'Database Optimization',
                'description': 'Optimize database queries and improve performance',
                'status': 'COMPLETED',
                'duration_days': 15
            }
        ]

        for assignment_data in assignments_data:
            start_date = timezone.now().date()
            end_date = start_date + timedelta(days=assignment_data['duration_days'])
            
            assignment = Assignment.objects.create(
                title=assignment_data['title'],
                description=assignment_data['description'],
                start_date=start_date,
                end_date=end_date,
                status=assignment_data['status']
            )

        # Create assignment allocations
        employees = Employee.objects.all()
        assignments = Assignment.objects.all()

        # Allocate Website Redesign to UI/UX Designer
        AssignmentAllocation.objects.create(
            employee=employees.get(designation='UI/UX Designer'),
            assignment=assignments.get(title='Website Redesign'),
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=30),
            status='ACTIVE'
        )

        # Allocate Mobile App Development to Senior Developer
        AssignmentAllocation.objects.create(
            employee=employees.get(designation='Senior Developer'),
            assignment=assignments.get(title='Mobile App Development'),
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=60),
            status='PENDING'
        )

        # Allocate Database Optimization to Senior Developer
        AssignmentAllocation.objects.create(
            employee=employees.get(designation='Senior Developer'),
            assignment=assignments.get(title='Database Optimization'),
            start_date=timezone.now().date() - timedelta(days=15),
            end_date=timezone.now().date(),
            status='COMPLETED'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
