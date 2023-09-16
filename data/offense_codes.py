import pandas as pd
import csv

def get_bad_offense_codes():
    df = pd.read_excel('data/all_offense_codes.xlsx')
    codelist = df['CODE'].tolist()
    offense = df['NAME'].tolist()
    code_list_new = []
    offenselist_new = []

    for elt in offense:
        if pd.isna(elt) == False:
            offenselist_new.append(elt)

    for elt in codelist:
        if pd.isna(elt) == False:
            code_list_new.append(elt)

    # convert the list of key-value pairs to a dictionary
    bad_offenses = dict(zip(code_list_new, offenselist_new))
    return bad_offenses

def get_crimes():
    bad_offenses = get_bad_offense_codes()
    csv_name = 'data/2023BostonCrime.csv'
    with open(csv_name, 'r', newline = '') as file:
        reader = csv.reader(file)
        crimes = {}
        for i,row in enumerate(reader):
            if not i:
                continue
            code, description = int(row[1]), row[3]
            if not description or code not in bad_offenses:
                continue
            if code not in crimes:
                crimes[code] = description
    return crimes