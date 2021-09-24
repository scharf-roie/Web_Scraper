#! python3

#TODO: Create regex for phone number and email
#Get text off clipboard
#Extract email/phone from text
#Copy extracted email/phone to clipboard

import re, pyperclip

phoneRegex = re.compile(r"""
(
((\d\d\d)|(\(\d\d\d\)))?                #area code (optional)
(\s|-)                                       # first seperator - or space
\d\d\d                                      # first 3 digits
-                                             # 2nd seperator
\d\d\d\d                                                # last 4 digits
(((ext(\.)?\s)|x)
(\d{2,5}))?             #extension
)
""", re.VERBOSE)

emailRegex = re.compile(r"""

[a-zA-Z0-9_.+]+ #Name part of email
@
[a-zA-Z0-9_.+]+ # Domain name
                # Code does not account for pdf where spaces are not put before email
""", re.VERBOSE)

text = pyperclip.paste()


extractedPhone = phoneRegex.findall(text)

extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for  i in extractedPhone:
    if len(i[0]) == 12: #i[0] is the first group in the tuple
        allPhoneNumbers.append(i[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results) #Results are copied to clipboard and can be pasted
