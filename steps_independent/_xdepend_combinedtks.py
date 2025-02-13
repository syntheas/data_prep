import __init__
from pathlib import Path
import pandas as pd
from modules.text import *
from parallel_pandas import ParallelPandas

#initialize parallel-pandas
ParallelPandas.initialize(n_cpu=10, split_factor=4, disable_pr_bar=True)


# get script dir
script_dir = Path(__file__).parent
# data columns: title,title,ticket_type,category,sub_category1,sub_category2,business_service,urgency,impact
data_body_path = str(script_dir / '../output_independent/_body.csv')
data_title_path = str(script_dir / '../output_independent/_title.csv')
data_outpath = str(script_dir / '../output_independent/_combinedtks.csv')


# depends on _body.py and _title.py
def main():
    df_body = pd.read_csv(data_body_path)
    df_title = pd.read_csv(data_title_path)
    # fill nan values with empty string
    df_body.fillna('', inplace=True)
    df_title.fillna('', inplace=True)
    # combine body and title tks to one string
    df_res = pd.DataFrame()
    df_res['id'] = df_body['id']
    df_res['combined_tks'] = df_title['title'] + ' ' + df_body['body']
    # clean combined tks
    df_res['combined_tks'] = df_res['combined_tks'].apply(clean_combinedtks)
    df_res.to_csv(data_outpath, index=False)


def clean_combinedtks(text):
    text = remove_consecutive_word_groups(text)
    text = ' '.join(text.split())  # Remove multiple spaces between words
    return text


if __name__ == '__main__':
    main()