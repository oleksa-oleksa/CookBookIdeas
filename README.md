# Project Documentation
This project is a web application designed to manage and display recipes, with the backend handling data storage and retrieval and the frontend providing a user interface for creating and viewing recipe data. The setup includes:

Backend: A FastAPI-based API to manage recipes.
Frontend: An Angular app that allows users to interact with the data, create new recipes, and view existing ones.

# Backend (FastAPI)
The backend is built with FastAPI, a Python web framework optimized for building APIs quickly and efficiently. The primary functions include:

<b> API Endpoints:</b> The FastAPI server exposes RESTful endpoints for creating, retrieving, updating, and deleting recipes. Endpoints include:

POST /receipts/: Adds a new recipe to the database.
GET /receipts/: Retrieves all recipes.
GET /receipts/{id}: Retrieves a specific recipe by ID.

## Database: Recipes are stored in a relational database, managed through SQLAlchemy. Each recipe entry has fields like:

title, photo_url, ingredients (array of ingredient objects), 
preparation_steps (array of strings), 
tags, date_added, date_cooked, and rating.
default_servings: Defaults to null unless specified.

## Data Validation: The backend uses Pydantic models to validate incoming data for consistency and type-checking, ensuring that only correctly structured data is saved.

CORS: The backend includes CORS settings, allowing the Angular frontend to access the API.

# Frontend (Angular)
The frontend is an Angular application providing an interactive interface for managing recipes. Main components include:

## Components:

app.component.ts: The root component that initializes the app.
recipe-list.component.ts: Displays the list of all recipes. It fetches data from the backend using the RecipeService and iterates over recipes to display them in a structured format.
add-receipt.component.ts: Contains a form for adding a new recipe. It allows users to enter details like the title, ingredients, preparation steps, and more. It has:
Form validation for required fields.
Dynamic addition/removal of ingredients.
recipe-detail.component.ts (optional): Could display a specific recipe with full details if included.

## Services:
RecipeService: Handles HTTP requests between the Angular app and the FastAPI backend, making calls to the API endpoints.

------------------------------
To run everything together—backend, frontend, and database, the Docker Compose is used.
Builds the backend and frontend containers from their respective Dockerfiles.
Sets up a PostgreSQL database in a container.
Exposes the backend on port 8000, frontend on port 4200, and database on port 5432.
Uses Docker networks to let the services communicate with each other internally.


Structure:
my-receipt-app/  
├── backend/           # FastAPI backend  
│   ├── app/  
│   ├── Dockerfile  
│   └── requirements.txt  
├── frontend/          # Angular frontend  
│   ├── src/  
│   ├── Dockerfile  
│   └── package.json  
├── database/          # Database (PostgreSQL to run in container)  
│   ├── Dockerfile  
├── docker-compose.yml # Docker Compose for orchestration  
├── .github/  
│   └── workflows/     # GitHub Actions for CI/CD pipelines  
└── README.md  
