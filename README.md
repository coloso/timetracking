# Timetracking
### Container
| name  | contains      | port |
|-------|---------------|------|
| web   | python 3.10.4 | 8000 |
| db    | postgres 14.2 | 5432 |


### Install
* https://www.docker.com/get-started/
* https://docs.docker.com/samples/django/
* https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html#config-docker
* https://data-flair.training/blogs/django-orm-tutorial/

build container:
```shell
docker-compose up
```

execute django commands:
```shell
docker-compose run web python [command]
```

### App
http://localhost:8000/