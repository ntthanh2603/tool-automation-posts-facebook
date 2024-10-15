import random
import pyautogui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pyperclip


def addImage(path_image):
    pyautogui.typewrite(path_image)

    pyautogui.press('enter')

def add_img_on_post(driver, xpath, path_image):
    button = driver.find_element(By.XPATH, xpath)

    time.sleep(random.randint(1, 2))

    button.click()

    time.sleep(random.randint(1, 2))

    addImage(path_image)

    time.sleep(random.randint(2, 3))

    return driver


def posts(driver, link, content, name_gr):
    driver.get(link)

    time.sleep(random.randint(1, 2))

    # Nhấn vào đăng bài
    try:
        button1 = driver.find_element(By.XPATH, '//*[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
        button1.click()
    except NoSuchElementException:
        print(f"Group posting failed: \n    - Name Group: {name_gr}. \n    - URL: {link}.")
        return driver

    # Nhập nội dung
    time.sleep(random.randint(3, 5))
    button2 = driver.find_element(By.XPATH, '//*[@class="_1mf _1mj"]')
    time.sleep(random.randint(1, 2))
    button2.send_keys(content)

    # Nhấn vào chỗ ảnh video
    time.sleep(random.randint(1, 2))
    button3 = driver.find_element(By.XPATH, '//*[@aria-label="Ảnh/video"]')
    time.sleep(random.randint(1, 2))
    button3.click()

    driver = add_img_on_post(driver, '//*[@class="x1n2onr6 x1ja2u2z x9f619 x78zum5 xdt5ytf x2lah0s x193iq5w x5yr21d"]',
                      r"G:\post_facebook\data\images\1.1.jpg")

    driver = add_img_on_post(driver, '//*[@aria-label="Thêm ảnh/video"]',
                      r"G:\post_facebook\data\images\2.1.jpg")

    driver = add_img_on_post(driver, '//*[@aria-label="Thêm ảnh/video"]',
                      r"G:\post_facebook\data\images\3.2.jpg")

    # Nhấn đăng
    time.sleep(random.randint(1, 2))
    button4 = driver.find_element(By.CSS_SELECTOR, '[aria-label="Đăng"]')
    time.sleep(random.randint(1, 2))
    button4.click()

    # Đăng thành công
    print(f"Posted on the group: \n    - Name group: {name_gr}. \n    - URL: {link}.")

    time.sleep(random.randint(8,10))

    # button5 = driver.find_element(By.XPATH, '//*[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xg83lxy x1h0ha7o x10b6aqq x1yrsyyn"')
    # time.sleep(random.randint(1, 2))
    # button5.click()
    # time.sleep(random.randint(1, 2))
    # copied_text = pyperclip.paste()
    #
    # # In nội dung ra terminal
    # print("Link đã sao chép:", copied_text)


    return driver


def post_a_lot(driver, df_gr, df_ct, start, end):
    len_df_gr = df_gr.shape[0]
    len_df_ct = df_ct.shape[0]

    for i in range(start, end):
        print(f'<------> Posts Group {i} <------->')
        driver = posts(driver=driver,
                      link=df_gr['Link group'][i],
                      content=df_ct["Content"][random.randint(0,df_ct.shape[0]-1)],
                      name_gr=df_gr["Name group"][i])

    return driver


