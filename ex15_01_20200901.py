from sys import argv

script, fileName = argv

txtName = open(fileName)

print(txtName.read())

