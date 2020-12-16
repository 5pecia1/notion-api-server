# Notion API Server

It's an API server that can control Notoin's API using REST.

## TODO

- [x] add item with property in database
- [x] add item with content in database
- [ ] add multi page context itme in database
- [x] update item
- [ ] real RESTful
- [ ] notion key in Authorization in http header

## Usage

### Quick Start

```sh
$ NOTION_TOKEN=xxxx
$ docker run --restart always -e NOTION_TOKEN=${NOTION_TOKEN} -p 5000:5000 --name notion 5pecia1/notion-api-server:latest
$ curl --location --request GET 'http://localhost:5000/database' \
--header 'Content-Type: application/json' \
--data-raw '{
    "database": "https://www.notion.so/3e5fa45b1ced42de9344441cbe033079?v=cf8b57ec9a254072b6f4cfb43b06815c",
    "fields": {
        "status": "Not started",
        "name": "api test"
    },
    "content": "test line1\ntest line2"
}' 
$ curl --location --request GET 'http://localhost:5000/database' \
--header 'Content-Type: application/json' \
--data-raw '{
    "database": "https://www.notion.so/3e5fa45b1ced42de9344441cbe033079?v=cf8b57ec9a254072b6f4cfb43b06815c",
    "query": {
        "Status": "Not started"
    },
    "update": {
        "Status": "In progress"
    } 
}' 
```

API Reference: [.http](./.http)

#### JSON Body

* `database`: (string) notion database url
* `fields`: (JSON)notion database item(page) properties.  
    You can add any notion property by JSON key, value
    * `name`: notion database item(page) title
* `content`: (string) notion database item(page) content.  


### Develop

#### Prerequisites

* make
* Docker
* Docker Compose
* python 3.8.x
* pip 3
* virtualenv
    * `pip install virtualenv`

#### Configure

```sh
$ git clone https://github.com/5pecia1/notion-api-server.git
$ cd notion-api-server
$ make init-venv
$ source venv/bin/activate

## exit virtual environment
$ deactivate
```

#### Running

```sh
$ make run
```

#### Docker Build

```sh
$ make docker-build
```

#### Docker Running

```sh
$ make docker-up
```

#### CAUTION for developer

* https://github.com/jamalex/notion-py/issues/132  
* `git clone https://github.com/jamalex/notion-py.git && mv notion-py/notion . && rm -rf notion-py`
* current version: `b7041ade477c1f59edab1b6fc025326d406dd92a`
