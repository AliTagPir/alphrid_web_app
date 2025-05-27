from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import charts, tracker, auth

app = FastAPI(
    title="ALPHRID API",
    version="1.0.0"
)

# CORS configuration (adjust origins as needed for your Vue dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(charts.router, prefix="/charts", tags=["Charts"])
app.include_router(tracker.router, prefix="/track", tags=["Tracker"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])