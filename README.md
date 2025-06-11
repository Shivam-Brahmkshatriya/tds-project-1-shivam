# TDS Project 1 - LLM Automation Agent

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `uvicorn app.main:app --reload`

## Usage
- POST /run?task=... — executes a task
- GET /read?path=... — returns output file

## Docker
```bash
docker build -t tds-project-1 .
docker run -p 8000:8000 tds-project-1
```

## License
MIT
