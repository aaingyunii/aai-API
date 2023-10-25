# aai-API

### preparation
- https://pdm.fming.dev/latest/#installation

```bash
$ source .venv/bin/activate
$ pdm add fastapi
$ pdm add "uvicorn[standard]"
$ pdm add -dG test pytest pytest-cov
$ pdm install
```

### RUN SERVER
- http://localhost:8000/docs
```bash
$ uvicorn app.main:app --reload
```

### API
- http://localhost:8000/docs

```bash
$ curl -X 'GET' 'http://localhost:8000/djw' -H 'accept: application/json'
{"location":"동작구 신대방2동","weather_condition":"맑음","temperature":"18.4"}

$ curl http://localhost:8000/djw
{"location":"동작구 신대방2동","weather_condition":"맑음","temperature":"18.4"}
```

![image](https://github.com/aaingyunii/aai-API/assets/31847834/69a54a31-cd05-4ed7-9277-5e44d0f4c411)

### Docker
- http://localhost:9040/docs

```bash
$ docker build -t aai-api .
$ docker run -dit --name aai-fastapi -p 9040:80 aai-api
```

### Deploy fly.io
- https://aai-api.fly.dev/

```bash
$ fly deploy

Visit your newly deployed app at https://aai-api.fly.dev/

```

### Register Docker-hub

- https://hub.docker.com/r/aaingyunii/aai-api/tags

```bash
$ docker login

$ docker build -t aaingyunii/aai-api:0.5.0 .

$ docker push aaingyunii/aai-api:0.5.0

$ docker tag aaingyunii/aai-api:0.5.0  aaingyunii/aai-api:latest
$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED         SIZE
aaingyunii/aai-api   0.5.0     037732a03f05   3 minutes ago   1.04GB
aaingyunii/aai-api   latest    037732a03f05   3 minutes ago   1.04GB

$ docker push aaingyunii/aai-api

```

![image](https://github.com/aaingyunii/aai-API/assets/31847834/9fb9aa53-0e5b-43be-9969-f265976a0333)


### Ref
- https://fastapi.tiangolo.com/ko/#_4
- https://fastapi.tiangolo.com/ko/deployment/docker/?h=docker

