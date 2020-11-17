import json
import csv
import os
import shutil



# Opening JSON files
list_json_files = os.listdir('C:/Users/Public/DevOps/devops/JSON_Files')

for filejson in list_json_files:
    print(filejson)

    # Loading the data into the variable data
    with open('JSON_Files/%s' % filejson) as json_file:
        print(type(json_file))
        data = json.load(json_file)
        print(type(json_file))

    employee_data = data['emp_details']

    file_name = filejson[:-5]
    print(file_name)
    # now we will open a file for writing
    data_file = open('CSV_Files/%s.csv' % file_name, 'w')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for emp in employee_data:
        if count == 0:

            # Writing headers of CSV file
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(emp.values())

    data_file.close()
    
    shutil.move('C:/Users/Public/DevOps/devops/JSON_Files/%s' % filejson , 'C:/Users/Public/DevOps/devops/Used_JSON/%s' % filejson)