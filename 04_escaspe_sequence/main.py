# \n \f \t \b

print("Hello\nWorld", end='$$') # space
print("World")

print("abc\fxyz")

# abc
#    xyz

print("Hellooasdfas\rWorld")

# Worldooasdfas

student_name = "Maria"
student_id = 4045
average_score = 92.8754

print("Report Card:\n---------------")
# \t (Horizontal Tab): Inserts a tab space.
print(f"Name:\t{student_name}")
print(f"ID:\t{student_id}")

# \" (Double Quote): Inserts a literal double quote inside a string delimited by double quotes.
print("Comment:\t\"A very dedicated student.\"")

# \\ (Backslash): Inserts a literal backslash. Used commonly for file paths.
print("File saved at: C:\\New_Reports\\Final.txt")

# This will print "12346" because the '5' is "backspaced" over by the '6'.
print("Loading: 12345\b6")

# \r (Carriage Return): Moves the cursor to the start of the current line.
# Subsequent characters overwrite the beginning of the line.
# This will print "CompleteGHIJK".
print("ABCDEFGHIJK\rComplete")

# \f (Form Feed): Historically used to eject a page on a printer.
# In most modern terminals, it may just print a special symbol or move down.
print("Page 1 Summary\fPage 2 Details")

# \x (Hex escape): Prints the character corresponding to the hex value. (Hex 41 = 'A').
print("Grade: \x41")

# \N{Name} (Unicode Name): Prints the symbol corresponding to its official Unicode name.
print("Currency: \N{euro sign} \N{yen sign} \N{dollar sign}")
print("Symbols: \N{copyright sign} \N{black universal recycling symbol}")
print("Math: Area = \N{greek small letter pi}r\N{superscript two}, H\N{subscript two}O")

print("\n--- 4. Print() Function Parameters (sep and end) ---")
# Using 'end' to stop print() from adding a newline.
# This prints both statements on the same line, separated by a comma and space.
print(f"Student: {student_name}", end=', ')
print(f"ID: {student_id}")


# Using 'sep' to define the separator between multiple arguments passed to print().
print("Name", "ID", "Score", sep=' | ')
print(student_name, student_id, average_score, sep=' | ')

#%d %f %s %x
# f""

# A. %-Formatting (C-Style / Old Style)
print("\nA. %-Formatting:")
print("Details: Name %s (ID: %d) has an average of %f." % (student_name, student_id, average_score))
# Formatting: %-10s = Left-align string in 10 spaces. %.2f = float with 2 decimal places.
print("Padded: |%-10s| Score: %.2f" % (student_name, average_score))


# B. .format() Method
print("\nB. .format() Method:")
# Implicit order (empty braces)
print("Details: Name {} (ID: {}) has an average of {}.".format(student_name, student_id, average_score))
# Indexed order (re-using arguments)
print("Repeating: {0} loves Python. ID: {1}. {0} is great.".format(student_name, student_id))
# Formatting with alignment/precision:
# {0:<10} = Arg 0, Left-aligned, 10 spaces
# {1:^10} = Arg 1, Center-aligned, 10 spaces
# {2:>.2f} = Arg 2, Right-aligned, 2 decimal places (float)
print("Aligned: |{0:<10}|{1:^10}|{2:>.2f}|".format(student_name, student_id, average_score))

# C. f-Strings (Formatted String Literals / Modern Style)
print("\nC. f-Strings (Most Recommended):")
print(f"Details: Name {student_name} (ID: {student_id}) has an average of {average_score}.")
# Formatting is built directly into the braces.
# {student_name:>10} = Right-align in 10 spaces
# {average_score:^10.2E} = Center-align in 10 spaces, Scientific Notation, 2 decimal places
print(f"Aligned: |{student_name:>10}|{average_score:^10.2E}|")