# ContactMaker
Making vcfs from the csv file downloaded from google forms

**Format of the Google Sheet**
(column-wise)
1. Timestamp (automatically provided by google sheets)
2. Email-Address
3. Whatsapp Number
4. Name
5. BITS ID
6. Subjects for Registration (*Make sure to add space between the codes, ex: ABC F234* and not *ABCF234*)

**Inputs by the user**
Input has to be the following:
***Subject Name*, *Subject Code*, *Batch Size*** for each subject.
eg:
'ABC', 'CDFG F234', 36

**Output**
1. A csv file containing split students and the contact information
2. A separate csv and a vcf file for each subject with their contact
**Contact making**
If the ID number is 1234F5GH*7645* and the student has chosen a subject 'CDFG F234', then the contact made will be
**CDFGF324_*A*7645**, here 'A' will be allotted based on batch size.


