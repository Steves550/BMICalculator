# Create a variable named person_list that contains a list of six names.
person_list = ["Steve", "Sarah", "Kevin", "Mark", "Brittany", "Carmen"]

# In a variable named bmi_result set the variable equal to an empty array.
bmi_result = []

# Create three variables named under_weight_count, normal_weight_count, and over_weight_count.
# Set all three variables equal to zero.
under_weight_count = 0
normal_weight_count = 0
over_weight_count = 0

# The first display message will show the user the instructions for what they have to do.
# Explain and show an example of how the user should enter an individual's height and weight.
# The user is to enter the height in inches and the weight in pounds.
print("Enter the height and weight for each of the 6 individuals in the provided list.\n")
print("For each individual's height enter the number in inches.\nExample: Steve's height = 72.\n")
print("For each individual's weight enter the number in pounds.\nExample: Steve's weight = 180.")

# Create a function named person_bmi that will contain the body mass index formula.
# In the function create a variable named bmi set equal to this formula.
# The function parameters will be person_height and person_weight. These parameters will be used in a for loop.
def person_bmi(person_height, person_weight):
    bmi = person_weight * (703 / person_height**2)
    
    # Return the variable bmi.
    return bmi

# Create a function named weight_category.
# Pass in bmi as a parameter returned from the person_bmi function.
# In the function create one if and two elif statements.
def weight_category(bmi):
    
    # The if statemetnt will check for a bmi of less than 18.5. If true return underweight.
    if bmi < 18.5:
        return "underweight"
    
    # The elif statement checks for bmi greater than or equal to 18.5 and less than or equal to 24.9. If true return normal weight.
    elif bmi >= 18.5 and bmi <= 24.9:
        return "normal weight"
    
    # The second elif statemtnt checks for bmi greater than 24.9. If true return overweight.
    elif bmi > 24.9:
        return "overweight"

# Create a for loop that will in range loop through the length of person_list.
# Create two variables named person_height and person_weight.
for i in range(len(person_list)):
    
    # Both variables will be a float input that prompts the user for the height and weight of the current name in the iteration.
    # Inside of an f string use {person_list[i]} for displaying the name of the current person in that iteration of the loop. For height and weight.
    person_height = float(input(f"\nWhat is the height for {person_list[i]}?: "))
    person_weight = float(input(f"How much does {person_list[i]} weigh?: "))

    # Set bmi equal to the function call of person_bmi(person_height, person_weight). Call the function with both parameters passed in.
    bmi = person_bmi(person_height, person_weight)

    # Append the bmi variable data to bmi_results.
    bmi_result.append(bmi)

# This is here to space out the first for loop from the second for loop when displayed to the user.
print()

# Create a for loop for bmi in bmi_result.
for bmi in bmi_result:
    # Create a varaible named bmi_category set equal to the function call of weight_category(bmi). Pass in bmi as the parameter.
    bmi_category = weight_category(bmi)

    # Create a variable named determine_person set equal to person_list that pulls data from bmi_result.index(bmi).
    # This variable is important for later displaying exactly what individual by name is under, normal, or overweight.
    determine_person = person_list[bmi_result.index(bmi)]

    # Create one if statement and two elif statements.
    # Each statement will check if the bmi_category is equal to underweight, normal weight, or overweight.
    # Depending on which statement is true the count for the variables under_weight_count, normal_weight_count, and over_weight_count will increase.
    if bmi_category == "underweight":
        under_weight_count = under_weight_count + 1
    elif bmi_category == "normal weight":
        normal_weight_count = normal_weight_count + 1
    elif bmi_category == "overweight":
        over_weight_count = over_weight_count + 1

    # Display to the user at the end of the loop what individuals by name are under, normal, or overweight.
    # Inside of the f string use the variable determine_person for displaying the name of each individual.
    # Also inside of the f string include the variable bmi_category for displaying where each individual falls based on their BMI.
    print(f"{determine_person} is {bmi_category}")

# Create three print() functions. Each print() function will display to the user the number of under, normal, and overweight indiviuals in the list.
print(f"\nNumber of underweight individuals: {under_weight_count}")
print(f"Number of normal weight individuals: {normal_weight_count}")
print(f"Number of over weight individuals: {over_weight_count}")



