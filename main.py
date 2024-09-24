from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.pages_routes import page_router

# Initialise our fastapi app
app = FastAPI(title="Favicba Hotel & Gardens", description="A simple website for Favicba")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Include routers
app.include_router(page_router)







