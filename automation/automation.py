import re

# Given a document potential-contacts, 
with open("../assets/potential_contacts.txt") as f:
    doc = f.read()


# find and collect all email addresses and phone numbers.
# Phone numbers may be in various formats.
# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
phone_list= []

phone_pattern_area_code = r"\(?([1-9]{3})\)?[-.]?([1-9]{3})[-.]?([0-9]{4})"
phone_pattern_local = r"\(?\s([([0-9]{3})[-.]?([0-9]{4})"
email_pattern = r"[A-Za-z]+?[0-9[._]{1}[A_Za-z0-9]*[@][a-z]*[.][a-z]{3}"


phone_nums= re.findall(phone_pattern_area_code, doc)
local_phone_nums = re.findall(phone_pattern_local, doc)
emails = set(re.findall(email_pattern, doc))
# print('local: ', phone_nums)
result_phones = ['-'.join(nums) for nums in phone_nums]

for number in phone_nums:
    fixed_number = ('-').join(number)
    if fixed_number in phone_list:
        continue
    phone_list.append(fixed_number)
    # f.write(str(number))
print(phone_list)

with open("../assets/emails.txt", "a") as e:
    email_contacts = e.read()
    for email in emails:
        lambda email, email_contacts: email_contacts.write(str(email))
        
    # print(email_contacts)

# print("email: ", emails)
def format_phones(phone_list):
    #if doesn't match correct pattern, strip and rebuild number
    #if doesn't have an area code, add 206 to front.
    for number in phone_list:
        if len(number.split()) in phone_list <= 8:
            pass
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.
# Once emails and phone numbers are found they should be stored in two separate documents.
# The information should be sorted in ascending order.
# Duplicate entries are not allowed.

# phone_numbers.txt
# 123-456-7890
# 206-678-9012
# 234-567-8901

# emails.txt
# ana@foo.bar
# bill_x@foo.bar
# chris.schmidt@bar.baz