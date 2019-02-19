import pandas as pd
import re
import itertools
import numpy as np

fname = "filepath_here"

with open(fname) as f:
    content = [s.strip() for s in f.readlines()]

def parseFASTA(content):
    sequences = []
    current_string = ''
    for index,elem in enumerate(content[1:]):
        if '>Rosalind' in elem:
            sequences.append(current_string)
            current_string = ''
        else:
            current_string += elem
    sequences.append(current_string)        
    return(sequences)
    
test = parseFASTA(content)

def getConsensus(list_of_sequences):
    df = pd.DataFrame(columns = list(range(len(test[0]))))

    for seq in test:
        df.loc[len(df)] = list(seq)

    final_string = ''.join(list(df.mode().loc[0]))
    count_matrix = np.empty((len(['A','C','G','T']),len(df.loc[0])),dtype=np.int64)
    
    for i in range(len(df.loc[0])):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        current_col = df[i]
        for char in current_col:
            if char == 'A':
                a_count += 1
            elif char == 'C':
                c_count += 1
            elif char == 'G':
                g_count += 1
            elif char == 'T':
                t_count += 1
        count_matrix[:,i] = [a_count,c_count,g_count,t_count]
    print(final_string)
    print('A:',' '.join(str(x) for x in count_matrix[0,:]))
    print('C:',' '.join(str(x) for x in count_matrix[1,:]))
    print('G:',' '.join(str(x) for x in count_matrix[2,:]))
    print('T:',' '.join(str(x) for x in count_matrix[3,:]))
    return(final_string,count_matrix)
