import os
import json
from utils.logging import LOG_DIR

def summarize_log(filename: str) -> str:
    try:
        # Build full path to the log file
        filepath = os.path.join(LOG_DIR, filename)
        if not os.path.exists(filepath):
            return f"[Error] Log file not found: {filepath}"

        # Read the log content
        with open(filepath, "r") as f:
            log = json.load(f)

        # Extract fields
        prompt = log.get("prompt", "N/A")
        model = log.get("model", "N/A")
        steps = log.get("steps", 0)
        entropy = log.get("entropy", [])
        tokens = log.get("tokens", [])

        # Start summary
        summary = f"🧪 **Experiment Summary** for prompt: \"{prompt}\" using model `{model}`\n"
        summary += f"- Steps taken: `{steps}`\n"

        if entropy:
            start_e = round(entropy[0], 4)
            end_e = round(entropy[-1], 4)
            delta_e = round(start_e - end_e, 4)
            summary += f"- Entropy: `{start_e} → {end_e}` (Δ = {delta_e})\n"

            if delta_e > 0.7:
                summary += "→ Strong convergence detected.\n"
            elif delta_e > 0.3:
                summary += "→ Moderate convergence.\n"
            else:
                summary += "→ Weak or unstable convergence.\n"
        else:
            summary += "- No entropy data available.\n"

        if tokens:
            summary += f"- Output tokens: `{len(tokens)}` total\n"
            summary += f"- Example ending: `{' '.join(tokens[-5:])}`\n"
        else:
            summary += "- No token output captured.\n"

        return summary

    except Exception as e:
        return f"[Error summarizing log: {str(e)}]"

