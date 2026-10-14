#5. Write a program to solve Tower of Hanoi problem

def tower_of_hanoi(n,source,auxiliary,destination):
    if n == 1:
        print("move disk 1 from",source,"to",destination)
        return


    tower_of_hanoi(n-1,source,destination,auxiliary)
    print("move disk",n,"from",source,"to",destination)
    

    tower_of_hanoi(n-1,auxiliary,source,destination)

n = int(input("enter number of disks :"))

tower_of_hanoi(n,'A','B','C')
