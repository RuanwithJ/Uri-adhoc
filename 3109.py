def swap(position, A, B):
    aux = position[A]
    position[A] = position[B]
    position[B] = aux
nEmployees = int(input())
employees = []
position = []
for i in range(nEmployees):
    employees.append(i)
    position.append(i)
nEvents = int(input())
for i in range(nEvents):
    event = input().split()
    if(event[0]=="1"):
        A = int(event[1])-1
        B = int(event[2])-1
        Ap = employees[A]
        Bp = employees[B]
        swap(position, Ap,Bp)
        swap(employees, position[Ap], position[Bp])
    else:
        swaps = 0
        p = position[int(event[1]) -1]
        search = position[int(event[1]) -1]
        while(True):
            if(search==position[p]):
                break
            swaps+=1
            p = position[p]
        print(swaps)