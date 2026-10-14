CAP_X, CAP_Y = 4, 3
GOAL = 2
def get_successors(state):
    x,y = state
    successors = []
    successors.append((CAP_X,y))
    successors.append((x,CAP_Y))
    successors.append((0,y))
    successors.append((x,0))

    pour = min(x, CAP_Y-y)
    successors.append((x - pour,y + pour))

    pour2 = min(y, CAP_X - x)
    successors.append((x + pour2, y - pour2))

    return successors

def dfs(start):
    stack = [(start, [])]
    visited = set([start])

    while stack:
        state, path = stack.pop()
        if state[0] == GOAL or state[1] == GOAL:
            return path + [state]

        for new_state in get_successors(state):
            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [state]))
    return None

start = (0,0)
solution = dfs(start)
if solution:
    print("solution found in",len(solution) -1,"moves:\n")
    for step in solution:
        print(f"Jug X: {step[0]}L Jug Y: {step[1]}L")
else:
    print("No solution found")
