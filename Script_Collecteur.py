import json
import csv

# Opening JSON file and loading the data
# into the variable data
# Plusieur fichiers jsons (déplacé)
with open('JSON_Files/fichier3.json') as json_file:
    data = json.load(json_file)

employee_data = data['emp_details']
print(employee_data)

# now we will open a file for writing

with open('CSV_Files/fichier3.csv', "w", newline='') as data_file:
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    print(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for emp in employee_data:

        header = emp.keys()
        print(header)
        csv_writer.writerow(header)
        # Writing data of CSV file
        values = emp.values()
        csv_writer.writerow(values)
        print(emp.values())


data_file.close()
