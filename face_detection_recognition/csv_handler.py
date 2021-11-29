import csv


def insertData(data):
    field = ['Name', "Age", "Gender", "DOB", "Address", "Blood Group", "NIC", "Crimes"]
    x = [data['Name'], data["Age"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Address'], data['Blood Group'],
         data['NIC'], data['Crimes Done']]
    filen = "Criminals_details.csv"
    with open(filen, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(x)
