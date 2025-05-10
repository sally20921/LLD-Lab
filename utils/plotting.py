import matplotlib.pyplot as plt
import io
import base64

def plot_entropy(entropy: list):
    plt.figure(figsize=(8, 4))
    plt.plot(entropy, marker='o')
    plt.title("Entropy Over Time")
    plt.xlabel("Step")
    plt.ylabel("Entropy")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

