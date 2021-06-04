from fastapi import FastAPI
from .routers import image, text, page


app = FastAPI()

app.include_router(image.router)
app.include_router(text.router)
app.include_router(page.router)


@app.get("/")
async def root():
    return {"message": "success"}
