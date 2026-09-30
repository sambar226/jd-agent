FROM python:3.11-slim
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY . .

# Add the isolated virtual environment to the system path
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# Call uvicorn natively without triggering uv's auto-sync
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
