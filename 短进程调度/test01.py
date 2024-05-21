import random

class PCB:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.finish_time = 0

    def __repr__(self):
        return f'PCB(pid={self.pid}, arrival={self.arrival_time}, burst={self.burst_time}, priority={self.priority})'


def generate_processes(n):
    processes = []
    for i in range(n):
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        priority = random.randint(1, 5)
        processes.append(PCB(i, arrival_time, burst_time, priority))
    return processes

# 生成10个随机进程
processes = generate_processes(10)
for process in processes:
    print(process)
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    completed_processes = 0
    n = len(processes)

    while completed_processes < n:
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p.finish_time == 0]
        if not ready_queue:
            current_time += 1
            continue

        ready_queue.sort(key=lambda x: x.burst_time)
        current_process = ready_queue[0]
        current_time += current_process.burst_time
        current_process.finish_time = current_time
        current_process.turnaround_time = current_process.finish_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        completed_processes += 1

    return processes

# 调用SJF算法
sjf_processes = sjf_scheduling(processes.copy())
for process in sjf_processes:
    print(f'PID: {process.pid}, Finish Time: {process.finish_time}, Turnaround Time: {process.turnaround_time}, Waiting Time: {process.waiting_time}')
def rr_scheduling(processes, time_quantum):
    queue = []
    current_time = 0
    for p in sorted(processes, key=lambda x: x.arrival_time):
        queue.append(p)

    while queue:
        current_process = queue.pop(0)
        if current_process.remaining_time > time_quantum:
            current_time += time_quantum
            current_process.remaining_time -= time_quantum
            queue.append(current_process)
        else:
            current_time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.finish_time = current_time
            current_process.turnaround_time = current_process.finish_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time

    return processes

# 调用RR算法
time_quantum = 2
rr_processes = rr_scheduling(processes.copy(), time_quantum)
for process in rr_processes:
    print(f'PID: {process.pid}, Finish Time: {process.finish_time}, Turnaround Time: {process.turnaround_time}, Waiting Time: {process.waiting_time}')


def hrrn_scheduling(processes):
    current_time = 0
    completed_processes = 0
    n = len(processes)

    while completed_processes < n:
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p.finish_time == 0]
        if not ready_queue:
            current_time += 1
            continue

        for process in ready_queue:
            process.response_ratio = ((current_time - process.arrival_time) + process.burst_time) / process.burst_time
        ready_queue.sort(key=lambda x: x.response_ratio, reverse=True)

        current_process = ready_queue[0]
        current_time += current_process.burst_time
        current_process.finish_time = current_time
        current_process.turnaround_time = current_process.finish_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        completed_processes += 1

    return processes


# 调用HRRN算法
hrrn_processes = hrrn_scheduling(processes.copy())
for process in hrrn_processes:
    print(
        f'PID: {process.pid}, Finish Time: {process.finish_time}, Turnaround Time: {process.turnaround_time}, Waiting Time: {process.waiting_time}')
def calculate_average_turnaround_time(processes):
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    return total_turnaround_time / len(processes)

# 计算并比较平均周转时间
sjf_avg_turnaround = calculate_average_turnaround_time(sjf_processes)
rr_avg_turnaround = calculate_average_turnaround_time(rr_processes)
hrrn_avg_turnaround = calculate_average_turnaround_time(hrrn_processes)

print(f'SJF Average Turnaround Time: {sjf_avg_turnaround}')
print(f'RR Average Turnaround Time: {rr_avg_turnaround}')
print(f'HRRN Average Turnaround Time: {hrrn_avg_turnaround}')
