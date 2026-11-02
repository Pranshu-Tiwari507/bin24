def toh(n, source, auxiliary, destination):
    if n == 0:
        return
    toh(n - 1, source, destination, auxiliary)
    print(f"Move Disk {n} from {source} to {destination}")
    toh(n - 1, auxiliary, source, destination)
n = int(input("Enter number of disks: "))
if n < 1:
    print("Enter at least 1 disk.")
else:
    disks = list(range(1, n + 1))
    print("\nInitial Condition:")
    print("Rod A:", disks)
    print("Rod B: Empty")
    print("Rod C: Empty")
    print("\nMoves:")
    toh(n, 'A', 'B', 'C')
    print("\nFinal Condition:")
    print("Rod A: Empty")
    print("Rod B: Empty")
    print("Rod C:", disks)
    print(f"\nTotal moves: {2 ** n - 1}")

# """Tower of Hanoi by state-space search (BFS gives the shortest solution).

# State : tuple of 3 pegs (A, B, C). Each peg is a tuple of disks, bottom to top.
#         Example: ((3, 2), (1,), ()) -> A has disks 3,2 ; B has disk 1 ; C empty.
# """
# from collections import deque


# def solve(n):
#     start = (tuple(range(n, 0, -1)), (), ())     # all disks on A
#     goal = ((), (), tuple(range(n, 0, -1)))      # all disks on C

#     parent = {start: None}                       # also acts as the visited set
#     queue = deque([start])

#     while queue:
#         state = queue.popleft()
#         if state == goal:
#             break
#         for src in range(3):
#             for dst in range(3):
#                 # legal: src has a disk, and dst is empty or has a bigger top disk
#                 if src != dst and state[src] and (not state[dst] or state[src][-1] < state[dst][-1]):
#                     disk = state[src][-1]
#                     new = list(state)
#                     new[src] = state[src][:-1]       # remove top disk
#                     new[dst] = state[dst] + (disk,)  # place it on dst
#                     new = tuple(new)
#                     if new not in parent:
#                         parent[new] = (state, f"Move disk {disk} from {'ABC'[src]} to {'ABC'[dst]}")
#                         queue.append(new)

#     # walk back from the goal to rebuild the path
#     steps, state = [], goal
#     while parent[state]:
#         prev, move = parent[state]
#         steps.append((move, state))
#         state = prev
#     return steps[::-1]


# if __name__ == "__main__":
#     n = 3
#     steps = solve(n)
#     print("Start:", ((tuple(range(n, 0, -1))), (), ()))
#     for i, (move, state) in enumerate(steps, 1):
#         print(f"{i:>2}. {move:<22} A,B,C = {state}")
#     print(f"\nTotal moves: {len(steps)}  (2^{n} - 1 = {2 ** n - 1})")