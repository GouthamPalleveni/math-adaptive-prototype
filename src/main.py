from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import adjust_difficulty
import time

def main():
    name = input("Enter your name: ")
    level = input("Choose difficulty (Easy/Medium/Hard): ").title()
    tracker = PerformanceTracker()

    for _ in range(5):
        question, answer = generate_puzzle(level)
        print(f"\nSolve: {question}")
        start = time.time()
        user_answer = input("Your answer: ")
        end = time.time()

        correct = str(answer) == user_answer
        tracker.log(correct, end - start)

        print("✅ Correct!" if correct else f"❌ Incorrect! Correct answer: {answer}")
        level = adjust_difficulty(tracker.records, level)
        print(f"➡ Next Level: {level}")

    print("\n--- Session Summary ---")
    print(tracker.summary())

if __name__ == "__main__":
    main()
