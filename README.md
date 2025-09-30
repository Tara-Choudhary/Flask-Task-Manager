
# Flask Task Manager

## Project Overview
A simple web-based task manager built with Flask. Users can create, edit, and manage tasks via a web interface. The app is ready for local development or containerized deployment with Docker.

## Features
- Add new tasks
- Edit existing tasks (including status)
- Delete tasks
- View all tasks
- Responsive UI with Bootstrap 5

## Built With
- Python 3.11
- Flask
- Flask-SQLAlchemy
- PyMySQL
- Bootstrap 5

![Python](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-ready-green)
  

## Environment Variables
Set the following environment variables (or use the defaults in `config.py`):

- `MYSQL_USER` (default: `user` for Docker, `root` for local)
- `MYSQL_PASSWORD` (default: `userpassword` for Docker, `Tara@1234` for local)
- `MYSQL_HOST` (default: `db` for Docker, `localhost` for local)
- `MYSQL_PORT` (default: `3306`)
- `MYSQL_DB` (default: `taskmanager`)
- `SECRET_KEY` (default: `dev-secret`)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Tara-Choudhary/Flask-Task-Manager.git
cd Flask-Task-Manager
```

### 2. Run with Docker (Recommended)
Ensure you have Docker and Docker Compose installed.
```bash
docker-compose up --build
```
The app will be available at [http://localhost:5000](http://localhost:5000).

*The database will be initialized automatically on first run.*

### 3. Run via Docker Hub

You can run the app directly from Docker Hub without cloning the repo:

```bash
docker pull tara00/flask-task-manager:latest

docker run -d -p 5000:5000 \
  --name flask-task-manager \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=userpassword \
  -e MYSQL_HOST=db \
  -e MYSQL_DB=taskmanager \
  tara00/flask-task-manager:latest
```
Access the app at http://localhost:5000

### 4. Local Development (without Docker)
1. (Optional) Create and activate a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Update environment variables in `config.py` or set them in your shell as needed.
4. Initialize the database:
  ```bash
  python init_db.py
  ```
5. Run the app:
  ```bash
  python app.py
  ```
6. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Deployment Notes
- For production, use a WSGI server (e.g., Gunicorn) instead of the Flask dev server.
- The app is fully dockerized for easy deployment and local development.
- MySQL runs in a separate container and is pre-configured for the app.
- Update environment variables as needed for your environment.

## Project Structure
```
app.py                # Main Flask application
config.py             # Configuration settings
init_db.py            # Database initialization script
requirements.txt      # Python dependencies
Dockerfile            # Docker image definition
docker-compose.yml    # Multi-container orchestration
static/style.css      # Custom styles
templates/            # HTML templates
  base.html
  index.html
  edit_task.html
```
## 📬 Contact

**Author:** Tara Choudhary  

**GitHub:** [Tara-Choudhary](https://github.com/Tara-Choudhary)  

**LinkedIn:** [Tara Choudhary](https://www.linkedin.com/in/tara-choudhary00/)  

**Email:** developer.tarachoudhary@gmail.com


## License
This project is licensed under the MIT License.
