# CampusHub ERP — College Management System

## Project Overview

CampusHub ERP is a Python-based College Management System designed to manage students, faculty members, courses, and student enrollments. The project demonstrates Object-Oriented Programming, database operations, REST APIs, testing, logging, and software design patterns.

## Technologies Used

- Python
- SQLite
- SQLAlchemy
- Flask
- JSON
- Regular Expressions
- `unittest` for testing

## Main Features

- **Student Management:** Add, search, update, and delete student records.
- **Faculty Management:** Manage faculty information.
- **Course Management:** Manage courses and validate course codes.
- **Enrollment Management:** Create, search, update, and delete enrollments.
- **Data Validation:** Validate names, emails, ages, student IDs, phone numbers, and course codes.
- **Database Management:** Store student records using SQLite and SQLAlchemy ORM.
- **REST API:** Provide HTTP endpoints for student CRUD operations.
- **Logging:** Record important operations in `logs/application.log`.
- **Reports and Data Exchange:** Generate reports and support JSON serialization and import/export.
- **Asynchronous Processing:** Demonstrate generators, threading, multiprocessing, and asyncio.

## Project Structure

```text
CampusHubERP/
├── app/
│   ├── api/
│   ├── core/
│   │   └── model_factory.py
│   ├── database/
│   │   ├── connection.py
│   │   ├── orm_connection.py
│   │   └── student_repository.py
│   ├── models/
│   ├── services/
│   └── utils/
├── data/
│   └── campushub.db
├── logs/
│   └── application.log
├── reports/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Install Python.
2. Open a terminal in the project directory.
3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running the Project

Run the main demonstration:

```bash
python main.py
```

Initialize the SQLite database:

```bash
python -m app.database.connection
```

Start the Flask Student API:

```bash
python -m app.api.student_api
```

The API runs at `http://127.0.0.1:5000` when the development server starts successfully.

## Running Tests

Run all discoverable tests:

```bash
python -m unittest discover -s tests -v
```

The project test suite has passed 18 tests in the current development environment.

## Design Patterns

- **Singleton Pattern:** Provides a shared SQLite connection manager.
- **Factory Method Pattern:** Creates Student, Faculty, and Course objects through `ModelFactory`.
- **Repository Pattern:** Separates student database operations from `StudentDBService`.

## Database and Logs

The SQLite database is stored at `data/campushub.db`. Application logs are written to `logs/application.log`. Generated reports are stored in the `reports/` directory.

## Project Purpose

This project demonstrates practical Python programming concepts and the development of a modular college management application.
