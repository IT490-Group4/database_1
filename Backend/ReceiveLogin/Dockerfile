FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh", "mysql:3306", "--", "python", "recLogin.py"] 