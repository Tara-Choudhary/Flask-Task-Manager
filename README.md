
# Flask Task Manager

## Project Overview
A simple web-based task manager built with Flask. Users can create, edit, and manage tasks via a web interface.

## Features
- Add new tasks
- Edit existing tasks
- Delete tasks
- View all tasks
- Responsive UI with Bootstrap 5

## Built With
- Python 3.x
- Flask
- SQLAlchemy
- PyMySQL
- Bootstrap 5

## Environment Variables
Set the following environment variables (or use the defaults in `config.py`):

- `MYSQL_USER` (default: `root`)
- `MYSQL_PASSWORD` (default: `Tara@1234`)
- `MYSQL_HOST` (default: `localhost`)
- `MYSQL_DB` (default: `taskdb`)
- `SECRET_KEY` (default: `dev-secret`)

## Setup Instructions

### Clone the repository
```bash
git clone <repo-url>
cd flask-task-manager
```

### Create a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Initialize the database
```bash
python init_db.py
```

### Run the application
```bash
python app.py
```

### Access the app
Open your browser and go to: http://127.0.0.1:5000

## Deployment Notes (for DevOps)
- Ensure the MySQL server is running and credentials in environment variables match your DB.
- For production, use a WSGI server (e.g., Gunicorn) instead of the Flask dev server.
- The app can be dockerized for easier deployment:
  - Expose port 5000 for Flask
  - Map MySQL credentials through environment variables

## Project Structure
```
app.py                # Main Flask application
config.py             # Configuration settings
init_db.py            # Database initialization script
requirements.txt      # Python dependencies
static/style.css      # Custom styles
templates/            # HTML templates
    base.html
    index.html
    edit_task.html
```

## License
This project is licensed under the MIT License.
