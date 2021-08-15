FROM python:3.9 AS build
# multistage image

LABEL maintainer="noone@localhost"

# This image installs nvm, venv and python3

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# This container with a non privileged user without sudo or password
ENV THEUSER=user
RUN useradd -m -s /bin/bash ${THEUSER}

ADD requirements.txt /app/
RUN chmod -R guo+r /app

USER ${THEUSER}

RUN pip install --no-warn-script-location -r /app/requirements.txt

COPY openapi_client/ /app/openapi_client/
COPY crontab extract-thumbnails.py fetch-submissions.py parse-submission-emails.py requirements.txt /app/

USER root
RUN chmod -R guo+r /app
RUN chmod -R go-w /app

# ----

FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV THEUSER=user
RUN useradd -m -s /bin/bash ${THEUSER}

COPY --from=build /home/${THEUSER} /home/${THEUSER}
COPY --from=build /app /app

USER ${THEUSER}

