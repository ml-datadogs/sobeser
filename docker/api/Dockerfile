FROM python:3.11-buster

ENV PYTHONPATH=/sobeser/

COPY api/ /sobeser/api/
COPY secrets/ /sobeser/secrets/
COPY docker/api/main.py /sobeser/main.py
COPY requirements.txt /sobeser/requirements.txt

RUN pip3 install -r /sobeser/requirements.txt

WORKDIR /sobeser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "12300"]
