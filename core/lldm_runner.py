from utils.logging import log_run

def run_experiment(prompt: str, model: str, steps: int = 10):
    tokens = [f"<{prompt}_{i}>" for i in range(steps)]
    entropy = [1.0 - (i / steps) for i in range(steps)]
    
    result = {
        "prompt": prompt,
        "model": model,
        "steps": steps,
        "tokens": tokens,
        "entropy": entropy
    }

    result["log_path"] = log_run(result)
    return result

