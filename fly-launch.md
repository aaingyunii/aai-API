## Fly.io launch

### fly.io app 만드는 과정 (무료로)

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
```