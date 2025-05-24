# Hospital Management System

A Django-based hospital management system for managing patients and prescriptions. This application provides a streamlined interface for healthcare professionals to manage patient records and prescription information.

## Features

- **Patient Management**
 - Add new patients with personal details
 - View complete patient list
 - Update patient information
 - Delete patient records

- **Prescription Management**
 - Create new prescriptions linked to patients
 - Track medication details, dosages, and dates
 - View all prescriptions in the system
 - Update prescription information
 - Delete prescriptions when needed

- **User Interface**
 - Clean, responsive Bootstrap-based interface
 - Intuitive navigation between patients and prescriptions
 - Confirmation dialogs for delete operations

## Installation

1. **Clone the repository**
  ```bash
  git clone https://github.com/FaMaHo/OS-hospital-system.git
  cd hospital-management-system
```
2.  **Create and activate a virtual environment**
  ```bash
  # On macOS/Linux
python -m venv env
source env/bin/activate

  # On Windows
python -m venv env
env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables** (optional)
```bash
# Create a .env file in the project root with:
SECRET_KEY=your_secret_key_here
```

5. **Database configuration**
By default, this project is configured to store the database at ~/hospital_db.sqlite3.
If you prefer a different location, you can set the DB_PATH environment variable:
```bash
# Linux/Mac
export DB_PATH=/your/preferred/path/db.sqlite3

# Windows
set DB_PATH=C:\your\preferred\path\db.sqlite3
```

6. **Run migrations**
```bash
python manage.py migrate
```

7. **Create a superuser** (optional, for admin access)
```bash
python manage.py createsuperuser
```

8. Run the development server
```bash
python manage.py runserver
```

9. **Access the application**
Main application: http://127.0.0.1:8000/
Admin interface: http://127.0.0.1:8000/admin/

## Project Structure
```
hospital_system/
├── hospital_app/           # Main application
│   ├── templates/          # HTML templates
│   │   └── hospital_app/   # App-specific templates
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   └── forms.py            # Form definitions
├── hospital_project/       # Project configuration
│   ├── settings.py         # Settings file
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## Database Models
### Patient Model
- ```patient_id```: Unique identifier for each patient (primary key)
- ```nhs_number```: National Health Service number
- ```patient_name```: Full name of the patient
- ```date_of_birth```: Patient's birth date
- ```patient_address```: Patient's residential address

### Prescription Model

- Linked to Patient model via ForeignKey
- Includes medication details, dosage, issue/expiry dates
- Tracks additional medical information

### Technology Stack

- Backend: Django 4.2
- Frontend: HTML, CSS, Bootstrap 5
- Database: SQLite (default)
- Deployment: Compatible with any WSGI-compatible server

## Development

### Adding New Features
1. Create or modify models in ```models.py```
2. Run ```python manage.py makemigrations``` followed by ```python manage.py migrate```
3. Update views, templates and URLs as needed
4. Test thoroughly before committing changes

### Coding Standards

- Follow PEP 8 guidelines for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write tests for new features

### Contributing

1. Fork the repository
2. Create a feature branch: ```git checkout -b feature-name```
3. Commit your changes: ```git commit -m 'Add some feature'```
4. Push to the branch: ```git push origin feature-name```
5. Open a pull request

### Security Considerations

- Default SECRET_KEY is for development only
- For production, set environment variables for all sensitive data
- DEBUG should be set to False in production
- Review Django's deployment checklist before going live
