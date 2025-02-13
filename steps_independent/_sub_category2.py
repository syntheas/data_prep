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
data_path = str(script_dir / '../output_independent/__all_tickets_step1.csv')
data_outpath = str(script_dir / '../output_independent/_sub_category2.csv')


def main():
    df = pd.read_csv(data_path, usecols=['sub_category2', 'id'])
    # one hot encode sub_category2
    df = pd.get_dummies(df, columns=['sub_category2'], prefix='sub_category2')
    # drop one sub_category2 column because it is redundant (sub_category2_28 beacause has one of least number of tickets)
    df.drop(columns=['sub_category2_28'], inplace=True)
    df.to_csv(data_outpath, index=False)


if __name__ == '__main__':
    main()