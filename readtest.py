import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler

output_dir = 'output_data'
os.makedirs(output_dir, exist_ok=True)

def read_data(filename):
    x = pickle._Unpickler(open(filename, 'rb'))
    x.encoding = 'latin1'
    data = x.load()
    return data

labels = []
data = []

fileph = ".\output_data/data_n0_i0.dat"
d = read_data(fileph)
labels.append(d['label'])
data.append(d['data'])

print(d['label'])
print(data)
