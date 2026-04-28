# Route Design (MyLife)

## Authentication
| Method | URL | Description | Template |
|--------|-----|-------------|----------|
| GET | `/auth/login` | Login page | `auth/login.html` |
| POST | `/auth/login` | Handle login | - |
| GET | `/auth/register` | Registration page | `auth/register.html` |
| POST | `/auth/register` | Handle registration | - |
| GET | `/auth/logout` | Handle logout | - |

## Task Management
| Method | URL | Description | Template |
|--------|-----|-------------|----------|
| GET | `/tasks/` | List all tasks | `tasks/index.html` |
| POST | `/tasks/add` | Add a new task | - |
| POST | `/tasks/update/<int:id>` | Toggle completion or edit | - |
| POST | `/tasks/delete/<int:id>` | Delete a task | - |

## Personal Accounting
| Method | URL | Description | Template |
|--------|-----|-------------|----------|
| GET | `/accounting/` | Overview and history | `accounting/index.html` |
| POST | `/accounting/add` | Record income/expense | - |
| GET | `/accounting/stats` | Visual stats/charts | `accounting/stats.html` |

## Reading Notebook
| Method | URL | Description | Template |
|--------|-----|-------------|----------|
| GET | `/notes/` | List all notes | `notes/index.html` |
| GET | `/notes/add` | New note page | `notes/edit.html` |
| GET | `/notes/edit/<int:id>` | Edit existing note | `notes/edit.html` |
| POST | `/notes/save` | Create/Update note | - |
| POST | `/notes/delete/<int:id>` | Delete note | - |

## Event Registration
| Method | URL | Description | Template |
|--------|-----|-------------|----------|
| GET | `/events/` | List available events | `events/index.html` |
| GET | `/events/<int:id>` | Event details | `events/detail.html` |
| POST | `/events/register/<int:id>` | Enroll in event | - |

## Recipe Collection
| Method | URL | Description | Template |
|--------|-----|-------------|----------|
| GET | `/recipes/` | List all recipes | `recipes/index.html` |
| GET | `/recipes/add` | New recipe page | `recipes/edit.html` |
| GET | `/recipes/edit/<int:id>` | Edit recipe | `recipes/edit.html` |
| POST | `/recipes/save` | Create/Update recipe | - |
| POST | `/recipes/delete/<int:id>` | Delete recipe | - |
