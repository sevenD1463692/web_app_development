# Flowchart Documentation

## System Flowchart

```mermaid
flowchart TD
    %% User Interaction
    UI[User Interface (Jinja2 Templates)] -->|HTTP Request| Flask[Flask Server]
    Flask --> Auth[Authentication Service]
    Auth -->|Authenticated| ServiceLayer[Service Layer]
    ServiceLayer -->|Calls| DAL[Data Access Layer (SQLite)]
    DAL -->|CRUD Operations| DB[SQLite DB]
    DB --> DAL
    DAL --> ServiceLayer
    ServiceLayer -->|Returns Data| Flask
    Flask -->|Render HTML| UI

    %% Modular Features
    subgraph Features
        Tasks[Task Management]
        Accounting[Personal Accounting]
        Notebook[Reading Notebook]
        Events[Event Registration]
        Recipes[Recipe Collection]
    end
    ServiceLayer --> Tasks
    ServiceLayer --> Accounting
    ServiceLayer --> Notebook
    ServiceLayer --> Events
    ServiceLayer --> Recipes

    %% Feature CRUD flows (example for Tasks)
    Tasks -->|Create| CreateTask[Create Task]
    CreateTask --> DAL
    Tasks -->|Read/List| ListTask[Read Tasks]
    ListTask --> DAL
    Tasks -->|Update| UpdateTask[Update Task]
    UpdateTask --> DAL
    Tasks -->|Delete| DeleteTask[Delete Task]
    DeleteTask --> DAL

    %% Similar CRUD subflows can be imagined for other features
    classDef external fill:#f9f,stroke:#333,stroke-width:2px;
    class UI,Flask,Auth,ServiceLayer,DAL,DB external;
```

*The diagram visualises the high‑level request‑response flow from the UI through Flask, authentication, service layer, data access, and back, as well as the modular feature components and their CRUD interactions.*
