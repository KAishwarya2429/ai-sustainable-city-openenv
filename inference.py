from fastapi import FastAPI
from pydantic import BaseModel
from openenv import PollutionEnv

app = FastAPI()

env = PollutionEnv()

class ActionRequest(BaseModel):
    action: int

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs, "message": "environment reset successful"}

@app.post("/step")
def step(req: ActionRequest):
    obs, reward, done, info = env.step(req.action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def home():
    return {"status": "OpenEnv running successfully"}