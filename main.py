from fastapi import FastAPI

app = FastAPI()

# Base de datos simulada
servers = {}

@app.get("/")
def home():
    return {"status": "DeskBot API running"}

@app.get("/check/{guild_id}")
def check_server(guild_id: int):
    active = servers.get(guild_id, False)
    return {"active": active}

@app.post("/activate/{guild_id}")
def activate_server(guild_id: int):
    servers[guild_id] = True
    return {"active": True}

# Arranque del servidor
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
