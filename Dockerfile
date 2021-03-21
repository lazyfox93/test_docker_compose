FROM python:3.8

COPY requirements.txt .
COPY run_test.py .
COPY wait_for_env.py .
RUN pip install -r requirements.txt
CMD ["python", "wait_for_env.py"]
