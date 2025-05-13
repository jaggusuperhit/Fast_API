from fastapi import FastAPI, HTTPException
from model_loader import generator
from schemas import GenerationRequest, GenerationResponse
import uvicorn

app = FastAPI(title="LLM Inference API")

@app.get("/")
def health_check():
    return {"status": "running", "docs": "http://localhost:8000/docs"}

@app.post("/generate", response_model=GenerationResponse)
async def generate_text(req: GenerationRequest):
    try:
        result = generator(
            req.prompt,
            max_length=req.max_length,
            temperature=req.temperature,
            num_return_sequences=1
        )
        return {"generated_text": result[0]['generated_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("\nAccess these endpoints:")
    print("• API Docs: http://localhost:8000/docs")
    print("• Generate: http://localhost:8000/generate\n")
    uvicorn.run(
        app,
        host="127.0.0.1",  # Explicit localhost
        port=8000,
        log_level="info",
        reload=True
    )