# packages

import ast
import pandas as pd
import numpy as np
import csv
import json
import os
import pickle



# raw dataset
ipcr = pd.read_csv('raw_data/ipcr.tsv', sep='\t')
assignee = pd.read_csv('raw_data/rawassignee.tsv', sep='\t')



#### construction of canincal datasets ####
# assignee_0 = assignee[['patent_id','assignee_id','organization']]

# list of organisation_id/true_name_organization
# assignee_1 = assignee[['assignee_id','organization']]
# assignee_1['organization'] = assignee_1['organization'].str.upper()

# list of  patent_id / organisation_id
# assignee_2 = assignee[['patent_id','assignee_id']]

# ipcr_1 = ipcr[['patent_id','ipc_version_indicator']]

# conversion en date
# ipcr_1['ipc_version_indicator']=pd.to_datetime(ipcr_1['ipc_version_indicator'],format='%Y-%m-%d', errors='ignore')

# filtrage pour enlever les patent qui n'ont pas de date
# ipcr_1= ipcr_1[ipcr_1['ipc_version_indicator']>pd.datetime(1800,1,1)]

# ipcr_1 = ipcr_1.set_index('patent_id')

# filtrage qui permet d'enlever les patents en double
# ipcr_1 = ipcr_1[~ipcr_1.index.duplicated(keep='first')]

#### ---- ####


# canonical datasets
with open("canonique_1.p", "rb") as cano1:
    canonique_1 = pickle.load(cano1)
canonique_1.head()

with open("canonique_2.p", "rb") as cano2:
    canonique_2 = pickle.load(cano2)
canonique_2.head()



# crunchbase import

crunchbase_1 = pd.read_csv("/Volumes/Samsung_T5/patent_similarity_data/CRUNCHBASE_EXPORT/acquisitions_private_hardware_us.csv")



