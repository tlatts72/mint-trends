# https://docs.docker.com/engine/reference/builder/

# FROM arm64v8/alpine:3.18
FROM arm64v8/python:3.11-slim-bullseye
# USER root
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
USER root
WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# # into this layer. 
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip3 install -r requirements.txt

# extras
RUN set -eux; \
	pip3 install --upgrade pip; \
	pip3 install numpy --no-use-pep517; \
	pip3 install pandas --no-use-pep517


# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 5000

# # Run the application.
CMD gunicorn 'app:app' --bind=0.0.0.0:5000

# CMD ["sleep", "infinity"]