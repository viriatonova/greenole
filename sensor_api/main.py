import uvicorn
from api.router import router
from api.settings import API_HOST, API_PORT, DEBUG, RELOAD
from fastapi import FastAPI

app = FastAPI(
    debug=DEBUG,
    title="API CTI",
    version="0.0.1",
    description="Api in development",
    docs_url="/api/v1/docs",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=API_HOST, port=API_PORT, reload=RELOAD)
