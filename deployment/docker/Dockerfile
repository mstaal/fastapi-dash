ARG CONTAINER_PYTHON_IMAGE
FROM --platform=linux/amd64 ${CONTAINER_PYTHON_IMAGE}

ARG PROJECT_DIR=.
ARG POETRY_VERSION
# Create user to avoid running as root
RUN useradd --create-home app

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=${POETRY_VERSION}

# Update pip
RUN pip install --upgrade pip

# Install poetry
COPY install-poetry.py .
RUN python ./install-poetry.py
ENV PATH="$PATH:$POETRY_HOME/bin"

# Copy and modify paths to local monorepo libs in poetry files
# to ensure recursive dependencies are resolved correctly.
COPY ${PROJECT_DIR}/pyproject.toml ${PROJECT_DIR}/poetry.lock ./


# Install dependencies, not application
RUN poetry install --no-root --no-cache --no-interaction --no-ansi

COPY ${PROJECT_DIR}/app ./app

# Install application, needed for jobs to find "petry"
RUN poetry install --only main

EXPOSE 20409
CMD ["uvicorn", "app.server.main:app", "--host", "0.0.0.0", "--port", "20409", "--proxy-headers", "--forwarded-allow-ips", "*"]
