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
$ curl -X 'GET' 'http://localhost:8000/weather' -H 'accept: application/json'
{"location":"동작구 신대방2동","weather_condition":"맑음","temperature":"18.4"}

$ curl http://localhost:8000/weather
{"location":"동작구 신대방2동","weather_condition":"맑음","temperature":"18.4"}
```

![image](https://github.com/aaingyunii/aai-API/assets/31847834/69a54a31-cd05-4ed7-9277-5e44d0f4c411)


### ref
- https://fastapi.tiangolo.com/ko/#_4
