# This scrpts tells the user hemoglobin value with the given of amount
# using boolean comparission and/or/not e.g 
# todo: add exception handling 
print("Enter your gender: ")
gender = input(">>> ")
print("Enter your hemoglobin value: ")
hemoglobin_value = float(input(">>> "))

if gender == "male" and hemoglobin_value < 134:
    print("Hemoglobin value is low")
elif gender == "male" and hemoglobin_value > 167:
    print("Hemoglobin value is high")
elif gender == "male" and hemoglobin_value >= 134 and hemoglobin_value <= 167:
    print("Hemoglobin value is normal")

elif gender == "female" and hemoglobin_value < 117:
    print("Hemoglobin value is low")
elif gender == "female" and hemoglobin_value > 155:
    print("Hemoglobin value is high")
elif gender == "female" and hemoglobin_value >= 117 and hemoglobin_value <= 155:
    print("Hemoglobin value is normal")
else:
    print("invalid input")
