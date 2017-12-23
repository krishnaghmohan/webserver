FROM python:2.7-slim
WORKDIR /app
ADD ./app
RUN pip install Flask
EXPOSE 8001:8001
CMD {"python","app.py"}
