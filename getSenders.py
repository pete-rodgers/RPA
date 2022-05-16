from PIL import Image
import pytesseract
import extract_msg
import os
import csv

print("Looping through directories")
#create a table containing two columns, sender and count
table = []

directoryPath = '/Users/mattfalconer/Desktop/Automation Anywhere/Molylycke/NewScript/'

# #create folder /Users/mattfalconer/Desktop/Automation Anywhere/Molylycke/NewScript/Extracted/
# if not os.path.exists('/Users/mattfalconer/Desktop/Automation Anywhere/Molylycke/NewScript/Extracted/'):
#     os.makedirs('/Users/mattfalconer/Desktop/Automation Anywhere/Molylycke/NewScript/Extracted/')
# else:
#     #overwrite folder
#     os.system('rm -rf /Users/mattfalconer/Desktop/Automation Anywhere/Molylycke/NewScript/Extracted/*')

#loop through all files in '/Users/mattfalconer/Documents/Automation Anywhere/Molylycke/NewScript'

for files in os.listdir(directoryPath):
    if files.endswith('.msg'):
        attachmentsTable = []
        print("Found")
        msg = extract_msg.openMsg(directoryPath + files)
        #get the sender name
        sender = msg.sender
        #get attachment name, if pdf
        if msg.attachments:
            for attachment in msg.attachments:
                #save attachment to folder
                msg.saveAttachments()
        #get email address from string
        try:
            email = sender.split('<')[1].split('>')[0]
        except:
            email = sender.split('<')[0].split('>')[0]

        #get website from string, remove tld
        try:
            website = email.split('@')[1].split('.')[0]
        except:
            website = email.split('@')[0].split('.')[0]

        #add subject to list
        table.append([email, website])


#write table to csv
with open(directoryPath + 'Senders.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table)