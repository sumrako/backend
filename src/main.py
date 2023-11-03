from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.log_routes import log_router

import uvicorn


app = FastAPI()
app.add_middleware(CORSMiddleware)
app.include_router(log_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True)