#!/usr/bin/python
import os

def addAccenture(name):
	if str(name[:9]) != 'Accenture':
		return 'Accenture-' + name
	else:
		return name

def duplicates(name):
	lst = list(name)
	for x in range(len(lst)):
		if lst[x] == '-' and lst[x+1] == '-':
			lst[x] = ''
		if lst[x] == ' ' and lst[x+1] == ' ':
			lst[x] = ''
	return ''.join(lst)

def capitalize(name):
	lst = list(name)
	for x in range(len(lst)):
		if lst[x] == '-' and lst[x+1].isalpha():
			lst[x+1] = lst[x+1].upper()
	return ''.join(lst)

print os.getcwd()
table = {}

for file in os.listdir(os.getcwd()):
	if '.txt' in file or '.pdf' in file or '.png' in file or '.jpg' in file or '.js' in file or '.css' in file or '.pptm' in file or '.pptx' in file or '.docx' in file or '.doc' in file:
		new_name = ''
		new_name =  '-'.join(file.split('_'))
		new_name =  '-'.join(new_name.split(' '))
		new_name =  '-'.join(new_name.split(' _ '))
		new_name =  '-'.join(new_name.split(' - '))
		new_name = capitalize(duplicates(addAccenture(new_name)))
		table[str(file)] = new_name
		os.rename(file, new_name)

for old_name, new_name in table.items():
            print '{0:10} ==> {1:10}'.format(old_name, new_name)