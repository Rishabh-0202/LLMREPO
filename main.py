from fastapi import Request, FastAPI, HTTPException,Response
import uvicorn
import json
from app import chatbot


app = FastAPI()

@app.post("/question")
async def question(request: Request):
    message = (await request.json())
    print (message)
    ans = chatbot(message["question"])
    response = json.dumps({"response": ans})
    print(type(response))
    return Response(response,media_type="application/json")

@app.get("/get")
async def get():
    return "Hi"


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
        timeout_keep_alive=65,
    )
