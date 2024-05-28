import random

# 定义进程数量和资源数量
NUM_PROCESSES = 5
NUM_RESOURCES = 3

# 初始化系统的总资源
total_resources = [10, 15, 12]

# 随机生成每个进程的最大需求
max_demand = [[random.randint(0, total_resources[j]) for j in range(NUM_RESOURCES)] for i in range(NUM_PROCESSES)]

# 初始化分配的资源为0
allocation = [[0 for j in range(NUM_RESOURCES)] for i in range(NUM_PROCESSES)]

# 计算需要的资源
need = [[max_demand[i][j] - allocation[i][j] for j in range(NUM_RESOURCES)] for i in range(NUM_PROCESSES)]

# 初始化可用资源
available = [total_resources[j] - sum(allocation[i][j] for i in range(NUM_PROCESSES)) for j in range(NUM_RESOURCES)]

# 输出进程信息
def print_status():
    print("进程\t最大需求\t已分配\t需要\t可用")
    for i in range(NUM_PROCESSES):
        print(f"P{i}\t{max_demand[i]}\t{allocation[i]}\t{need[i]}")
    print(f"Available: {available}\n")

# 安全性检查
def is_safe():
    work = available[:]
    finish = [False] * NUM_PROCESSES
    while True:
        found = False
        for i in range(NUM_PROCESSES):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(NUM_RESOURCES)):
                for j in range(NUM_RESOURCES):
                    work[j] += allocation[i][j]
                finish[i] = True
                found = True
        if not found:
            break
    return all(finish)

# 资源请求
def request_resources(process, request):
    if all(request[j] <= need[process][j] for j in range(NUM_RESOURCES)):
        if all(request[j] <= available[j] for j in range(NUM_RESOURCES)):
            for j in range(NUM_RESOURCES):
                available[j] -= request[j]
                allocation[process][j] += request[j]
                need[process][j] -= request[j]
            if is_safe():
                print(f"进程P{process}请求成功: {request}")
                return True
            else:
                for j in range(NUM_RESOURCES):
                    available[j] += request[j]
                    allocation[process][j] -= request[j]
                    need[process][j] += request[j]
                print(f"进程P{process}请求失败（导致不安全状态）: {request}")
                return False
        else:
            print(f"进程P{process}请求失败（资源不足）: {request}")
            return False
    else:
        print(f"进程P{process}请求失败（超过最大需求）: {request}")
        return False

# 模拟进程运行和资源请求
def run_simulation():
    print_status()
    for _ in range(10):
        process = random.randint(0, NUM_PROCESSES - 1)
        request = [random.randint(0, need[process][j]) for j in range(NUM_RESOURCES)]
        request_resources(process, request)
        print_status()

# 运行模拟
run_simulation()
