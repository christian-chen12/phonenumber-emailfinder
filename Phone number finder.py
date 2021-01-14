import re, pyperclip

# Find phone number
phoneRegex = re.compile(r''' 
# 123-456-7890, 123-4567, (123) 456-7890, 123-4567 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)                          # first seperator 
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s)|x)               # extensions word part(optional)
(\d{2,5}))?                     # extension number part(optional)
)      
''', re.VERBOSE)

# Find email
emailRegex = re.compile(r''' 
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+   # name part
@                 # @ symbol
[a-zA-Z0-9_.+]+   # domain part

''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

