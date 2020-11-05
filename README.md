# fdk-baseregistries-publisher
A service exposing an endpoint that publishes a catalog of national base registries

## Develop and run locally
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://pypi.org/project/nox-poetry/)

### Install software:
```
% git clone https://github.com/Informasjonsforvaltning/fdk-baseregistries-publisher.git
% cd fdk-baseregistries-publisher
% pyenv install 3.9.0
% pyenv local 3.9.0
% python get-poetry.py
% pipx install nox
% pipx inject nox nox-poetry
% poetry install
```
### Environment variables
To run the service locally, you need to supply a set of environment variables. A simple way to solve this is to supply a .env file in the root directory.

```
FDK_DATASERVICE_HARVESTER_URI=https://dataservices.staging.fellesdatakatalog.digdir.no
```
### Running the API locally
 Start the endpoint:
```
% poetry shell
% FLASK_APP=fdk_baseregistries_publisher FLASK_ENV=development flask run --port=8080
```
## Running the API in a wsgi-server (gunicorn)
```
% poetry shell
% gunicorn  --chdir src "fdk_baseregistries_publisher:create_app()"  --config=src/fdk_baseregistries_publisher/gunicorn_config.py
```
## Running the wsgi-server in Docker
To build and run the api in a Docker container:
```
% docker build -t digdir/fdk-baseregistries-publisher:latest .
% docker run --env-file .env -p 8080:8080 -d digdir/fdk-baseregistries-publisher:latest
```
The easier way would be with docker-compose:
```
docker-compose up --build
```
## Running tests
We use [pytest](https://docs.pytest.org/en/latest/) for contract testing.

To run linters, checkers and tests:
```
% nox
```
