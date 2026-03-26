"""Endpoints for the API."""

from api.controllers.collection_controller import router as collection_router

routers = [collection_router]