"""
This script demonstrates logical operators by combining the comparison
results from the previous example to make a final decision.

Operators demonstrated:
- `and`: True only if ALL conditions are true.
- `or`: True if AT LEAST ONE condition is true.
- `not`: Inverts a boolean value.

It also showcases short-circuiting behavior.
"""

# --- Variables ---
student_gpa = 3.8
student_absences = 2
student_grade_level = "Grade 12"

# && || 
# and or sql language

is_eligible = (student_gpa >= 3.5) and (student_absences < 5) and (student_grade_level == "Grade 12")

print(f"Is the student eligible for the honor roll? {is_eligible}")