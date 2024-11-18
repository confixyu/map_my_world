import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from src.config.settings import settings
from src.routers.api_router import api_router
from src.config.database.sqlmodel import create_db_and_tables


app = FastAPI(title=settings.MS_NAME, openapi_url=f"{settings.API_STR}/openapi.json")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    """Main endpoint to check the service health status"""
    return {"Health": "ok"}


app.include_router(api_router, prefix=settings.API_STR)
add_pagination(app)


async def startup_event():
    await create_db_and_tables()


app.add_event_handler("startup", startup_event)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT_SERVER, reload=settings.DEBUG)
