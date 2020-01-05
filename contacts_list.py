import numpy as np
import pandas as pd

subject_codes = [['EG', 'BITSF110'],
                 ['M1', 'MATHF111'],
                 ['PS', 'MATHF113'],
                 ['CH', 'CHEMF111'],
                 ['BI', 'BIOF111'],
                 ['MOW', 'PHYF111']
                 ]
subject_codes = pd.DataFrame(subject_codes, columns=['Subject', 'Code'])


#making the dataframe ready
file_name = r'C:\Users\Suhrudh\Desktop\dual_boot\CTE_Files\contacts.csv'
df = pd.read_csv(file_name)
df = df.iloc[:, 1:]
df = df.ffill(axis = 1) #checking if whatsapp num is different from phone
df.insert(6, 'EG', 0)
df.insert(7, 'M1', 0)
df.insert(8, 'PS', 0)
df.insert(9, 'CH', 0)
df.insert(10, 'BI', 0) 
df.insert(11, 'MOW', 0)
for i in range(0, len(df)):
    if 'BITS F110' in df.iloc[i][5]:
        df.at[i, 'EG'] = 1
for i in range(0, len(df)):
    if 'MATH F111' in df.iloc[i][5]:
        df.at[i, 'M1'] = 1   
for i in range(0, len(df)):
    if 'MATH F113' in df.iloc[i][5]:
        df.at[i, 'PS'] = 1       
for i in range(0, len(df)):
    if 'CHEM F111' in df.iloc[i][5]:
        df.at[i, 'CH'] = 1        
for i in range(0, len(df)):
    if 'BIO F111' in df.iloc[i][5]:
        df.at[i, 'BI'] = 1       
for i in range(0, len(df)):
    if 'PHY F111' in df.iloc[i][5]:
        df.at[i, 'MOW'] = 1     

# separate each batch guys
eg = df[df['EG'] == 1].iloc[:, :5]
m1 = df[df['M1'] == 1].iloc[:, :5]
ps = df[df['PS'] == 1].iloc[:, :5]
ch = df[df['CH'] == 1].iloc[:, :5]
bi = df[df['BI'] == 1].iloc[:, :5]
mow = df[df['MOW'] == 1].iloc[:, :5]



#make the contact csv
eg_1 = eg.iloc[:, [2, 4]].reset_index().iloc[:, 1:]
m1_1 = m1.iloc[:, [2, 4]].reset_index().iloc[:, 1:]
ps_1 = ps.iloc[:, [2, 4]].reset_index().iloc[:, 1:]
ch_1 = ch.iloc[:, [2, 4]].reset_index().iloc[:, 1:]
bi_1 = bi.iloc[:, [2, 4]].reset_index().iloc[:, 1:]
mow_1 = mow.iloc[:, [2, 4]].reset_index().iloc[:, 1:]

# access id phone number and make csv
#doing this for specific groups
#eg
subject_codes = [['EG', 'BITSF110'],
                 ['M1', 'MATHF111'],
                 ['PS', 'MATHF113'],
                 ['CH', 'CHEMF111'],
                 ['BI', 'BIOF111'],
                 ['MOW', 'PHYF111']
                 ]
subject_codes = pd.DataFrame(subject_codes, columns=['Subject', 'Code'])

#decide batch size

alphabets = list('ABCDEF')
#batch numbers for each batch
batch_num_eg = 3
batch_num_m1 = 6
batch_num_ps = 3
batch_num_ch = 4
batch_num_bi = 6
batch_num_mow = 6

## looping through all the entries and making a dataframe
eg_1.insert(2, 'Contact', 0)
m1_1.insert(2, 'Contact', 0)
ps_1.insert(2, 'Contact', 0)
ch_1.insert(2, 'Contact', 0)
bi_1.insert(2, 'Contact', 0)
mow_1.insert(2, 'Contact', 0)
def make_contact(dataframe, batch_num, subject_code):
    n = subject_codes.index[subject_codes['Code']==subject_code][0]
    batch_size = len(dataframe)/batch_num
    for i in range(0, len(dataframe)):
        reqd = str(dataframe.iloc[i][1])
        if i < batch_size:
            contact = "{}{}_{}".format(subject_codes.iloc[n][1], alphabets[0], reqd[8: 12])
            dataframe.loc[i, 'Contact'] = str(contact)
        elif i>= batch_size and i < 2 * batch_size :
            contact = "{}{}_{}".format(subject_codes.iloc[n][1], alphabets[1], reqd[8: 12])
            dataframe.loc[i, 'Contact'] = str(contact)
        elif i>= 2* batch_size and i < 3*batch_size :
            contact = "{}{}_{}".format(subject_codes.iloc[n][1], alphabets[2], reqd[8: 12])
            dataframe.loc[i, 'Contact'] = str(contact)
        elif i>= 3* batch_size and i < 4*batch_size :
            contact = "{}{}_{}".format(subject_codes.iloc[n][1], alphabets[3], reqd[8: 12])
            dataframe.loc[i, 'Contact'] = str(contact)
        elif i>= 4* batch_size and i < 5*batch_size :
            contact = "{}{}_{}".format(subject_codes.iloc[n][1], alphabets[4], reqd[8: 12])
            dataframe.loc[i, 'Contact'] = str(contact)
        else:
            contact = "{}{}_{}".format(subject_codes.iloc[n][1], alphabets[5], reqd[8: 12])
            dataframe.loc[i, 'Contact'] = str(contact)
    dataframe = dataframe.iloc[:, [0, 2]]
    return dataframe
eg_1 = make_contact(eg_1, batch_num_eg, subject_codes.iloc[0][1])
m1_1 = make_contact(m1_1, batch_num_m1, subject_codes.iloc[1][1])
ps_1 = make_contact(ps_1, batch_num_ps, subject_codes.iloc[2][1])
ch_1 = make_contact(ch_1, batch_num_ch, subject_codes.iloc[3][1])
bi_1 = make_contact(bi_1, batch_num_bi, subject_codes.iloc[4][1])
mow_1 = make_contact(mow_1, batch_num_mow, subject_codes.iloc[5][1])

# make an excel sheet for the following contact lists


writer = pd.ExcelWriter('Contacts_separated.xlsx', engine = 'openpyxl')

eg.to_excel(writer ,sheet_name = 'EG')
m1.to_excel(writer,sheet_name = 'M1')
ps.to_excel(writer,sheet_name = 'PS')
ch.to_excel(writer,sheet_name = 'CH')
bi.to_excel(writer,sheet_name = 'BI')
mow.to_excel(writer,sheet_name = 'MOW')
eg_1.to_excel(writer ,sheet_name = 'EG_contacts')
m1_1.to_excel(writer,sheet_name = 'M1_contacts')
ps_1.to_excel(writer,sheet_name = 'PS_contacts')
ch_1.to_excel(writer,sheet_name = 'CH_contacts')
bi_1.to_excel(writer,sheet_name = 'BI_contacts')
mow_1.to_excel(writer,sheet_name = 'MOW_contacts')
writer.save()
writer.close()

eg_1.to_csv("EG_contacts.csv", index = False, header = False)
m1_1.to_csv("M1_contacts.csv", index = False, header = False)
ps_1.to_csv("PS_contacts.csv", index = False, header = False)
ch_1.to_csv("CH_contacts.csv", index = False, header = False)
bi_1.to_csv("BI_contacts.csv", index = False, header = False)
mow_1.to_csv("MOW_contacts.csv", index = False, header = False)