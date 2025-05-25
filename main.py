from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("marks.csv")

@app.get("/api")
def get_marks(name: list[str] = []):
    result = []
    for n in name:
        row = df[df["name"] == n]
        if not row.empty:
            result.append(int(row["marks"].values[0]))
        else:
            result.append(None)
    return {"marks": result}