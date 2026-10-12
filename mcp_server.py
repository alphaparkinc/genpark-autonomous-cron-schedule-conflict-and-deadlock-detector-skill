"""MCP server for Autonomous Cron Schedule Conflict & Deadlock Detector."""
import sys
import json
from client import CronScheduleConflictDetector

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "detect_cron_schedule_conflicts",
                "description": "Detects overlapping time windows and resource lock contention across scheduled jobs",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "jobs": {"type": "array"}
                    },
                    "required": ["jobs"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "detect_cron_schedule_conflicts":
            jobs = params.get("arguments", {}).get("jobs", [])
            res = CronScheduleConflictDetector.detect_schedule_conflicts(jobs)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
