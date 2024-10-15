import time
import pandas as pd

from login import login
from comments import comment_a_lot


def main():
    df_account = pd.read_csv(r'./data/accounts.csv')

    df_posts = pd.read_csv(r"./data/posts.csv", encoding='utf-8')

    df_comments = pd.read_csv(r'./data/comments.csv', encoding='utf-8')

    index_acc = 2
    
    start_posts = 44
    end_posts = df_posts.shape[0]

    for i in range(df_account.shape[0]):
        if i == index_acc:
            driver = login(
                        email=df_account["Email"][i],
                        password=df_account['Password'][i])

            driver = comment_a_lot(driver=driver,
                                   df_posts=df_posts,
                                   df_comments=df_comments,
                                   start=start_posts,
                                   end=end_posts)


    time.sleep(10)


if __name__ == '__main__':
    main()




