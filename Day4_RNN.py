from __future__ import print_function
from keras.layers import Dense, Activation
from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential
import numpy as np

fin=open('alice.txt', 'rb')
lines = []
for line in fin:
  line = line.strip().lower()
  line = line.decode('ascii', 'ignore')
  if(len(line) == 0):
    continue
  lines.append(line)
fin.close()

text = ' '.join(lines)

# Counting number of unique chars

chars = set([c for c in text])
nb_chars = len(chars)

char2index = dict((c,i) for i,c in enumerate(chars))
index2char = dict((i,c) for i,c in enumerate(chars))

input_chars = []
label_chars = []

for in range(0,len(text)-11,1):
  input_chars.append(text[i:i+10])
  label_chars.append(text[i+10])

x=np.zeros((len(input_chars),10,nb_chars),dtype=np.bool)
x=np.zeros((len(input_chars),nb_chars),dtype=np.bool)

for i, word in enumerate(input_chars):
  for j, ch in enumerate(word)
    x[i,j,char2index[ch]] = 1
  y[i,char2index[label_chars[i]]] = 1



