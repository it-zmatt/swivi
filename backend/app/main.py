from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import days, tasks, timeslots, weeks

app = FastAPI(title="Swivi API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weeks.router)
app.include_router(days.router)
app.include_router(timeslots.router)
app.include_router(tasks.router)


@app.get("/health")
def health():
    return {"status": "ok"}
