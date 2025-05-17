def fcfs_scheduling():
    # 1- Iterate the input values for the list
    # 2.0 Iterate the waiting time
    # 2.1 The waiting time is the previous waiting time + the previous burst time
    # 3.0 Calculate the troundaround time = burst time + waiting time + Itertae all values

    # 1- Collect the Values ties
    # FCFS
    try:
        n = int(input("Enter the number of processes: "))
        if n <= 0:
            print("Number of processes must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    processes = []
    # Collect Arrival and Burst Times
    for i in range(n):
        try:
            at = int(input(f"Enter Arrival Time for P{i + 1}: "))
            bt = int(input(f"Enter Burst Time for P{i + 1}: "))
            if at < 0 or bt <= 0:
                print("Arrival time must be ≥ 0 and Burst time must be > 0.")
                return
            processes.append((i + 1, at, bt))  # (Process ID, Arrival Time, Burst Time)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

    # Sort by Arrival Time
    processes.sort(key=lambda x: x[1])

    waiting_times = [0] * n
    turnaround_times = [0] * n
    start_time = 0

    for i in range(n):
        pid, at, bt = processes[i]
        if start_time < at:
            start_time = at  # Wait until the process arrives
        waiting_times[i] = start_time - at
        turnaround_times[i] = waiting_times[i] + bt
        start_time += bt

    avg_waiting = sum(waiting_times) / n
    avg_turnaround = sum(turnaround_times) / n

    print("\n{:<10} {:<10} {:<10} {:<15} {:<15}".format("Process", "Arrival", "Burst", "Waiting", "Turnaround"))
    for i in range(n):
        pid, at, bt = processes[i]
        print("{:<10} {:<10} {:<10} {:<15} {:<15}".format(f"P{pid}", at, bt, waiting_times[i], turnaround_times[i]))

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")

    return {
        "processes": processes,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround
    }


def priority_scheduling():
    # 1- Iterate the input values for the list
    # 2 - Grouping the values in tuple
    # 3 - Sort it by the priority
    # 4 - Iterate to Caulculate the waiting time and waiting time

    # Priority
    # 1- Iterate the input
    try:
        n = int(input("Enter the number of Process: "))
        if n <= 0:
            print("Number of processes must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    burst_times = []
    priorities = []

    for i in range(n):
        try:
            bt = int(input(f"Enter burst time for process p{i + 1}: "))
            priority = int(input(f"Enter priority for process p{i + 1}: "))
            if bt <= 0:
                print("Burst time must be > 0.")
                return
            burst_times.append(bt)
            priorities.append(priority)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

    # 2- Grouping index with burst time and priorty in tuple
    processes = [(i, bt, prio) for i, (bt, prio) in enumerate(zip(burst_times, priorities))]

    # 3- Sort by the priority , 0 is the index and 2 is the priority
    processes.sort(key=lambda x: (x[2], x[0]))

    waiting_times = [0] * n
    current_time = 0
    # 4- Iterate for calculation
    for proc in processes:
        original_idx, bt, _ = proc  # (_) ignore the third value in tuple because we know the order now
        waiting_times[original_idx] = current_time
        current_time += bt

    turnaround_times = [waiting_times[i] + burst_times[i] for i in range(n)]

    avg_wt = sum(waiting_times) / n
    avg_tat = sum(turnaround_times) / n

    print("\n{:<10} {:<10} {:<10} {:<15} {:<15}".format("Process", "Burst", "Priority", "Waiting", "Turnaround"))
    for i in range(n):
        print("{:<10} {:<10} {:<10} {:<15} {:<15}".format(
            f"P{i + 1}", burst_times[i], priorities[i], waiting_times[i], turnaround_times[i]
        ))

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    return {
        "burst_times": burst_times,
        "priorities": priorities,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "avg_waiting": avg_wt,
        "avg_turnaround": avg_tat
    }

def round_robin_scheduling():
    # 1- Iterate the input values for the list
    # 2- Iterate the waiting time
    # 3- make a copy of the burst time
    # 4- if the remaining burst time total time will add the quantum time
    # 5- the other case is if it is lower or equal then add then remaining time
    # 6- calculate the waiting time and turnaround time

    # Round Robin
    try:
        n = int(input("Enter the number of Process: "))
        if n <= 0:
            print("Number of processes must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    burst_times = []

    for i in range(n):
        try:
            bt = int(input(f"Enter the burst time of process p{i + 1}: "))
            if bt <= 0:
                print("Burst time must be > 0.")
                return
            burst_times.append(bt)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

    try:
        quantum = int(input("Enter the time quantum: "))
        if quantum <= 0:
            print("Time quantum must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer for time quantum.")
        return

    # Tracking remaining burst time
    remaining_bt = burst_times.copy()
    turnaround_time = [0] * n  # Store the completion time
    total_time = 0
    context_switches = 0  # Initialize context switch counter

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:  # Check if the process has remaining burst time
                done = False
                if remaining_bt[i] > quantum:
                    total_time += quantum  # For example, 24 > 4, the total time will be 4
                    remaining_bt[i] -= quantum  # Remaining burst time will be 20
                    context_switches += 1  # Increment counter when quantum expires
                else:
                    total_time += remaining_bt[i]  # Add the remaining bt to the total time
                    turnaround_time[i] = total_time
                    remaining_bt[i] = 0  # There is no remaining burst time
                    # Only count as context switch if there are more processes to execute
                    if not all(bt == 0 for bt in remaining_bt):
                        context_switches += 1
        if done:
            break

    waiting_time = [turnaround_time[i] - burst_times[i] for i in range(n)]
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("\n{:<10} {:<10} {:<15} {:<15}".format("Process", "Burst", "Turnaround", "Waiting"))
    for i in range(n):
        print("{:<10} {:<10} {:<15} {:<15}".format(
            f"P{i + 1}", burst_times[i], turnaround_time[i], waiting_time[i]
        ))

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Total Context Switches: {context_switches}")

    return {
        "burst_times": burst_times,
        "waiting_times": waiting_time,
        "turnaround_times": turnaround_time,
        "quantum": quantum,
        "avg_waiting": avg_wt,
        "avg_turnaround": avg_tat,
        "context_switches": context_switches
    }

def sjf_non_preemptive():
    # 1- Collect the Values
    # 2- Sort the values by arrival time
    # 3- Varible for count processes finished , and for track , varible to check if  it is completed
    # 4- Collect values arrived but not finished
    # 5- choose the short process from the ready queue
    # 6- Extract the id and arrival and burst time

    try:
        n = int(input("Enter the Number of Processes: "))
        if n <= 0:
            print("Number of processes must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    processes = []

    # 1- Input arrival and burst times
    for i in range(n):
        try:
            at = int(input(f"Enter Arrival Time for P{i}: "))
            bt = int(input(f"Enter Burst Time for P{i}: "))
            if at < 0 or bt <= 0:
                print("Arrival time must be ≥ 0 and Burst time must be > 0.")
                return
            processes.append((i, at, bt))  # (ID, arrival, burst)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

    # 2- sort the processes
    processes.sort(key=lambda x: x[1])

    # 3- Variables to track and check
    completed = 0
    current_time = 0
    waiting_times = [0] * n
    turnaround_times = [0] * n
    is_completed = [False] * n

    # 4- Collect values are ready
    while completed < n:
        # Find all processes that have arrived and are not completed
        ready_queue = [proc for proc in processes if proc[1] <= current_time and not is_completed[proc[0]]]

        if not ready_queue:
            current_time += 1
            continue

        # 5- Select and extract the process with the shortest burst time
        shortest_proc = min(ready_queue, key=lambda x: x[2])
        pid, at, bt = shortest_proc

        # Calculations
        waiting_times[pid] = current_time - at
        turnaround_times[pid] = waiting_times[pid] + bt
        current_time += bt
        is_completed[pid] = True
        completed += 1

    avg_waiting = sum(waiting_times) / n
    avg_turnaround = sum(turnaround_times) / n

    print("\n{:<10} {:<15} {:<15} {:<15} {:<15}".format("Process", "Arrival", "Burst", "Waiting", "Turnaround"))
    for pid, at, bt in sorted(processes, key=lambda x: x[0]):
        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(f"P{pid}", at, bt, waiting_times[pid], turnaround_times[pid]))

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")

    return {
        "arrival_times": [at for _, at, _ in processes],
        "burst_times": [bt for _, _, bt in processes],
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround
    }


def sjf_preemptive():
    # 1- iterate the values
    # 2-  Store in dictionary the process and arrival time with burst time and remaining burst time
    # 3- varibles for tracking , time , complete process , start for track time , finsh to mark
    # 4- store in the list the process have arrived and still have time
    # 5- take the shortest process from the list
    # 6- the process hasn't started record the start time
    # 7- then mark the process and calculate
    try:
        n = int(input("Enter the number of processes: "))
        if n <= 0:
            print("Number of processes must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    processes = []

    for i in range(n):
        try:
            at = int(input(f"Enter arrival time for P{i}: "))
            bt = int(input(f"Enter burst time for P{i}: "))
            if at < 0 or bt <= 0:
                print("Arrival time must be ≥ 0 and Burst time must be > 0.")
                return
            # 2-  Store in dictionary the process and arrival time with burst time and remaining burst time
            processes.append({'pid': i, 'arrival': at, 'burst': bt, 'remaining': bt})
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

    time = 0
    complete = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    start_times = [-1] * n
    finished = [False] * n

    while complete < n:
        # Get ready processes
        ready = [p for p in processes if p['arrival'] <= time and p['remaining'] > 0]

        if ready:
            # Choose process with shortest remaining time
            current = min(ready, key=lambda p: p['remaining'])
            pid = current['pid']

            if start_times[pid] == -1:
                start_times[pid] = time

            # Run for 1 time unit
            current['remaining'] -= 1
            time += 1

            # If process is finished
            if current['remaining'] == 0:
                complete += 1
                turnaround_time[pid] = time - current['arrival']
                waiting_time[pid] = turnaround_time[pid] - current['burst']
                finished[pid] = True
        else:
            time += 1  # idle

    # Print results manually (without pandas)
    print("\n{:<10} {:<15} {:<15} {:<15} {:<15}".format("Process", "Arrival", "Burst", "Waiting", "Turnaround"))
    for i in range(n):
        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
            f"P{i}", processes[i]['arrival'], processes[i]['burst'], waiting_time[i], turnaround_time[i]
        ))

    print(f"\nAverage Waiting Time: {sum(waiting_time) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time) / n:.2f}")

    return {
        "arrival_times": [p['arrival'] for p in processes],
        "burst_times": [p['burst'] for p in processes],
        "waiting_times": waiting_time,
        "turnaround_times": turnaround_time,
        "avg_waiting": sum(waiting_time) / n,
        "avg_turnaround": sum(turnaround_time) / n
    }
