FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --create-home learner && chown -R learner:learner /app
USER learner
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
