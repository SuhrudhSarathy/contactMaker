# file for making contacts

import numpy as np
import pandas as pd
import sys

#input the subject data
# ["name of the csv/vcf file", "Subject code with spaces or however is given in the google sheet", "number of groups"]
subject_codes = [['EG', 'BITS F110', 1],
                 ['EEE', 'EEE F111', 1],
                 ['THM', 'BITS F111', 4],
                 ['MOW', 'PHY F111', 3]
                 ]
subject_codes = pd.DataFrame(subject_codes,columns = ['Subject', 'Code', 'Batch Size'])

# take in the csv file name
file_name = 'contacts_students.csv'
df = pd.read_csv(file_name)
pd.options.display.float_format = '{:,.0f}'.format
df = df.iloc[:, [1, 2, 3, 4, 5]] # emoving the timestamp
df = df.ffill(axis = 1) #checking if whatsapp num is different from phone

#inserting an indicating zero to show chosen subject
for i in range(len(subject_codes)):
    df.insert(5+i, subject_codes.loc[i][0], 0)

# marking the counters according the   
for i in range(0, len(subject_codes)):
    for j in range(0, len(df)):
        if subject_codes.loc[i][1] in df.loc[j][4]:
            df.loc[j, subject_codes.loc[i][0]] = 1
#make a dict of contact list
contacts = {}
for i in range(0, len(subject_codes)):
    contacts[subject_codes.loc[i][0]] = df[df[subject_codes.loc[i][0]] == 1].iloc[:, :4]
a1 = contacts['EG']
#make contacts for csv
contacts_csv = {}
for i in range(0, len(subject_codes)):
    contacts_csv[subject_codes.loc[i][0]] = contacts[subject_codes.loc[i][0]].iloc[:, [0, 1, 3]].reset_index().iloc[:, 1:]
a = contacts_csv['EG']
alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#insert a column for contacts
for i in range(len(subject_codes)):
    contacts_csv[subject_codes.loc[i][0]].insert(3, 'Contact', 0)
#access id numbers and stuff
def make_contact(dataframe, batch_num, subject_code, i):
    batch_size = len(dataframe)/batch_num
    for j in range(0, len(dataframe)):
        reqd = str(dataframe.iloc[j][2])
        if j < batch_size:
            contact = "{}{}_{}".format(subject_codes.loc[i][1].replace(" ", ""), alphabets[0], reqd[8: 12])
            dataframe.loc[j, 'Contact'] = str(contact)
        elif j>= batch_size and j < 2 * batch_size :
            contact = "{}{}_{}".format(subject_codes.loc[i][1].replace(" ", ""), alphabets[1], reqd[8: 12])
            dataframe.loc[j, 'Contact'] = str(contact)
        elif j>= 2* batch_size and j < 3*batch_size :
            contact = "{}{}_{}".format(subject_codes.loc[i][1].replace(" ", ""), alphabets[2], reqd[8: 12])
            dataframe.loc[j, 'Contact'] = str(contact)
        elif j>= 3* batch_size and j < 4*batch_size :
            contact = "{}{}_{}".format(subject_codes.loc[i][1].replace(" ", ""), alphabets[3], reqd[8: 12])
            dataframe.loc[j, 'Contact'] = str(contact)
        elif j>= 4* batch_size and j < 5*batch_size :
            contact = "{}{}_{}".format(subject_codes.loc[i][1].replace(" ", ""), alphabets[4], reqd[8: 12])
            dataframe.loc[j, 'Contact'] = str(contact)
        else:
            contact = "{}{}_{}".format(subject_codes.loc[i][1].replace(" ", ""), alphabets[5], reqd[8: 12])
            dataframe.loc[j, 'Contact'] = str(contact)
    return dataframe
for i in range(0, len(subject_codes)):
    contacts_csv[subject_codes.loc[i][0]] = make_contact(contacts_csv[subject_codes.loc[i][0]],
                subject_codes.loc[i][2], subject_codes.loc[i][0], i)
b = contacts_csv[subject_codes.loc[1][0]]
#making an excel file
writer = pd.ExcelWriter('Contacts_separated.xlsx', engine = 'openpyxl')
for i in range(0, len(subject_codes)):
    contacts[subject_codes.loc[i][0]].to_excel(writer ,sheet_name = subject_codes.loc[i][0])
    contacts_csv[subject_codes.loc[i][0]].to_excel(writer ,sheet_name = subject_codes.loc[i][0] + '_contacts')    
writer.save()
writer.close()

#making vcf
for i in range(0, len(subject_codes)):
    contacts_csv[subject_codes.loc[i][0]].to_csv(subject_codes.loc[i][0]+ ".csv", index = False, header = False)
import csv
import sys

#convert a "comma separated values" file to vcf contact cards. I used this to convert a list of student
#names and phone numbers into a vcf and save the trouble of adding one by one through phone

#USAGE:
#CSV_to_Vcards.py CSV_filename


def convert(somefile, file2):
    #assuming file format : lastname,firstname,phonenumber,mail
    with open( somefile, 'r' ) as source:
        reader = csv.reader( source ) #reader now holds the whole data like ['lastname', 'firstname', 'phonenumber', 'mail']
        allvcf = open(file2, 'w') 
        i = 0
        for row in reader:
            
            allvcf.write( 'BEGIN:VCARD' + "\n")
            allvcf.write( 'VERSION:2.1' + "\n")
            allvcf.write( 'N:' + row[3] + "\n") # write the name of person
            allvcf.write( 'FN:' + row[2] + "\n") #write the name of the contact
            allvcf.write( 'ORG:' + "\n")
            allvcf.write( 'TEL;CELL:' + row[1] + "\n")
            allvcf.write( 'EMAIL:' + row[0] + "\n")
            allvcf.write( 'END:VCARD' + "\n")
            allvcf.write( "\n")

            i += 1#counts

        allvcf.close()
        print (str(i) + " vcf cards generated")


for i in range(0, len(subject_codes)):
    filename = subject_codes.loc[i][0]
    file_csv = '{}.csv'.format(filename)
    file_vcf = '{}.vcf'.format(filename)
    convert(file_csv, file_vcf)
print("Done!")
