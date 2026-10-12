"""Autonomous Cron Schedule Conflict & Deadlock Detector.
100% Python Standard Library.
"""

class CronScheduleConflictDetector:
    """Detects overlapping execution windows and resource lock contention across scheduled autonomous agent jobs."""

    @staticmethod
    def detect_schedule_conflicts(jobs: list) -> dict:
        conflicts = []
        for i in range(len(jobs)):
            for j in range(i + 1, len(jobs)):
                a = jobs[i]
                b = jobs[j]
                if a.get("resource_lock") and a.get("resource_lock") == b.get("resource_lock"):
                    overlap = not (a["end_minute"] <= b["start_minute"] or b["end_minute"] <= a["start_minute"])
                    if overlap:
                        conflicts.append({
                            "job_a": a["name"],
                            "job_b": b["name"],
                            "contended_resource": a["resource_lock"]
                        })

        return {
            "jobs_analyzed": len(jobs),
            "conflict_free": len(conflicts) == 0,
            "conflicts_count": len(conflicts),
            "conflicts": conflicts
        }
