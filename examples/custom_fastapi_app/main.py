#!/usr/bin/env python3
import frontend
import uvicorn
from fastapi import FastAPI

app = FastAPI()
frontend.init(app)


@app.get('/')
def read_root():
    return {'Hello': 'World'}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
