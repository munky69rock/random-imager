Random Imager
=============

## Requirements

- python
- sqlite3

## Run Server

```sh
$ FLASK_APP=app.py flask run
```

## Usage

```sh
$ curl localhost:5000 # redirect to random image url
$ curl localhost:5000?json=1 # return random image url
$ curl -X POST -F url=[image_url] localhost:5000 # add image url
```
