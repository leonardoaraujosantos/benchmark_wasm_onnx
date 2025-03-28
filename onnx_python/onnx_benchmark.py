import onnxruntime as ort
import numpy as np
import time

# Carrega o modelo
session = ort.InferenceSession("model.onnx")  # Substitua pelo seu modelo .onnx
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape
input_dtype = session.get_inputs()[0].type

# Gera dados de entrada aleatórios compatíveis
input_data = np.random.rand(*[dim if isinstance(dim, int) else 1 for dim in input_shape]).astype(np.float32)

# Benchmark
iterations = 100000
start = time.time()
for _ in range(iterations):
    session.run(None, {input_name: input_data})
end = time.time()

# Resultados
duration = end - start
print(f"Total time for {iterations} inferences: {duration:.2f}s")
print(f"Inferences per second: {iterations / duration:.2f}")
