from fastapi import FastAPI
from pydantic import BaseModel
from openenv import PollutionEnv

app = FastAPI()
env = PollutionEnv()

class Action(BaseModel):
    action: int

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(req: Action):
    obs, reward, done, info = env.step(req.action)
    return {
        "obs": obs,
        "reward": reward,
        "done": done,
        "info": info
    }