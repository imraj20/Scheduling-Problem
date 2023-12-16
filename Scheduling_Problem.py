from ortools.sat.python import cp_model

def nurse_scheduling():
    
    model = cp_model.CpModel()

    
    num_nurses = 10  
    num_shifts = 7  
    num_shift_types = 3  

    
    shifts = {}
    for nurse in range(num_nurses):
        for day in range(num_shifts):
            for shift_type in range(num_shift_types):
                shifts[(nurse, day, shift_type)] = model.NewBoolVar(f'nurse_{nurse}_day_{day}_shift_{shift_type}')

    

    
    for nurse in range(num_nurses):
        model.Add(sum(shifts[(nurse, day, shift_type)] for day in range(num_shifts) for shift_type in range(num_shift_types)) <= 5)

    
    for day in range(num_shifts):
        model.Add(sum(shifts[(nurse, day, 0)] for nurse in range(num_nurses)) >= 3)  
        model.Add(sum(shifts[(nurse, day, 1)] for nurse in range(num_nurses)) >= 2)  
        model.Add(sum(shifts[(nurse, day, 2)] for nurse in range(num_nurses)) >= 2)  

    
    for day in range(num_shifts):
        for shift_type in range(num_shift_types):
            model.Add(
                sum(shifts[(nurse, day, shift_type)] for nurse in range(num_nurses)) >= 1
            )

    
    for nurse in range(num_nurses):
        for day in range(num_shifts - 2):  
            model.Add(shifts[(nurse, day, 2)] + shifts[(nurse, day + 1, 2)] + shifts[(nurse, day + 2, 2)] <= 1)

    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    
    if status == cp_model.OPTIMAL:
        for day in range(num_shifts):
            for nurse in range(num_nurses):
                for shift_type in range(num_shift_types):
                    if solver.Value(shifts[(nurse, day, shift_type)]) == 1:
                        print(f'Nurse {nurse} works on Day {day}, Shift {shift_type}')

if __name__ == '__main__':
    nurse_scheduling()
