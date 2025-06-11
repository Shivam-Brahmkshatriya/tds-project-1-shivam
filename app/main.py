from fastapi import FastAPI, Request
from app.agent import run_task
import os

app = FastAPI()

@app.post("/run")
async def run(request: Request):
    query = request.query_params.get("task")
    output_path = await run_task(query)
    return {"output": output_path}

@app.get("/read")
async def read_output(path: str):
    if os.path.exists(path):
        with open(path) as f:
            return {"data": f.read()}
    return {"error": "File not found"}
