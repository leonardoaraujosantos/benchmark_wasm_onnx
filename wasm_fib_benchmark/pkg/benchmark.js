const { fib } = require('./wasm_fib_benchmark');

function benchmark(iterations = 1_000_000) {
  const start = Date.now();
  let total = 0;
  for (let i = 0; i < iterations; i++) {
    total += fib(15);
  }
  const duration = (Date.now() - start) / 1000; // seconds
  console.log(`Total time: ${duration.toFixed(2)}s`);
  console.log(`Executions per second: ${(iterations / duration).toFixed(0)}`);
  console.log(`Result checksum (ignore): ${total}`);
}

benchmark(1_000_000);
