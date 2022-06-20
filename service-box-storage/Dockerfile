FROM python:3.8
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8002"]