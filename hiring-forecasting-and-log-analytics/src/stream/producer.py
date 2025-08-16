"""Simulate log production by appending to JSONL batches."""
import json
import time
import uuid
from datetime import datetime
from pathlib import Path
from src.common.config import STREAM_DIR

def produce(n=5, req_id="R-100"):
    Path(STREAM_DIR).mkdir(parents=True, exist_ok=True)
    fname = Path(STREAM_DIR) / f"batch_{int(time.time())}.jsonl"
    with open(fname, "w", encoding="utf-8") as f:
        for _ in range(n):
            rec = {
                "ts": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "candidate_id": f"C-{uuid.uuid4().hex[:6]}",
                "event": "apply",
                "req_id": req_id,
            }
            f.write(json.dumps(rec) + "\n")
    print("wrote", fname)

if __name__ == "__main__":
    produce()
