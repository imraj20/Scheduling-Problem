 The thought process behind the nurse scheduling code:

1. Understanding the Problem:
   The problem is to create a weekly schedule for a hospital's nursing staff. The schedule must meet staffing requirements for different shifts, consider nurse availability, work hour limits, and skill levels. There are constraints regarding the minimum and maximum number of nurses per shift, maximum workdays per week, and the need for specific skill levels in each shift.

2. Choosing a Solver:
   The code uses Google's OR-Tools library, specifically the CP-SAT (Constraint Programming - Simple and Fast) solver. This type of solver is suitable for problems with constraints and binary decision variables.

3. Modeling the Problem:
   - Decision Variables:
     The code defines binary decision variables for each nurse, day, and shift type. These variables represent whether a nurse is assigned to a particular shift on a specific day.

   - Constraints:
     - Each nurse works at most 5 days a week.
     - There is a minimum number of nurses required for each shift on each day.
     - At least one nurse of Competent or Expert level is required for each shift.
     - A nurse must have at least 48 hours off after a night shift.

4. Creating the Solver and Solving the Model:
   - The code initializes the CP-SAT solver and attempts to find an optimal solution to the defined problem.

5. Outputting the Schedule:
   - If an optimal solution is found, the code prints the nurse assignments for each day and shift type.

6. Note on Constraints:
   - The constraints are formulated based on the problem requirements, ensuring a fair and efficient schedule while adhering to staffing rules and nurse preferences.

7. Adaptation for Specifics:
   - The code is a template and needs adaptation based on specific details such as the number of nurses, skill levels, and actual nurse availability data.

8. Testing and Refinement:
   - After running the code, the schedule output can be reviewed to ensure it meets the requirements. If necessary, constraints or model parameters can be adjusted for better results.

9. Handling Output:
   - The schedule output can be used for communication with the nursing staff or integrated into a larger system for managing hospital schedules.

Overall, the thought process involves understanding the problem, formulating it as a constraint satisfaction problem, implementing the model using a solver, and interpreting the results to generate a feasible and optimized nurse schedule.


















OUTPUT:

![image](https://github.com/imraj20/Scheduling-Problem/assets/67505003/426878aa-c62c-401d-884c-ce20b1fb6fbe)
