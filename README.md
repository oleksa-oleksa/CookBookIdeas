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
