from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset
df = pd.read_csv("marks.csv")  # Make sure this file is committed and pushed to GitHub

@app.get("/api")
def get_marks(name: list[str] = []):
    result = df[df["Name"].isin(name)]["Marks"].tolist()
    return {"marks": result}
