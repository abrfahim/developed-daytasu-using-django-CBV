# DayTasu Task Manager

This is a task management web application built with Django. It allows multiple users to create, view, update, and delete tasks. The application provides a REST API for managing tasks and uses Django templates for rendering views. PostgreSQL is used as the database, and Django ORM is utilized for managing database relations.

## Setup Instructions

1. **Clone the repository:**
   git clone repo_link

3. **Set up a virtual environment:**
   python -m venv env

4. **Install dependencies:**
   pip install -r requirements.txt

5. **Set up environment variables:**
Create a `.env` file in the project root directory and add the following environment variables:

Connect to db, where,

SECRET_KEY=<your-secret-key>
DB_NAME=<your-database-name>
DB_USER=<your-database-user>
DB_PASSWORD=<your-database-password>
DB_HOST=<your-database-host>
DB_PORT=<your-database-port>


6. **Run database migrations:**

7. **Create a superuser (admin):**

8. **Run the development server:**

9. **Access the application:**
Open your web browser and go to http://localhost:8000/

## API Endpoints
- **List all tasks:** `GET /api/tasks/`
- **RetrieveUpdateDelete tasks:** `GET /api/tasks/<int:pk>/`

## Template Views
- **Task List:** http://localhost:8000/ (Login Required)

## Contributing
Contributions are welcome! Feel free to submit pull requests.
