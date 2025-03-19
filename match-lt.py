import linktransformer as lt
import pandas as pd
import os

# Load the data
rivals_data = pd.read_csv(os.path.join('data_test', 'rivals_data_fuzzy_test.csv'))
siren_data = pd.read_csv(os.path.join('data', 'siren_database.csv'))

rivals_data['RIVAL_NAME'] = rivals_data['RIVAL_NAME'].astype(str)
siren_data['RIVAL_NAME'] = siren_data['RIVAL_NAME'].astype(str)

rivals_data['apen2'] = rivals_data['apen2'].fillna(0)
siren_data['apen2'] = siren_data['apen2'].fillna(0)

merged_data = lt.merge(rivals_data, siren_data, merge_type='1:1', on=['RIVAL_NAME']) #, model='dell-research-harvard/lt-wikidata-comp-fr')
merged_data.to_csv('results_test/result-1-1-test.csv')

print("Success")