import numpy as np
import csv
from cryptography.fernet import Fernet
import hashlib
import random
import array

ipp = input("Enter the search ")
nonce = random.randint(1,100000)
nonce = str(nonce)
l = [ord(a) ^ ord(b) for a,b in zip(nonce, ipp)]

print(l)
l = ''.join(str(e) for e in l)
print(l)
hash_object = hashlib.md5(l.encode())
#abc = hashlib.md5(b'MST3K')

pp = 1

op_data= []

with open('Data.tsv') as tsk:
    tsk = csv.DictReader(tsk, dialect='excel-tab')
    
    for row in tsk:
        for word in row['review'].split():
            l2 = [ord(a) ^ ord(b) for a,b in zip(nonce, word)]
            l2 = ''.join(str(e) for e in l2)
            new_ciph = hashlib.md5(l2.encode())
            if new_ciph.hexdigest() == hash_object.hexdigest():
                op_data.insert(0,row['review'])
                pp = 0
#plain_text = cipher_suite.decrypt(cipher_text)
#if abc.hexdigest() == hash_object.hexdigest():
    #pp = 1
print(pp)
print(op_data)
