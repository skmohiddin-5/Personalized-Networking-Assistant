from transformers import pipeline

# Load text generation model
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

def generate_starters(event, interests):
    prompt = f"""
Event: {event}
Interests: {interests}

Generate three professional networking conversation starters.
"""

    result = generator(
        prompt,
        max_new_tokens=80,
        num_return_sequences=1,
        do_sample=True
    )

    text = result[0]["generated_text"]

    starters = text.replace(prompt, "").split("\n")

    starters = [s.strip("- ").strip() for s in starters if s.strip()]

    while len(starters) < 3:
        starters.append("I'd love to hear your thoughts on this topic.")

    return starters[:3]