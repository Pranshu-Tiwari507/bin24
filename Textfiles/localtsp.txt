import math, random

cities = [(0, 0), (2, 6), (5, 2), (6, 6), (8, 3), (3, 4)]

def length(tour):
    return sum(math.dist(cities[tour[i]], cities[tour[i - 1]]) for i in range(len(tour)))

def neighbors(tour):
    result = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            t = tour[:]
            t[i], t[j] = t[j], t[i]
            result.append(t)
    return result

k = 3
beam = []
for _ in range(k):
    t = list(range(len(cities)))
    random.shuffle(t)
    beam.append(t)

best = min(beam, key=length)
while True:
    pool = [n for tour in beam for n in neighbors(tour)]
    beam = sorted(pool, key=length)[:k]
    if length(beam[0]) < length(best):
        best = beam[0]
        print("Improved:", best, round(length(best), 2))
    else:
        break

print("Best tour:", best, "Length:", round(length(best), 2))



# import math
# import random
# def tour_length(tour, pts):
#     return sum(math.dist(pts[tour[i]], pts[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))
# def successors(tour):
#     n = len(tour)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             t = tour[:]
#             t[i], t[j] = t[j], t[i]
#             yield t
# def local_beam_search(pts, k=5, max_iters=500, seed=None):
#     rng = random.Random(seed)
#     n = len(pts)
#     beam = []
#     for _ in range(k):
#         t = list(range(n))
#         rng.shuffle(t)
#         beam.append(t)
#     best = min(beam, key=lambda t: tour_length(t, pts))
#     best_len = tour_length(best, pts)
#     history = [best_len]
#     for _ in range(max_iters):
#         pool = {tuple(s) for t in beam for s in successors(t)}
#         if not pool:
#             break
#         ranked = sorted(pool, key=lambda t: tour_length(t, pts))[:k]
#         beam = [list(t) for t in ranked]
#         cand_len = tour_length(beam[0], pts)
#         if cand_len < best_len - 1e-9:
#             best, best_len = beam[0][:], cand_len
#             history.append(best_len)
#         else:
#             break
#     return best, best_len, history
# if __name__ == "__main__":
#     rng = random.Random(42)
#     n = 12
#     cities = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(n)]
#     print("Cities:")
#     for i, c in enumerate(cities):
#         print(f"  {i}: ({c[0]:.1f}, {c[1]:.1f})")
#     for k in (1, 3, 10):
#         tour, length, hist = local_beam_search(cities, k=k, seed=1)
#         print(f"\nBeam width k={k}: length={length:.2f}, iterations={len(hist) - 1}")
#         print("Tour:", " -> ".join(map(str, tour + [tour[0]])))