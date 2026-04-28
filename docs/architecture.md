# System Architecture Document

## Overview
The **MyLife 全方位個人生活管理系統** is a web application built with a **Flask** backend, **Jinja2** templating for the UI, and a **SQLite** relational database. The system integrates five core functional domains:
1. 任務管理系統 (Task Management)
2. 個人記帳簿 (Personal Accounting)
3. 讀書筆記本 (Reading Notebook)
4. 活動報名系統 (Event Registration)
5. 食譜收藏夾 (Recipe Collection)

## High‑Level Architecture
```
+-------------------+        +-------------------+        +-------------------+
|  Frontend (UI)    | <----> |   Flask Server    | <----> |   SQLite DB      |
|  (Jinja2)         |        |  (REST/API)       |        | (Data Store)    |
+-------------------+        +-------------------+        +-------------------+
        ^                ^                 ^
        |                |                 |
        |                |                 |
  Auth Middleware   Service Layer   Data Access Layer
```

### 1. Frontend (Jinja2 Templates)
- Renders HTML pages for each feature.
- Uses Bootstrap‑5 for responsive design and custom CSS for premium visual aesthetics (dark mode, gradients, micro‑animations).
- Communicates with the Flask server via standard form submissions and AJAX (Fetch API) for asynchronous actions.

### 2. Backend (Flask)
- **Blueprints** for modular routing: `tasks`, `accounting`, `notes`, `events`, `recipes`, `auth`.
- **Service Layer** implements business logic for each domain (e.g., task status toggling, accounting balance calculations).
- **Authentication**: User registration & login using Werkzeug security (password hashing with PBKDF2). Session‑based auth with Flask‑Login.
- **Security Middleware**: Input validation, CSRF protection (Flask‑WTF), SQL injection prevention via parameterised queries/ORM.
- **Email Scheduler** (optional for MVP later) using `apscheduler` for reminder emails.

### 3. Data Access Layer (SQLite)
- Separate tables for each domain with proper foreign‑key relationships to the `users` table.
- Example schema snippets:
  ```sql
  CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      password_hash TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL
  );

  CREATE TABLE tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER REFERENCES users(id),
      title TEXT NOT NULL,
      description TEXT,
      due_date DATE,
      completed BOOLEAN NOT NULL DEFAULT 0
  );
  ```
- Indexes on frequently queried columns (e.g., `user_id`, `due_date`).

## Component Interaction Flow
1. **User Request** – Browser sends HTTP request (GET/POST) to Flask route.
2. **Auth Check** – Middleware validates session; unauthenticated users are redirected to login.
3. **Business Logic** – Service layer processes the request (e.g., create a task, record a transaction).
4. **Data Persistence** – DAL executes parameterised SQL/ORM calls against SQLite.
5. **Response Generation** – Flask renders a Jinja2 template with updated data or returns JSON for AJAX calls.
6. **UI Update** – Frontend displays the result, optionally with micro‑animations for feedback.

## Security & Non‑Functional Requirements
- **Password Hashing**: `werkzeug.security.generate_password_hash` and `check_password_hash`.
- **Input Sanitisation**: All form data validated server‑side; use `bleach` to sanitise HTML input for notes/recipes.
- **Performance**: Light‑weight Flask app, SQLite file, static assets served via Flask's built‑in static folder or a CDN. Page load < 2 seconds on typical broadband.
- **Privacy**: Row‑level security – each user can only access rows where `user_id` matches their ID.
- **Scalability**: While MVP uses SQLite, the data access layer is abstracted to allow swapping to PostgreSQL in future releases.

## Deployment Considerations (Future)
- Containerise with Docker (Dockerfile, docker‑compose) for consistent environment.
- Use Nginx as a reverse proxy with TLS termination.
- Add CI/CD pipeline (GitHub Actions) to run unit tests and linting.

---
*Document generated automatically from the PRD (docs/PRD.md).*
