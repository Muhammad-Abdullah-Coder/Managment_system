# Management System

## Project Description
This is a Django-based Management System designed to efficiently manage student information and attendance. It allows authorized users to add, view, update, and delete student records, mark attendance, and manage user settings. The system features user authentication with login/logout functionality.

## Features
- User authentication (login/logout)
- Dashboard displaying all students
- Add new students with detailed information including contact and image
- View individual student details
- Mark and view attendance status (Present/Absent) for students
- Update user account settings (username and email)
- Delete student records with confirmation
- Admin interface for managing student data with search capabilities

## Technology Stack
- Backend: Django (Python)
- Database: Default Django ORM (usually SQLite in development)
- Image processing: Pillow library for resizing student images
- Frontend: Django templates (HTML)
- Authentication: Django’s built-in authentication system

## Installation & Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/username/management-system.git
    cd management-system
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate      # On Windows: env\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    > *If `requirements.txt` is not included, install Django and Pillow manually:*  
    ```bash
    pip install django pillow
    ```

4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the application**
    - Open your browser and go to: `http://127.0.0.1:8000/`
    - Admin panel available at: `http://127.0.0.1:8000/admin/`

## Usage

- Login with your credentials to access the dashboard.
- Add, update, or delete students via the dashboard.
- Mark attendance for students using the attendance form.
- Update your user settings (username/email) through the settings page.
- Logout when finished.

## Folder Structure (Key files)

- `models.py` - Defines Student and Attendance models.
- `views.py` - Handles the views logic for user authentication, CRUD operations, and attendance.
- `forms.py` - Contains Django forms for student, attendance, and user settings.
- `admin.py` - Configures the Django admin panel for Student model.
- `templates/` - Contains HTML templates for different pages (login, dashboard, attendance, etc.)

## Demo Video

If you want to watch the live demo of the project, please click the link below:

[Watch Demo Video](https://drive.google.com/file/d/1sWtfq5pV2-mTXnnD0zCwN24XokaffGdz/view?usp=sharing)

## License
This project is licensed under a proprietary license. All rights reserved by Muhammad Abdullah. Please contact the owner for permissions.

## Contact
- GitHub: [Muhammad-Abdullah-Coder](https://github.com/Muhammad-Abdullah-Coder)
- Email: abdullahme1233@gmail.com

---

*Feel free to customize this README further as your project grows!*
