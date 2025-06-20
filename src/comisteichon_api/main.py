from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/health", tags=["Healthcheck"])
async def healthcheck():
    return JSONResponse(status_code=200, content={"status": "ok"})
