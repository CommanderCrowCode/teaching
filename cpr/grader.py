# import data
from explorer.menu import *

def count_digits(input):
    return int(math.log10(input))+1

print("Select a file inside a folder that contains the raw grade file.")
input()
targetFile = menu('./',['.csv'])
print(targetFile)

# data['IDcheck'] = data['StudentID'].apply(count_digits)
