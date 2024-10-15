import random
import pyautogui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def addImage(path_image):
    pyautogui.typewrite(path_image)

    pyautogui.press('enter')

def comment(driver, url, content, path_img, name_gr):

    try:
        button1 = driver.find_element(By.XPATH, '//*[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate"]')
    except NoSuchElementException:
        time.sleep(random.randint(1, 2))
        print(f'Comment failed: \n    -Name group: {name_gr}. \n    -URL: {url}.')
        return driver
    # button1.click()

    button1.send_keys(content)
    time.sleep(random.randint(2, 3))

    # button2 = driver.find_element(By.XPATH, '//*[@aria-label="Đính kèm một ảnh hoặc video"]')
    # time.sleep(random.randint(1, 2))
    #
    # button2.click()
    # time.sleep(random.randint(1, 2))
    #
    # addImage(path_img)
    # time.sleep(random.randint(3,5))


    button = driver.find_element(By.XPATH, '//*[@aria-label="Bình luận"]')
    time.sleep(random.randint(1, 2))
    button.click()
    time.sleep(random.randint(1, 2))

    print(f'Posted successfully: \n    -Name Group: {name_gr}. \n    -URL: {url}.\n    -Content: {content}.')

    return driver



def comment_a_lot(driver, df_posts, df_comments, start, end):

    for i in range(start, end):
        driver.get(df_posts['Link posts'][i])
        time.sleep(random.randint(3, 5))

        print(f'<<-------->> Comments posts {i} <<------->>')
        cnt = [random.randint(0, df_comments.shape[0] - 1) for j in range(2)]

        for j in cnt:
            driver = comment(driver=driver,
                             url=df_posts["Link posts"][i],
                             content=df_comments["Content"][j],
                             path_img=df_comments["Path_img"][j],
                             name_gr=df_posts["Name group"][i])

    return driver







