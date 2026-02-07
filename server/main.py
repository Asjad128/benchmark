from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import math
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI Backend Ready for Benchmarking"}

@app.get("/benchmark")
def benchmark(iterations: Optional[int] = 10000000):
    """CPU-intensive benchmark: heavy math operations to load the BE."""
    start = time.time()
    result = 0
    for i in range(iterations):
        result += math.sqrt(i) * math.log(i + 1) if i > 0 else 0
    end = time.time()
    duration = end - start
    return {
        "status": "completed",
        "iterations": iterations,
        "result": result,
        "duration_ms": round(duration * 1000, 2),
        "throughput": round(iterations / duration, 2)
    }
