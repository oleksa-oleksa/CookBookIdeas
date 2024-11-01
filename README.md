# Project Documentation
This project is a web application designed to manage and display recipes, with the backend handling data storage and retrieval and the frontend providing a user interface for creating and viewing recipe data. The setup includes:

Backend: A FastAPI-based API to manage recipes.
Frontend: An Angular app that allows users to interact with the data, create new recipes, and view existing ones.

## Backend (FastAPI)
The backend is built with FastAPI, a Python web framework optimized for building APIs quickly and efficiently. The primary functions include:

<b>API Endpoints:</b> The FastAPI server exposes RESTful endpoints for creating, retrieving, updating, and deleting recipes. Endpoints include:

POST /receipts/: Adds a new recipe to the database.
GET /receipts/: Retrieves all recipes.
GET /receipts/{id}: Retrieves a specific recipe by ID.

<b>Database:</b> Recipes are stored in a relational database, managed through SQLAlchemy. Each recipe entry has fields like:

title, photo_url, ingredients (array of ingredient objects), 
preparation_steps (array of strings), 
tags, date_added, date_cooked, and rating.
default_servings: Defaults to null unless specified.

<b>Data Validation:</b> The backend uses Pydantic models to validate incoming data for consistency and type-checking, ensuring that only correctly structured data is saved.

CORS: The backend includes CORS settings, allowing the Angular frontend to access the API.

## Frontend (Angular)
The frontend is an Angular application providing an interactive interface for managing recipes. Main components include:

<b>Components:</b>
app.component.ts: The root component that initializes the app.
recipe-list.component.ts: Displays the list of all recipes. It fetches data from the backend using the RecipeService and iterates over recipes to display them in a structured format.
add-receipt.component.ts: Contains a form for adding a new recipe. It allows users to enter details like the title, ingredients, preparation steps, and more. It has:
Form validation for required fields.
Dynamic addition/removal of ingredients.
recipe-detail.component.ts (optional): Could display a specific recipe with full details if included.

<b>Services:</b>
RecipeService: Handles HTTP requests between the Angular app and the FastAPI backend, making calls to the API endpoints.

## Frontend-Backend Interaction
The Angular frontend interacts with the FastAPI backend using the HttpClient service provided by Angular.

## Data Flow:
<b>GET Requests:</b> When recipe-list.component initializes, it calls the getRecipes method in RecipeService, which sends an HTTP GET request to the backend’s /receipts endpoint. The backend returns a list of recipes, which the component uses to render recipe information in the UI.
<b>POST Requests:</b> When the user fills out the form in add-receipt.component and submits it, the form data is sent as an HTTP POST request to /receipts. The backend validates and saves this data in the database, returning success or error responses that are managed in the component.

<b>rror Handling:</b>
The frontend displays form validation errors in add-receipt.component when the user provides invalid input.
Backend errors, such as CORS or validation issues, are logged in the console or displayed in the UI as needed.
Routing:

Angular’s routing configuration directs users to different views: the recipe list, add-recipe form, etc. It also includes a wildcard route to handle undefined URLs gracefully by redirecting users back to the /receipts page.

## Application Workflow
<b>Adding a New Recipe:</b>
The user navigates to the add-receipt page and fills out the form.
On submission, Angular collects the form data and sends it to the backend.

FastAPI validates the data and saves it in the database if valid.

Upon success, the Angular app redirects the user to the recipe-list page, where the new recipe is displayed.
Viewing Recipes:

The user lands on the main page (/receipts), which triggers a call to fetch all recipes.
The data returned by the backend is displayed in a structured list view.

<hr>
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
