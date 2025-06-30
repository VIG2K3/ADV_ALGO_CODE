# Question 1: Hashing
import random

def foldingHashing(ic_number, table_size):
    if len(ic_number) != 12 or not ic_number.isdigit():
        raise ValueError("IC number have to be a 12 digit number")

    parts = [int(ic_number[i:i + 4]) for i in range(0, 12, 4)]
    total = sum(parts)

    return total % table_size

def generateRandomIC():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

def insert_IN_Table(table_size, ic_list):
    hash_table = [[] for _ in range(table_size)]
    collisions = 0

    for ic in ic_list:
        index = foldingHashing(ic, table_size)
        if hash_table[index]:
            collisions += 1
        hash_table[index].append(ic)

    return collisions

def runProgram(rounds=10, num_ics=1000):
    table_sizes = [1009, 2003]
    avg_collisions = [0, 0]

    for size_index, size in enumerate(table_sizes):
        print(f"\nTable Size: {size}")
        for round_num in range(1, rounds + 1):
            ic_list = [generateRandomIC() for _ in range(num_ics)]
            collisions = insert_IN_Table(size, ic_list)
            avg_collisions[size_index] += collisions
            print(f"Round {round_num}: Collisions = {collisions}")

        avg = avg_collisions[size_index] / rounds
        print(f"Average Collisions, table size {size}: {avg}")

if __name__ == "__main__":
    runProgram()

