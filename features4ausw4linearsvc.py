from steps_independent import _body as step_body, _title as step_title
from pathlib import Path
import pandas as pd
# from sk learn import train_test_split
from sklearn.model_selection import train_test_split


# get script dir
script_dir = Path(__file__).parent
# columns: impact,id
data_all_path = str(script_dir / 'output_independent/__all_tickets_step1.csv')
# columns: combinedtks,id
data_combinedtks_path = str(script_dir / 'output_independent/_combinedtks.csv')
# columns: ...
data_business_service_path = str(script_dir / 'output_independent/_business_service.csv')
# columns: ...
data_category_path = str(script_dir / 'output_independent/_category.csv')
# columns: ...
data_sub_category1_path = str(script_dir / 'output_independent/_sub_category1.csv')
# columns: ...
data_sub_category2_path = str(script_dir / 'output_independent/_sub_category2.csv')
# columns: ...
data_ticket_type_path = str(script_dir / 'output_independent/_ticket_type.csv')

data_outpath = str(script_dir / 'output_merged/features4ausw4linearsvc_{}.csv')

def main():
    df_merged = merge()
    df_train, df_test = split(df_merged)
    df_train.to_csv(data_outpath.format('train'), index=False)
    df_test.to_csv(data_outpath.format('test'), index=False)


def merge():
    df_all = pd.read_csv(data_all_path, usecols=['id', 'impact'])
    df_combinedtks = pd.read_csv(data_combinedtks_path)
    df_category = pd.read_csv(data_category_path)
    df_sub_category1 = pd.read_csv(data_sub_category1_path)
    df_sub_category2 = pd.read_csv(data_sub_category2_path)
    df_ticket_type = pd.read_csv(data_ticket_type_path)
    df_business_service = pd.read_csv(data_business_service_path)

    df_merged = pd.merge(df_all, df_combinedtks, on='id')
    df_merged = pd.merge(df_merged, df_category, on='id')
    df_merged = pd.merge(df_merged, df_sub_category1, on='id')
    df_merged = pd.merge(df_merged, df_sub_category2, on='id')
    df_merged = pd.merge(df_merged, df_ticket_type, on='id')
    df_merged = pd.merge(df_merged, df_business_service, on='id')

    return df_merged

def split(df_merged):
    # split with sk learn stratify by impact
    df_train, df_test = train_test_split(df_merged, test_size=0.35, stratify=df_merged['impact'])
    return df_train, df_test


if __name__ == '__main__':
    main()