from fastapi import FastAPI
from routes.admin import admin_router
import uvicorn

app = FastAPI()

app.include_router(admin_router)

if __name__ == '__main__':
    uvicorn.run("app:app",host="127.0.0.1",port=8000,workers=1)