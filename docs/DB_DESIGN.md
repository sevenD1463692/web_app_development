# Database Design (MyLife)

## ER Diagram

```mermaid
erDiagram
    USERS ||--o{ TASKS : owns
    USERS ||--o{ LEDGER_ENTRIES : records
    USERS ||--o{ NOTES : writes
    USERS ||--o{ EVENT_REGISTRATIONS : registers
    USERS ||--o{ RECIPES : saves
    EVENTS ||--o{ EVENT_REGISTRATIONS : has

    USERS {
        int id PK
        string username
        string email
        string password_hash
        datetime created_at
    }

    TASKS {
        int id PK
        int user_id FK
        string title
        text description
        datetime due_date
        boolean is_completed
        datetime created_at
    }

    LEDGER_ENTRIES {
        int id PK
        int user_id FK
        float amount
        string type "income/expense"
        string category
        date entry_date
        text note
        datetime created_at
    }

    NOTES {
        int id PK
        int user_id FK
        string book_title
        string chapter
        text content
        datetime created_at
        datetime updated_at
    }

    EVENTS {
        int id PK
        string title
        text description
        datetime event_date
        int capacity
        datetime created_at
    }

    EVENT_REGISTRATIONS {
        int id PK
        int user_id FK
        int event_id FK
        datetime registered_at
    }

    RECIPES {
        int id PK
        int user_id FK
        string title
        text ingredients
        text steps
        string tags
        datetime created_at
    }
```

## Table Descriptions

### users
Stores user account information.
- `id`: Primary key.
- `username`: Unique username.
- `email`: Unique email address.
- `password_hash`: Salted and hashed password.
- `created_at`: Account creation timestamp.

### tasks
Stores to-do list items.
- `user_id`: Foreign key to users.
- `title`: Task summary.
- `due_date`: Optional deadline.
- `is_completed`: Completion status.

### ledger_entries
Stores financial transactions.
- `type`: Either 'income' or 'expense'.
- `amount`: Monetary value.
- `entry_date`: Date of transaction.

### notes
Stores reading notes.
- `book_title`: Name of the book.
- `chapter`: Chapter or section.
- `content`: The actual note text.

### events
Stores available events for registration.
- `event_date`: When the event takes place.
- `capacity`: Maximum number of participants.

### event_registrations
Join table for user-event enrollment.
- `user_id`: Foreign key to users.
- `event_id`: Foreign key to events.

### recipes
Stores cooking recipes.
- `ingredients`: List of ingredients.
- `steps`: Preparation steps.
- `tags`: Categorization tags (comma-separated or JSON).
