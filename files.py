
import os
import shutil

filename = 'gettysburg.txt' # for your convenience

# set a to the current working directory
a = os.getcwd()

# write the following lines of text to a variable named b
#   do not include the ''' lines
b = '''
Four score and seven years
ago our fathers founded on
this continent a new nation,
conceived in Liberty and
dedicated to the proposition
that all men are created equal.
'''




# write the contents of b into a file named 'gettysburg.txt'
#  (this string is stored in the variable 'filename'!)
#  it will be in the current working directory;
#  remember to close the file!
# # put the open, write, close lines here
fp = open(filename, 'w')
fp.write(b)
fp.close()

# set c to the length of the file 'gettysburg.txt'
c = os.path.getsize(filename)

# is the "gettysburg.txt" a file?
d = os.path.isfile(filename)

# set e to the absolute path name of this file
e = os.path.abspath(filename)

# read the file 'gettysburg.txt' and
#   set f to the 2nd to last word of the 2nd to last line
#   (hint: use readlines and split)
## put the open, reading, close lines here
fp = open(filename)
lines = fp.readlines()
fp.close()
lineminus2 = lines[-2]
f = lineminus2.split()[-2]

# set g to a boolean that sees if here is a directory in the current
#  directory that is named 'subdir',
if os.path.exists('subdir'):
 shutil.rmtree('subdir') # DO NOT REMOVE: removes any previous subdir directory
g = os.path.exists('subdir')

# if the directory 'subdir' does not exist, create it
0  # put the check if path exists and make directory here
if os.path.exists('subdir') == False:
    os.mkdir('subdir')


# set h to the contents of the 'subdir' directory
h = os.listdir('subdir')

# copy the file 'gettysburg.txt' to the 'subdir' directory
#   then set i to the new contents of the 'subdir' directory
shutil.copy(filename, 'subdir')
i = os.listdir('subdir')

# change to the 'subdir' directory,
#   then copy the file 'gettysburg.txt' to 'gettysburg0.backup'
#   set j to the contents of the (current) directory
os.chdir('subdir')
shutil.copy2(filename, 'gettysburg0.backup')
j = os.listdir()


# (Still in the 'subdir' directory):
#   rename 'gettysburg.txt' to 'gettysburg1.txt';
#   set k to the contents of the (current) directory
shutil.move(filename, 'gettysburg1.txt')
k = os.listdir()

# variable l is not used!

# using the list of files in k, build a list of files
#   that ends with the extension '.txt'
#   and store the list in m
m = []
for filex in k:
    if filex.endswith('.txt'):
        m.append(filex)
# delete the file 'gettysburg1.txt', then
#   set n to the contents of the (current) directory
os.unlink('gettysburg1.txt')
n = os.listdir()

# Do not change any of the lines after this point
answers = [a, b, c, d, e, f, g, h, i, j, k, m, n ]
alpha = 'abcdefghijkmn';
for index in range(len(alpha)):
    print(alpha[index] + ' is:', answers[index])

# The expected output is (assuming starting in C:\Python class); do not delete
'''
================= RESTART: C:/Python class/Lab 12 - files.py =================
a is: C:\Python class
b is: 
Four score and seven years
ago our fathers founded on
this continent a new nation,
conceived in Liberty and
dedicated to the proposition
that all men are created equal.

c is: 177
d is: True
e is: C:\Python class\gettysburg.txt
f is: the
g is: False
h is: []
i is: ['gettysburg.txt']
j is: ['gettysburg.txt', 'gettysburg0.backup']
k is: ['gettysburg0.backup', 'gettysburg1.txt']
m is: ['gettysburg1.txt']
n is: ['gettysburg0.backup']
>>> 
'''
