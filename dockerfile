FROM python:3.14-slim

# Install system dependencies for PostgreSQL
RUN apt-get update && \
	apt-get install -y gcc libpq-dev && \
	rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv


# Set working directory to the package root
WORKDIR /app/vinyl_collection_tool


# Copy dependency files first (for caching)
COPY pyproject.toml uv.lock* ../

# Install dependencies
RUN uv sync --frozen


# Copy the rest of the app
COPY . ../

# Expose FastAPI port
EXPOSE 8000

# Run the app with the correct import context
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]