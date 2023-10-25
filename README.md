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
$ flyctl auth login

$ flyctl launch
Creating app in /home/ika/code/aai-API
Scanning source code
Detected a Dockerfile app
? Choose an app name (leave blank to generate one): aai-api
automatically selected personal organization: aaingyunii
Some regions require a paid plan (bom, fra, maa).
See https://fly.io/plans to set up a plan.

? Choose a region for deployment: Tokyo, Japan (nrt)
App will use 'nrt' region as primary

Created app 'aai-api' in organization 'personal'
Admin URL: https://fly.io/apps/aai-api
Hostname: aai-api.fly.dev
? Would you like to set up a Postgresql database now? No
? Would you like to set up an Upstash Redis database now? No
? Create .dockerignore from 4 .gitignore files? No
Wrote config file fly.toml
? Would you like to deploy now? No
Validating /home/ika/code/aai-API/fly.toml
Platform: machines
✓ Configuration is valid
Your app is ready! Deploy with `flyctl deploy`

$ tail -n 13  fly.toml
app = "aai-api"
primary_region = "nrt"

[build]
  dockerfile = "Dockerfile"

[http_service]
  internal_port = 80
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 3
  processes = ["app"]


$ fly deploy
Visit your newly deployed app at https://aai-api.fly.dev/

```
### Ref
- https://fastapi.tiangolo.com/ko/#_4
- https://fastapi.tiangolo.com/ko/deployment/docker/?h=docker

