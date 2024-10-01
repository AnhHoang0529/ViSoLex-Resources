from rules import *
from generate_rule_dict import *
from ast import literal_eval
import pandas as pd
import numpy as np
import os,sys
import pickle
import re
import json
import random
from tqdm import tqdm

def custom_str(x):
    if isinstance(x, float):
        return np.format_float_positional(x)
    return str(x)

def flatten_lst(lst):
  return [word for element in lst for word in element.split()]

DATA_PATH = "/content/drive/MyDrive/LexNorm/KLTN/Data/ViLexNorm/ViLexNorm.csv"
DATA_ALIGNED_PATH = "/content/drive/MyDrive/LexNorm/KLTN/Data/ViLexNorm/Token_data/Segment/ViLexNorm_segment.json"
DICTIONARY_PATH = "/content/drive/MyDrive/LexNorm/KLTN/Data/ViLexNorm/dictionary/LexNorm_dict_segment.json"
DATA_U_PATH = "/content/drive/MyDrive/LexNorm/KLTN/Data/ASTRA/downstream_data.csv"

with open(DICTIONARY_PATH, 'r') as f:
    dictionary = json.load(f)

with open(DATA_ALIGNED_PATH, 'r') as f:
    aligned_data = json.load(f)
aligned_data = pd.DataFrame(aligned_data)

data = pd.read_csv(DATA_PATH)
data_u = pd.read_csv(DATA_U_PATH, converters={'input': literal_eval})

d_U = data_u[['original', 'input']]
d_U['original'] = d_U['original'].apply(custom_str)

data['input'] = aligned_data['input'].copy()
data['output'] = aligned_data['output'].copy()

data['regrex_rule'] = ''*len(data)
data['dict_rule'] = ''*len(data)

d_U['regrex_rule'] = ''*len(d_U)
d_U['dict_rule'] = ''*len(d_U)

df_U =  pd.DataFrame(columns=['original', 'input', 'regrex_rule', 'dict_rule'])
for i in tqdm(range(0,len(d_U)), desc ="Proccessed:"):
    sent = d_U['original'][i]
    sent_lst = d_U['input'][i].copy()
    regrex_sent = regrex_rule(sent, sent_lst, rule_list)
    sent_lst = data_u['input'][i].copy()
    dict_sent = dictionary_rule(sent, sent_lst, dictionary)
    df_U.loc[len(df_U)] = {'original': d_U['original'][i], 
                        'input': d_U['input'][i],                        
                        'regrex_rule': regrex_sent,
                        'dict_rule': dict_sent}
df_U.to_csv("/content/drive/MyDrive/LexNorm/KLTN/Code/astra/data/unlabeled.csv")

df = pd.DataFrame(columns=['original', 'normalized', 'input', 'output', 'regrex_rule', 'dict_rule'])
for i in tqdm(range(0,len(data)), desc ="Proccessed:"):
    sent = data['original'][i]
    sent_lst = data['input'][i].copy()
    regrex_sent = regrex_rule(sent, sent_lst, rule_list)
    sent_lst = data['input'][i].copy()
    dict_sent= dictionary_rule(sent, sent_lst, dictionary)
    #dict_sent =[word.replace('_', ' ') for element in dict_sent for word in element.split()]
    df.loc[len(df)] = {'original': data['original'][i],
                        'normalized': data['normalized'][i],
                        'input': data['input'][i],
                        'output': data['output'][i],
                        'regrex_rule': regrex_sent,
                        'dict_rule': dict_sent}


#df[:8369].reset_index(drop=True).to_csv("/content/drive/MyDrive/LexNorm/KLTN/Code/astra/data/train.csv")
#df[8370:9412].reset_index(drop=True).to_csv("/content/drive/MyDrive/LexNorm/KLTN/Code/astra/data/test.csv")
#df[9413:].reset_index(drop=True).to_csv("/content/drive/MyDrive/LexNorm/KLTN/Code/astra/data/dev.csv")
