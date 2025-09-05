principal_amount = 10000.1234  # P: Initial amount in dollars
annual_rate = 0.05           # r: 5% annual interest rate
compounds_per_year = 12      # n: Compounded monthly
years = 10                   # t: Investment duration

#Exponents `**`: The result of the parentheses is raised to the power of `(compounds_per_year * years)`.
future_value = principal_amount * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)

print("--- Compound Interest Calculation ---")
print(f"Principal amount: ${principal_amount:.2f}")
print(f"Annual Interest Rate: {annual_rate * 100}%")
print(f"Compounding Frequency: {compounds_per_year} times per year")
print(f"Investment Duration: {years} years")
print("-" * 40)
print(f"Future Value of Investment: ${future_value:,.2f}")

total_cents = int(future_value * 100)
full_dollars = total_cents // 100
remaining_cents = total_cents % 100

print("\n--- Breakdown using // and % ---")
print(f"Total value in cents: {total_cents}")
print(f"Full dollars part: ${full_dollars} (calculated with //)")
print(f"Remaining cents part: {remaining_cents} cents (calculated with %)")