import pandas as pd

def clean(in1, in2):
    df1 = pd.read_csv(in1)
    df2 = pd.read_csv(in2, converters={'birthdate': lambda x: str(x)})
    df1 = df1.set_index('respondent_id')
    df2 = df2.set_index('respondent_id')
    dfj = df1.join(df2)

    dfj['birthdate'] = pd.to_datetime(dfj['birthdate'], format='%m%d%Y')
    dfj['birthdate'] = dfj['birthdate'].dt.strftime('%Y-%m-%d')
    # dfj['address'] = dfj.address.str.replace('\n',' ')
    # dfj['address'] = dfj.address.str.replace(',','')

    return(dfj)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Pass the path to the "Contact" CSV file')
    parser.add_argument('input2', help='Pass the path to the "Other" CSV file')
    parser.add_argument('output', help='Pass the path for the output file')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output)
