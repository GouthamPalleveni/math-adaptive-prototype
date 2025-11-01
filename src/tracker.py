import time
class PerformanceTracker:
    def __init__(self):
        self.records = []

    def log(self, correct, response_time):
        self.records.append({"correct": correct, "time": response_time})

    def summary(self):
        total = len(self.records)
        correct = sum([1 for r in self.records if r["correct"]])
        accuracy = (correct / total) * 100 if total > 0 else 0
        avg_time = sum([r["time"] for r in self.records]) / total if total > 0 else 0

        return {
            "Total Questions": total,
            "Accuracy (%)": round(accuracy, 2),
            "Average Time (sec)": round(avg_time, 2)
        }
