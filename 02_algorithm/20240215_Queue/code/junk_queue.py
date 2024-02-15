N = 10
q = [0] * N
front = rear = -1

rear += 1
q[rear] = 10

rear += 1
q[rear] = 20

rear += 1
q[rear] = 30

while front != rear:
    front += 1
    print(q[front])