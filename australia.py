from itertools import product

states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

colors = ['Red', 'Green', 'Blue']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_valid(assignment):
    for state in assignment:
        for neighbor in neighbors[state]:
            if neighbor in assignment and assignment[state] == assignment[neighbor]:
                return False
    return True

def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment
    
    unassigned = [s for s in states if s not in assignment][0]
    
    for color in colors:
        assignment[unassigned] = color
        if is_valid(assignment):
            result = backtrack(assignment)
            if result:
                return result
        del assignment[unassigned]
    
    return None

solution = backtrack({})
print("Australia Map Coloring Solution:")
print(solution)