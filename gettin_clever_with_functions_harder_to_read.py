first_name = input('Enter your first Name: ')
first_name_initial = first_name[0:1].upper()

middle_name = input('Enter your middle name: ')
middle_name_initial = middle_name[0:1].upper()

last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1].upper()


print('Your initials are : ' + first_name_initial \
    + middle_name_initial + last_name_initial)
