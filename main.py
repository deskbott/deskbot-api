from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

active_servers = {}  # Para pruebas, simula base de datos

class ActivatePlan(BaseModel):
    guild_id: int

@app.get("/check/{guild_id}")
def check_plan(guild_id: int):
    return {"active": active_servers.get(guild_id, False)}

@app.post("/activate")
def activate_plan(data: ActivatePlan):
    active_servers[data.guild_id] = True
    return {"message": f"Guild {data.guild_id} activated."}

@app.post("/deactivate")
def deactivate_plan(data: ActivatePlan):
    active_servers[data.guild_id] = False
    return {"message": f"Guild {data.guild_id} deactivated."}
