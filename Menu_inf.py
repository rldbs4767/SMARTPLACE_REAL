from Basic_inf import *
from selenium.webdriver.common.by import By

# 1인당 평균가격
def average_price(driver):
    price_random = random.randint(1, 7)

    # 평균가격 > 목록 열기
    driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld"]/button[@class="Select_btn_select__tYcKk"]').click()
    time.sleep(1)

    # 평균가격 선택
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div/div/a[' + str(price_random) + ']').click()
    time.sleep(1)

# 메뉴 추가
def add_menu(driver):
    n = 2
    for x in range(n):
        # 메뉴 추가
        driver.find_element(By.XPATH,'//div[@class="Button_btn_group__vjO_z"]/button[@class="btn Button_btn_add__5Xnfi"]').click()
        time.sleep(1)

        # 메뉴명 입력하기
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("메뉴 "+str(x))
        time.sleep(1)

        # 가격 입력하기
        price_random = random.randint(0, 1) #직접 입력할지 변동가격 체크할지,,,

        # 0부터 9까지의 숫자 중 5개 랜덤 선택
        chosen = [str(random.randint(0, 9)) for _ in range(5)]
        # 선택한 숫자들을 하나의 문자열로 만들기
        price = ''.join(chosen)

        #가격 직접 입력
        if price_random == 0:
            driver.find_element(By.XPATH,'//div[@class="Input_root__am964 BusinessDetails_price_form__mNeK0"]/input[@class="Input_common_input__vGI1D"]').send_keys(price)
            time.sleep(1)

        #변동가격 선택
        else:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[4]/div/div[2]/div[1]/div[2]/div[2]/label/i').click()
            time.sleep(1)

        # 메뉴 사진
        driver.find_element(By.XPATH,'//div[@class="modal_layout"]/div/div/div/div[@class="InputImageUpload_root__n5AsO"]').click() # 사진 추가 버튼 클릭
        time.sleep(1)
        fileupload(img_photo())  # 사진파일만 업로드
        time.sleep(2)

        # '추천메뉴' 버튼까지 스크롤 이동
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[4]/div/div[2]/div[1]/div[5]/div/label/span')).perform()

        # 메뉴 설명
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/textarea[@class="Input_common_input__vGI1D Input_textarea__GajFm"]').send_keys("실제 메뉴는 없습니다.")
        time.sleep(1)

        # 추천 메뉴로 등록하기
        recommend_menu_random = random.randint(0, 1)

        #추천메뉴 클릭
        if recommend_menu_random == 0:
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_recommend__A7KKE"]/div/label/span[@class="Checkbox_form_text__jzyJr"]').click()
            time.sleep(1)

        # 추가하기 버튼 클릭하기
        driver.find_element(By.XPATH,'//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

        # '다음' 버튼까지 스크롤 이동
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.XPATH, '//div/div/button[@class="btn Button_btn_green__PyMEj"]')).perform()

# 메뉴 정보 탭
def menuInf(driver):

    #평균 가격 선택
    average_price(driver)

    # 메뉴판 사진 업로드
    photo_uplaod(driver)

    #'다음' 버튼까지 스크롤 이동
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH, '//div/div/button[@class="btn Button_btn_green__PyMEj"]')).perform()

    # 메뉴 추가
    add_menu(driver)


    # 다음 탭으로 이동
    driver.find_element(By.XPATH,'//div/div/button[@class="btn Button_btn_green__PyMEj"]').click()
    time.sleep(2)

    # 얼럿 > 추가정보 입력하기
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/button').click()
    time.sleep(1)
