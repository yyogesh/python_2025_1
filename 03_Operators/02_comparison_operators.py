"""
This script demonstrates advanced usage of comparison operators.
It checks if a student meets the criteria for the honor roll.

Operators demonstrated:
- Greater than or equal to (`>=`)
- Less than (`<`)
- Equal to (`==`)
- Chained comparison (`min < value < max`)

Scenario: To qualify for the honor roll, a student must have:
1. A GPA of 3.5 or higher.
2. Fewer than 5 absences.
3. Be enrolled in 'Grade 12'.
"""

# Student details
student_gpa = 3.8
student_absences = 2
student_grade_level = "Grade 12"
is_active_student = True

# --- Statements using Comparison Operators ---
# 1. Check GPA requirement.
has_high_gpa = student_gpa >= 3.5

# 2. Check attendance requirement.
has_good_attendance = student_absences < 5

# 3. Check grade level requirement.
is_correct_grade = student_grade_level == "Grade 12"

print("--- Student Honor Roll Eligibility Check ---")
print(f"Student GPA: {student_gpa} (Requirement: >= 3.5) -> Met: {has_high_gpa}")
print(f"Student Absences: {student_absences} (Requirement: < 5) -> Met: {has_good_attendance}")
print(f"Student Grade Level: '{student_grade_level}' (Requirement: 'Grade 12') -> Met: {is_correct_grade}")
print("-" * 45)

# --- Advanced Chained Comparison ---
# Let's check if a different student's GPA is in the 'B' range (3.0 to 3.9).
# Chaining is more readable than `gpa >= 3.0 and gpa < 4.0`.
b_student_gpa = 3.4
is_b_student = 3.0 <= b_student_gpa < 4.0

# a < 10 < c
# a < 10 && 10 < c

print("\n--- Chained Comparison Example ---")
print(f"Checking if GPA {b_student_gpa} is in the 'B' range (3.0 <= gpa < 4.0)...")
print(f"Result: {is_b_student}")