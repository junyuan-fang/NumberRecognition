from heapq import heappop, heappush,_heapify_max
heap = [1,5,3,4,5]
heappush(heap, 1)
_heapify_max(heap)
heappush(heap,4)
print(heap)

heap2 = [(40,None) for _ in range(3)]
heap2[0] = (20,2)
results = []
for item in heap2:
    results.append(item[1])
sets = set(results)
print(set(results))
p = max(set(results), key=results.count)
print(p)
# visited = [[False for j in range(28)] for i in range(28)]
# min_y = 15
# max_y = min_y
# min_x = 15
# max_x = min_x
# found = False
# while not found:
#     for row_index in range(min_x,max_x+1):
#         #up
#         visited[min_y][row_index] = True
#         #down
#         visited[max_y][row_index] = True

#     for colum_index in range(min_y, max_y+1):
#         #left 
#         visited[colum_index][min_x] = True
#         #right
#         visited[colum_index][max_x] = True
#     if (min_y == 0 and max_y == 27 and min_x == 0 and max_x == 27):
#         break
#     if not found:
#         if min_y > 0:
#             min_y -= 1
#         if max_y < 27:
#             max_y += 1
#         if min_x > 0:
#             min_x -= 1
#         if max_x < 27:
#             max_x += 1

# print(visited)

# print(visited[:2])