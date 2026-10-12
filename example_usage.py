"""Example usage for Autonomous Cron Schedule Conflict & Deadlock Detector."""
from client import CronScheduleConflictDetector

if __name__ == "__main__":
    jobs = [
        {"name": "nightly_index_sync", "start_minute": 10, "end_minute": 40, "resource_lock": "vector_db_primary"},
        {"name": "compact_embeddings", "start_minute": 30, "end_minute": 55, "resource_lock": "vector_db_primary"}
    ]
    res = CronScheduleConflictDetector.detect_schedule_conflicts(jobs)
    print("Conflicts:", res["conflicts"])
