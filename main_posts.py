import time
import pandas as pd

from login import login
from posting import post_a_lot


def main():
    df_account = pd.read_csv(r'./data/accounts.csv')

    df_group = pd.read_csv(r"./data/groups.csv", encoding='utf-8')

    df_content = pd.read_csv(r'./data/contents.csv', encoding='utf-8')

    index_acc = 10
    start_gr = 10
    end_gr = df_group.shape[0]


    for i in range(len(df_account)):
        if index_acc == i:
            driver = login(
                        email=df_account["Email"][i],
                        password=df_account['Password'][i])

            driver = post_a_lot(
                        driver=driver,
                        df_gr=df_group,
                        df_ct=df_content,
                        start=start_gr,
                        end=end_gr)




if __name__ == '__main__':
    main()




