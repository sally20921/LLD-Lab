import os
import matplotlib.pyplot as plt
import base64
import io
from utils.logging import read_log

def compare_entropy(filenames: list) -> str:
    plt.figure(figsize=(10, 5))

    for filename in filenames:
        try:
            log = read_log(filename)
            entropy = log.get("entropy", [])
            label = log.get("model", "unknown") + " | " + filename.replace(".json", "")
            if entropy:
                plt.plot(entropy, label=label)
            else:
                plt.plot([], [], label=label + " (no data)")
        except Exception as e:
            plt.plot([], [], label=f"{filename} (error: {str(e)})")

    plt.title("Entropy Comparison Across Experiments")
    plt.xlabel("Step")
    plt.ylabel("Entropy")
    plt.legend()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    return encoded

