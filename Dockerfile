FROM python:3.6

WORKDIR /app

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
ADD hs-plugins hs-plugins

RUN pipenv install --deploy

ENTRYPOINT ["pipenv"]
CMD ["run", "python3", "/app/hs-plugins/"]