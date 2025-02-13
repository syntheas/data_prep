import __init__
from pathlib import Path
import pandas as pd

# get script dir
script_dir = Path(__file__).parent
# data columns: title,body,ticket_type,category,sub_category1,sub_category2,business_service,urgency,impact
data_path = str(script_dir / '../input/all_tickets.csv')
data_outpath = str(script_dir / '../output_independent/__all_tickets_step1.csv')


def main():
    df = pd.read_csv(data_path)
    # add id column
    df['id'] = df.index
    # save to file
    df.to_csv(data_outpath, index=False)


if __name__ == '__main__':
    main()
    

