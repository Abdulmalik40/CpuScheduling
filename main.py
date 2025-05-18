# Abdulmalik : Round Robin , SJFS Non , SJFS Prem , Steps of Algorthim
# Amrou      : FCFS , Priorty , Recompsion code , Main file
import time
import sys
from Algorthims import (
fcfs_scheduling,
sjf_non_preemptive,
sjf_preemptive,
priority_scheduling,
round_robin_scheduling)
def main():
    while True:
        print("\n" + "=" * 50)
        print("         CPU Scheduling Algorithms Menu")
        print("=" * 50)
        print(" 1. First-Come, First-Served (FCFS)")
        print(" 2. Shortest Job First (Non-Preemptive)")
        print(" 3. Shortest Job First (Preemptive)")
        print(" 4. Priority Scheduling")
        print(" 5. Round Robin Scheduling")
        print(" 6. Exit")
        print("=" * 50)

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print(" Invalid input! Please enter a number between 1 and 6.")
            continue

        print("\n" + "-" * 50)

        if choice == 1:
            fcfs_scheduling()
        elif choice == 2:
            sjf_non_preemptive()
        elif choice == 3:
            sjf_preemptive()
        elif choice == 4:
            priority_scheduling()
        elif choice == 5:
            round_robin_scheduling()
        elif choice == 6:
            print("Exiting the program", end="", flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print(" Goodbye!")

            break
        else:
            print("Invalid choice Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
