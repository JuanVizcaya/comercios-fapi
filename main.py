from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def users_registration():    
    return {"message": "Hello World1"}
