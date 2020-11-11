import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn

app = fastapi.FastAPI()
app.mount("/", StaticFiles(directory="./html", html=True), name="root")
from starlette.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["*"])

uvicorn.run(app, host="0.0.0.0")