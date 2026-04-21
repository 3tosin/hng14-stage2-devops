# FIXES

## Issue 1
File: api/main.py  
Problem: Redis connection hardcoded to localhost, which breaks in containerized environments  
Fix: Replaced with environment variables (REDIS_HOST, REDIS_PORT) and defaulted to 'redis'

## Issue 2
File: worker/worker.py  
Problem: Redis connection hardcoded to localhost, preventing communication with Redis container  
Fix: Replaced with environment variables (REDIS_HOST, REDIS_PORT) and defaulted to 'redis'

## Issue 3
File: frontend/app.js  
Problem: API URL hardcoded to localhost, which prevents frontend container from reaching API container  
Fix: Replaced with environment variable (API_URL) and defaulted to 'http://api:8000'

## Issue 4
File: frontend/Dockerfile  
Problem: Missing FROM instruction causing Docker build to fail  
Fix: Added base image (node:18-alpine)

## Issue 5
File: api/main.py  
Problem: Incorrect usage of os.getenv() with invalid keyword argument 'port' causing runtime failure  
Fix: Corrected to proper usage with positional default value and cast port to integer

## Issue 6
File: api/Dockerfile  
Problem: Healthcheck used curl but curl was not installed, causing container to be marked unhealthy  
Fix: Installed curl in the image and cleaned apt cache
