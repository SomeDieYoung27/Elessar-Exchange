import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from src.graph import Workflow
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Gmail Automation",
    version="1.0",
    description="LangGraph backend for the AI Gmail automation workflow",
)

#Set all the CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

def get_runnable():
    return Workflow().app

runnable = get_runnable()

add_routes(app, runnable)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
