
# Directory Structure for this Project

```bash
LLD-Lab/
├── api/                        # FastAPI endpoints exposed to Custom GPT
│   ├── main.py                 # FastAPI app definition
│   └── routes/
│       ├── run.py              # POST /run - start experiment
│       ├── log.py              # GET /log - view logs
│       └── visualize.py        # GET /visualize - show plots
├── core/                       # Core logic for models
│   ├── lldm_runner.py          # Runs either LLaDA or Dream
│   ├── llada/                  # LLaDA source code (hooked)
│   └── dream7b/                # Dream 7B source code (hooked)
├── utils/
│   ├── config.py               # Reads server configs, model paths
│   ├── logging.py              # Structured logging
│   └── plotting.py             # Entropy, saliency, token maps
├── scripts/
│   └── run_dev.py              # Dev-only CLI for testing
├── data/
│   └── logs/                   # Saved logs, entropy maps, etc.
├── openai.yaml                 # Action schema for GPT interface
├── requirements.txt
├── README.md
└── .env                        # (Optional) Store environment configs
```
