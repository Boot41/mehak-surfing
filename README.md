# Full-Stack Employee Assignment Management System

A modern web application built with Django REST Framework backend and React/Vite frontend for managing employee assignments within organizations.

## 🚀 Tech Stack

### Backend
- Python 3.x
- Django 5.1.6
- Django REST Framework 3.15.2
- SQLite (Development)

### Frontend
- React
- Vite
- Node.js 18.x

### Infrastructure
- Docker
- Docker Compose

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🛠️ Installation & Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd boot41-feb
```

2. Create environment files:

For the server (./server/.env):
```bash
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

For the client (./client/.env):
```bash
VITE_API_URL=http://localhost:8000
```

3. Build and start the containers:
```bash
docker-compose up --build
```

## 🚀 Running the Application

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Django Admin: http://localhost:8000/admin/

### Available API Endpoints

- Organizations: http://localhost:8000/api/organizations/
- Employees: http://localhost:8000/api/employees/
- Assignments: http://localhost:8000/api/assignments/
- Assignment Allocations: http://localhost:8000/api/assignment-allocations/

## 💻 Development

### Backend Development

1. Access the Django admin interface:
   - URL: http://localhost:8000/admin/
   - Create a superuser (if needed):
     ```bash
     docker-compose exec server python manage.py createsuperuser
     ```

2. View API documentation:
   - Browse the API at http://localhost:8000/api/

### Frontend Development

The React application will automatically reload when you make changes to the frontend code.

## 🛑 Stopping the Application

To stop the application:
```bash
docker-compose down
```

To stop and remove all containers, networks, and volumes:
```bash
docker-compose down -v
```

## 📝 Project Structure

```
boot41-feb/
├── client/                 # React/Vite frontend
│   ├── src/               # Source files
│   ├── Dockerfile         # Frontend Docker configuration
│   └── package.json       # Frontend dependencies
├── server/                # Django backend
│   ├── core/             # Django project settings
│   ├── schema/           # Main application
│   ├── Dockerfile        # Backend Docker configuration
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Docker compose configuration
└── README.md            # Project documentation
```

## 🔒 Environment Variables

### Backend (.env)
- `DJANGO_SECRET_KEY`: Django secret key
- `DJANGO_DEBUG`: Debug mode (1 for development, 0 for production)
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Frontend (.env)
- `VITE_API_URL`: Backend API URL

## 🤝 Contributing

1. Create a feature branch
2. Commit your changes
3. Push to the branch
4. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
