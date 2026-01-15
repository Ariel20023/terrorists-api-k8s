from fastapi import FastAPI, HTTPException,UploadFile
from db import choosing_5_terrorists
import uvicorn
import pandas as pd
import csv
import io



app = FastAPI()


@app.post("/top-threats")
def top_threats(file:UploadFile):
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    return choosing_5_terrorists(reader)




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
