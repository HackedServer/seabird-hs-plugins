from python:3.6

WORKDIR /app

RUN pip install --no-cache-dir pipenv

COPY Pipfile .
COPY hs-plugins .

RUN pipfile install

WORKDIR /app/hs-plugins

CMD ["pipenv", "run", "python3", "."]