import linktransformer as lt
import pandas as pd

# Load the data
rivals_data = pd.read_csv('data/rivals_data_fuzzy.csv')
siren_data = pd.read_csv('data/siren_database_trimmed.csv')

rivals_data['RIVAL_NAME'] = rivals_data['RIVAL_NAME'].astype(str)
siren_data['RIVAL_NAME'] = siren_data['RIVAL_NAME'].astype(str)

rivals_data['apen2'] = rivals_data['apen2'].fillna(0)
siren_data['apen2'] = siren_data['apen2'].fillna(0)

result_csv_file = 'results/result-1-m.csv'
merged_data = lt.merge(rivals_data, siren_data, merge_type='1:m', on=['RIVAL_NAME']) #, model='dell-research-harvard/lt-wikidata-comp-fr')
merged_data.to_csv(result_csv_file)

print(f"Results put to {result_csv_file}")