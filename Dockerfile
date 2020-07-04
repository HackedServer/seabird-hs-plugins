FROM python:3.6

WORKDIR /app

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY hs-plugins .

RUN pipenv install --deploy

WORKDIR /app/hs-plugins

CMD ["pipenv", "run", "python3", "."]