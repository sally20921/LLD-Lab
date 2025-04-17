# core/lldm_runner.py

def run_experiment(prompt: str, model: str, steps: int = 10):
    # Placeholder: simulate generation
    return {
        "prompt": prompt,
        "model": model,
        "steps": steps,
        "tokens": [f"<{prompt}_{i}>" for i in range(steps)],
        "entropy": [1.0 - (i / steps) for i in range(steps)]
    }

