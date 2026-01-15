from fastapi import FastAPI, HTTPException,UploadFile,File
import uvicorn
import pandas as pd
import csv
import io
import python_multipart
from models import Terrorist
from db import insert_to_mongo



app = FastAPI()


@app.post("/top-threats")
def top_threats(file:UploadFile):
    df = pd.read_csv(file.file)
    df = df.sort_values(by="rate_danger", ascending=False).head(5)
    result = []
    for _, row in df.iterrows():
        threat = Terrorist(
        name=row["name"],
        location=row["location"],
        rate_danger=int(row["rate_danger"])
        )
        result.append(threat)
    insert_to_mongo(result)
    return {
    "count": len(result),
    "top": result
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)





















