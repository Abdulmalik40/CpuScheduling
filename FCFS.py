def fcfs_scheduling():
    # 1- Iterate the input values for the list
    # 2.0 Iterate the waiting time 
    # 2.1 The waiting time is the previous waiting time + the previous burst time
    # 3.0 Calculate the troundaround time = burst time + waiting time + Itertae all values

    # 1- Collect the Values ties
    # FCFS
    n = int(input("Enter the number of processes: "))
    burst_times = []

    for i in range(n):
        bt = int(input(f"Enter Burst time for Process {i+1}: "))
        burst_times.append(bt)

    # 2- intialise the waiting time then calculate for values after the first one
    waiting_times = [0] * n 
    # 2.1- Start from index 1 , not 0
    for i in range(1, n):
        waiting_times[i] = waiting_times[i-1] + burst_times[i-1]

    # 3 - Calculate turnaround times = burst time + waiting time
    turnaround_times = [burst_times[i] + waiting_times[i] for i in range(n)]

    avg_waiting = sum(waiting_times) / n
    avg_turnaround = sum(turnaround_times) / n

    print("\nProcess\tBurst Time\tWaiting Time\tTurnAround Time")
    for i in range(n): # Iterate through the values of the list
        print(f"P{i+1}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

    print(f"\nAverage Waiting Time-- {avg_waiting:.2f}")
    print(f"Average TurnAround Time-- {avg_turnaround:.2f}")

    return {
        "burst_times": burst_times,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround
    }
