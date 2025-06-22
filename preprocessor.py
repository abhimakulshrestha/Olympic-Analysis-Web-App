import pandas as pd

def preprocess(df, rdf):
    df = df.merge(rdf, on='NOC', how='left')
    df.drop_duplicates(inplace=True)

    if 'Medal' in df.columns:
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    else:
        print("Warning: 'Medal' column not found in DataFrame!")

    return df
