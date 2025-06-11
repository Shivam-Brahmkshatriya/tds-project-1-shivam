import os
import openai

openai.api_key = os.getenv("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZHMzMDAwMDM0QGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.FnFVGZPMFtUH9QyGOrbZVhjxXFv8UE9KARxZzoM6wu4")

async def run_task(task: str) -> str:
    output_dir = "/tmp/project1/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "task.txt")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": task}]
    )
    result = response.choices[0].message.content

    with open(output_path, "w") as f:
        f.write(result)

    return output_path
