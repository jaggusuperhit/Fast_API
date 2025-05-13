from transformers import pipeline

# Initialize the generator with more robust settings
generator = pipeline(
    "text-generation", 
    model="gpt2",
    device="cpu",  # or "cuda" if you have GPU
    framework="pt"  # PyTorch
)