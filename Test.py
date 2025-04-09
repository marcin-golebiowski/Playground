from llama_cpp import Llama

# Example: Offload as many layers as possible to the GPU
llm = Llama(
  model_path="D:\\ai\\gemma-3-27b-it-Q3_K_L.gguf",
  n_gpu_layers=-1, # Set to -1 to offload all possible layers, or a positive integer for a specific number
  n_ctx=20480 # Example context size
)

# Now use the llm object for inference
output = llm("Write me a Mermaid diagram for VISA cards transactions", max_tokens=10000)
print(output)