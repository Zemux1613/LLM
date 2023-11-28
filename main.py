import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can choose a different model if needed
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = TFGPT2LMHeadModel.from_pretrained(model_name)

# Encode input prompt
run = True
while run:
    prompt = input("prompt: ")
    if "cancel" in prompt:
        run = False
        break

    input_ids = tokenizer.encode(prompt, return_tensors="tf")

    # Generate text based on the input prompt
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50,
                            top_p=0.95)

    # Decode and print the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("AI: ", generated_text)
