# Question 3

import threading
import time
import random


def generateRandomNumbers():
    return [random.randint(0, 10000) for _ in range(100)]

def threadTask(name, results):
    result = generateRandomNumbers()
    results[name] = result

def multithreadingTest():
    total_time = 0
    print("\nMultithreading Execution")
    for round_num in range(1, 11):
        results = {}
        threads = []
        start_time = time.time_ns()

        for i in range(3):
            t = threading.Thread(target=threadTask, args=(f"Set-{i+1}", results))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        end_time = time.time_ns()
        T = end_time - start_time
        total_time += T
        print(f"Round {round_num}: T = {T} nanoseconds")

    avg_time = total_time // 10
    print(f"\nTotal Time over 10 rounds: {total_time} ns")
    print(f"Average Time: {avg_time} ns")

def sequentialTest():
    total_time = 0
    print("\nSequential Execution")
    for round_num in range(1, 11):
        start_time = time.time_ns()
        results = {}
        for i in range(3):
            results[f"Set-{i+1}"] = generateRandomNumbers()
        end_time = time.time_ns()
        T = end_time - start_time
        total_time += T
        print(f"Round {round_num}: T = {T} nanoseconds")

    avg_time = total_time // 10
    print(f"\nTotal Time over 10 rounds: {total_time} ns")
    print(f"Average Time: {avg_time} ns")


if __name__ == "__main__":
    multithreadingTest()
    sequentialTest()
