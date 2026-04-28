# Route Design (MyLife)

This document outlines the URL structure, HTTP methods, and template mappings for the MyLife system.

## 1. Route Overview

| Domain | Feature | Method | URL Path | Template | Description |
|--------|---------|--------|----------|----------|-------------|
| **Auth** | Login | GET | `/auth/login` | `auth/login.html` | Display login form |
| | Login | POST | `/auth/login` | — | Authenticate user and redirect |
| | Register | GET | `/auth/register` | `auth/register.html` | Display registration form |
| | Register | POST | `/auth/register` | — | Create user and redirect to login |
| | Logout | GET | `/auth/logout` | — | Clear session and redirect |
| **Tasks** | List Tasks | GET | `/tasks/` | `tasks/index.html` | Show user's to-do list |
| | Add Task | POST | `/tasks/add` | — | Create new task |
| | Edit Task | GET | `/tasks/edit/<id>` | `tasks/edit.html` | Show task edit form |
| | Update Task | POST | `/tasks/update/<id>` | — | Save task changes |
| | Delete Task | POST | `/tasks/delete/<id>` | — | Remove task |
| **Accounting** | Overview | GET | `/accounting/` | `accounting/index.html` | Summary and recent entries |
| | Add Entry | POST | `/accounting/add` | — | Record income or expense |
| | Statistics | GET | `/accounting/stats` | `accounting/stats.html` | Visual charts of finances |
| **Notes** | List Notes | GET | `/notes/` | `notes/index.html` | List all reading notes |
| | New Note | GET | `/notes/new` | `notes/edit.html` | Show blank note editor |
| | Edit Note | GET | `/notes/edit/<id>` | `notes/edit.html` | Show existing note editor |
| | Save Note | POST | `/notes/save` | — | Create or update note |
| | Delete Note | POST | `/notes/delete/<id>` | — | Remove note |
| **Events** | All Events | GET | `/events/` | `events/index.html` | Browse upcoming events |
| | Detail | GET | `/events/<id>` | `events/detail.html` | Show event details |
| | Register | POST | `/events/register/<id>` | — | Sign up for an event |
| **Recipes** | Collection | GET | `/recipes/` | `recipes/index.html` | List user's recipes |
| | New Recipe | GET | `/recipes/new` | `recipes/edit.html` | Show recipe creation form |
| | Edit Recipe | GET | `/recipes/edit/<id>` | `recipes/edit.html` | Show recipe edit form |
| | Save Recipe | POST | `/recipes/save` | — | Create or update recipe |
| | Delete Recipe | POST | `/recipes/delete/<id>` | — | Remove recipe |

## 2. Detailed Route Descriptions

### Authentication
- **Login/Register**: Standard form handling with `werkzeug.security`. Validation errors return to the same page with flash messages.
- **Logout**: Clears `session` and redirects to `/auth/login`.

### Task Management
- **Index**: Filters by `is_completed` (optional query param).
- **Add/Update**: Validates `title` (required) and `due_date`.

### Personal Accounting
- **Index**: Calculates total balance, total income, and total expense for the current month.
- **Add**: Validates `amount` > 0 and `type` matches schema constraints.

### Reading Notebook
- **Save**: Unified route for Create and Update based on presence of `id` in form.

### Event Registration
- **Register**: Checks if `capacity` is exceeded before allowing sign-up.

### Recipe Collection
- **Save**: Handles comma-separated `tags` string and sanitizes `steps` content.

## 3. Jinja2 Template List

All templates inherit from `templates/base.html`.

- `base.html`: Common layout (Navbar, Footer, Flash messages).
- `auth/login.html`: Login form.
- `auth/register.html`: Registration form.
- `tasks/index.html`: Task list with toggles.
- `tasks/edit.html`: Add/Edit task form.
- `accounting/index.html`: Financial dashboard.
- `accounting/stats.html`: Charts and trends.
- `notes/index.html`: Note list.
- `notes/edit.html`: Markdown-supported editor.
- `events/index.html`: Event marketplace.
- `events/detail.html`: Detailed info and register button.
- `recipes/index.html`: Recipe grid/list.
- `recipes/edit.html`: Ingredient and step editor.
