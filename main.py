from fastapi import FastAPI
import uvicorn
import models
from database import engine
from router import blogRoute, userRoute

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blogRoute.router)
app.include_router(userRoute.router)

\

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")