
# Sample data rampur 
# Total population (excluding kids)
total_population = 1000

# Number of men and women
men = 500
women = 500

# Number of literate men and women
literate_men = 400
literate_women = 300

# Kids (excluded from literacy rate calculations)
kids = 250

# Adjust total population to exclude kids
adult_population = total_population - kids

# Illiterate men and women
illiterate_men = men - literate_men
illiterate_women = women - literate_women

# Percentage calculations
def calculate_percentage(part, whole):
       return (part / whole) * 100 if whole > 0 else 0

# Literacy percentages
literate_men_percentage = calculate_percentage(literate_men, men)
literate_women_percentage = calculate_percentage(literate_women, women)

# Illiteracy percentages
illiterate_men_percentage = calculate_percentage(illiterate_men, men)
illiterate_women_percentage = calculate_percentage(illiterate_women, women)

# Display the results
print(f"Literate Men: {literate_men_percentage:.2f}%")
print(f"Illiterate Men: {illiterate_men_percentage:.2f}%")
print(f"Literate Women: {literate_women_percentage:.2f}%")
print(f"Illiterate Women: {illiterate_women_percentage:.2f}%")
