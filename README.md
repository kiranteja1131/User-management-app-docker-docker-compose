# User Management Application

A containerized User Management System built using Python Flask, MongoDB, and Nginx. The application provides user registration, authentication, session management, and a personalized dashboard.

## 🚀 Features

- User Registration
- Secure Password Hashing
- User Login and Authentication
- Session Management
- User Dashboard
- Logout Functionality
- Duplicate Email Prevention
- Password Validation
- MongoDB Data Persistence
- Backend Health Check

## 🏗️ Architecture

The application follows a three-tier containerized architecture.

1. **Frontend:** Nginx serves static HTML, CSS, and JavaScript files.
2. **Backend:** Python Flask provides REST APIs and handles authentication.
3. **Database:** MongoDB stores user information.

Nginx also acts as a reverse proxy, forwarding API requests to the Flask backend.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | REST API development |
| MongoDB | Database |
| Nginx | Frontend web server and reverse proxy |
| Docker | Containerization |
| Docker Compose | Multi-container management |
| HTML, CSS, JavaScript | Frontend development |
| Gunicorn | Python application server |

## 📁 Project Structure

```text
user-management-app/
│
├── frontend/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── Dockerfile
│   └── nginx.conf
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## ⚙️ Run Locally Using Docker

### Prerequisites

- Docker Desktop
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/user-management-app.git
```

### 2. Navigate to the project

```bash
cd user-management-app
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-strong-random-secret
MONGO_URI=mongodb://mongodb:27017/
```

### 4. Build and start containers

```bash
docker compose up -d --build
```

### 5. Verify containers

```bash
docker compose ps
```

### 6. Access the application

Open your browser:

```text
http://localhost:8082
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/register | Register a new user |
| POST | /api/login | Authenticate a user |
| GET | /api/me | Retrieve logged-in user details |
| POST | /api/logout | Log out the user |
| GET | /health | Check backend and database health |

## 🐳 Docker Commands

Start containers:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

View running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f
```

Rebuild application:

```bash
docker compose up -d --build
```

## 💾 Data Persistence

MongoDB uses a Docker named volume called `mongo_data`.

This allows user data to remain available even when containers are stopped, removed, and recreated.

## 🔐 Security

- Passwords are stored using Werkzeug password hashing.
- Environment variables are used for sensitive configuration.
- HTTP-only session cookies are enabled.
- Backend and database ports are not exposed directly to the host.

**Note:** Additional production security measures, including HTTPS, CSRF protection, rate limiting, and MongoDB authentication, should be configured before public deployment.

## 👨‍💻 Author

**Kiran Teja Palyam**

GitHub: https://github.com/kiranteja1131

---

Built as a hands-on project to practice Docker, Docker Compose, Flask, MongoDB, and multi-container application deployment.