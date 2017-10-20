#WINDOWS FILE LIST EXTRACTOR
#21-10-2017
import os
from os.path import join,getsize

if os.name == 'posix':
    base = '/windows/'
else:
    base = '/'

all_files = list()

for root,dirs,files in os.walk(base):
    for f in files:
        all_files.append((os.path.join(root,f)[len(base):] + '\n').replace('\\','/'))
newfile = open('Windows_file_list.txt','w')
newfile.writelines(sorted(all_files))
newfile.close()

