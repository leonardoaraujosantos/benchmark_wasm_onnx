import onnxruntime as ort
import numpy as np
import time

# Lista os provedores disponíveis
available_providers = ort.get_available_providers()
print(f"Available execution providers: {available_providers}")

# Verifica se CUDA (GPU) está disponível
use_cuda = 'CUDAExecutionProvider' in available_providers
print(f"Using CUDA: {use_cuda}")

# Cria a sessão com CUDA se disponível
session = ort.InferenceSession(
    "model.onnx",
    providers=['CUDAExecutionProvider', 'CPUExecutionProvider'] if use_cuda else ['CPUExecutionProvider']
)

# Obtém informações da entrada
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape

# Gera dados de entrada aleatórios compatíveis
input_data = np.random.rand(*[dim if isinstance(dim, int) else 1 for dim in input_shape]).astype(np.float32)

# Benchmark
iterations = 100_000
start = time.time()
for _ in range(iterations):
    session.run(None, {input_name: input_data})
end = time.time()

# Resultados
duration = end - start
print(f"Total time for {iterations} inferences: {duration:.2f}s")
print(f"Inferences per second: {iterations / duration:.2f}")