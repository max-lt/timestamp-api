# Python Timestamp API

## Docker

### Build image

```
docker build -t timestamp-api .
```

### Run container
```bash
docker run -p 5000:80 --env-file .env -v ./main.py:/app/main.py:ro timestamp-api
```
