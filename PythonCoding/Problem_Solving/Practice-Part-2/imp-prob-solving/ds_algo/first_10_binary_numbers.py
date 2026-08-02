"""
1
10
11
100
101
110
111
1000
1001
1010
"""

from collections import deque

def generate_binary_numbers(n):
    queue = deque()
    queue.append("1")

    for _ in range(n):
        front = queue.popleft()
        print(front)

        queue.append(front + "0")
        queue.append(front + "1")

generate_binary_numbers(10)
