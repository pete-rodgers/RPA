import extract_msg
import os
import csv

print("Looping through directories")
#create a table containing two columns, sender and count
table = []

directoryPath = 'C:/test/Molnlycke/data cleanse/DE 5 - May/'

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
#        print("Found")
        msg = extract_msg.openMsg(directoryPath + files)
        #get the sender name
        sender = msg.sender
#        emailfilename = msg.name
        subject = msg.subject
        sentdate = msg.date
        #get attachment name, if pdf
        if sender.endswith('molnlycke.com>'):
            for attachment in msg.attachments:
                ##save attachment to folder
#                attachmentname = msg.attachments.name
                msg.saveAttachments()
                print("Found Molnlycke")
                print(files.startswith)
        #get email address from string
#        try:
        #        except:
#            email = sender.split('<')[0].split('>')[0]

        #get website from string, remove tld
#        try:
            #website = email.split('@')[1].split('.')[0]
        #except:
            #website = email.split('@')[0].split('.')[0]

        #add subject to list
        table.append([sender, subject, sentdate])


#write table to csv
with open(directoryPath + 'Senders.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table)