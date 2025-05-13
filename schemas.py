from pydantic import BaseModel
from typing import Optional

class GenerationRequest(BaseModel):
    prompt: str
    max_length: Optional[int] = 100
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9  # Added common generation parameter
    do_sample: Optional[bool] = True  # Added sampling flag

class GenerationResponse(BaseModel):
    generated_text: str