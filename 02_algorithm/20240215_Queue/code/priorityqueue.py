from queue import PriorityQueue

q = PriorityQueue()


# 튜플로 입력
# 오름차순 기준으로(낮은 수 먼저) 정렬
q.put((45, 'z'))
q.put((17, 'x'))
print(q.queue)