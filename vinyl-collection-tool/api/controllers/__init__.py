"""Endpoints for the API."""

from api.controllers.session_controller import router as session_router

routers = [session_router]