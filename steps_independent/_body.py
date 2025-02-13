import __init__
from pathlib import Path
import pandas as pd
from modules.text import *
from parallel_pandas import ParallelPandas

#initialize parallel-pandas
ParallelPandas.initialize(n_cpu=10, split_factor=4, disable_pr_bar=True)

# get script dir
script_dir = Path(__file__).parent
# data columns: title,body,ticket_type,category,sub_category1,sub_category2,business_service,urgency,impact
data_path = str(script_dir / '../output_independent/__all_tickets_step1.csv')
data_outpath = str(script_dir / '../output_independent/_body.csv')


def main():
    df = pd.read_csv(data_path)
    df.loc[:, 'body'] = df['body'].apply(clean_body)
    df[['id', 'body']].to_csv(data_outpath, index=False)


def clean_body(text):
    text = expand_contractions(text)
    text = strip_all_entities(text)
    text = filter_chars(text)
    text = remove_mult_spaces(text)
    text = remove_numbers(text)
    text = remove_short_words(text)
    text = replace_elongated_words(text)
    text = remove_repeated_punctuation(text)
    text = remove_extra_whitespace(text)
    text = remove_url_shorteners(text)
    text = remove_short_words(text)
    text = remove_consecutive_word_groups(text)
    text = ' '.join(text.split())  # Remove multiple spaces between words
    return text

if __name__ == '__main__':
    main()