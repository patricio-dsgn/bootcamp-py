import os

dir = './caja/'
file = './data.json'

dir = os.path.exists(dir)
file = os.path.exists(file)

print(dir)
print(file)
