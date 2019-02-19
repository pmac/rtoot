FROM python:3-slim-stretch

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
CMD ["lektor", "server", "-h", "0.0.0.0", "-p", "5000"]
WORKDIR /app
EXPOSE 5000

# Install Python deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
