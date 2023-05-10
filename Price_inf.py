from Menu_inf import *

#가격표 사진 추가
def photo_price(driver):

    for x in range(2):
        driver.find_element(By.XPATH,'//div[@class="BusinessDetails_file_input_form___C3Pv"]/div[@class="InputImageUpload_root__n5AsO"]/label[@class="InputImageUpload_file_input__uICe6"]').click() #사진 추가 클릭
        time.sleep(1)
        fileupload(img_photo())  # 사진파일만 업로드
        time.sleep(1)

#시술 가격 추가 > 미용실,네일샵
def surgery_price(driver):
    for x in range(2):
        driver.find_element(By.XPATH,'//div[@class="Button_btn_group__vjO_z"]/button[@class="btn Button_btn_add__5Xnfi"]').click() #시술 가격 추가
        time.sleep(1)

        # 메뉴명 입력하기
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("시술 " + str(x))
        time.sleep(1)

        #시술 카테고리 펼침
        driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld"]/button[@class="Select_btn_select__tYcKk"]').click()
        time.sleep(1)

        #시술 카테고리 선택
        surgery_category = len(driver.find_elements(By.XPATH, '//div[@class="Select_select_list__S5kgz"]/a[@class="Select_item__J07Z3"]'))
        category = random.randint(1, surgery_category)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div/div/a[' + str(category) + ']').click()
        time.sleep(1)

        #가격
        price_random = random.randint(0, 1)  # 직접 입력할지 변동가격 체크할지,,,

        # 0부터 9까지의 숫자 중 5개 랜덤 선택
        chosen = [str(random.randint(0, 9)) for _ in range(5)]
        # 선택한 숫자들을 하나의 문자열로 만들기
        price = ''.join(chosen)

        # 가격 직접 입력
        if price_random == 0:
            driver.find_element(By.XPATH,'//div[@class="Input_root__am964 BusinessDetails_price_form__mNeK0"]/input[@class="Input_common_input__vGI1D"]').send_keys(price)
            time.sleep(1)

        # 변동가격 선택
        else:
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_row__vdTNq"]/div/label/i[@class="Checkbox_state_icon__jY3M3"]').click()
            time.sleep(1)

        #추천 시술로 등록하기
        if random.randint(0, 1) == 1:
            print("추천 시술로 등록함")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_recommend__A7KKE"]/div/label/span[@class="Checkbox_form_text__jzyJr"]').click()
            time.sleep(1)
        else:
            print("추천 시술아님")

        #추가하기 버튼 클릭
        driver.find_element(By.XPATH,'//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

#숙박 가격 추가 > 호텔, 콘도/리조트
def lodgment_price(driver):
    for x in range(2):
        driver.find_element(By.XPATH,'//div[@class="Button_btn_group__vjO_z"]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 숙박 가격 추가
        time.sleep(1)

        # 숙소명 입력하기
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("숙소 " + str(x))
        time.sleep(1)

        # 가격
        price_random = random.randint(0, 1)  # 직접 입력할지 변동가격 체크할지,,,

        # 0부터 9까지의 숫자 중 5개 랜덤 선택
        chosen = [str(random.randint(0, 9)) for _ in range(5)]
        # 선택한 숫자들을 하나의 문자열로 만들기
        price = ''.join(chosen)

        # 가격 직접 입력
        if price_random == 0:
            driver.find_element(By.XPATH,'//div[@class="Input_root__am964 BusinessDetails_price_form__mNeK0"]/input[@class="Input_common_input__vGI1D"]').send_keys(price)
            time.sleep(1)

        # 변동가격 선택
        else:
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_row__vdTNq"]/div/label/i[@class="Checkbox_state_icon__jY3M3"]').click()
            time.sleep(1)


        # 숙소 사진 업로드
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[3]/div/div[1]/label').click()
        time.sleep(1)
        fileupload(img_photo())
        time.sleep(1)

        # 추천 숙소로 등록하기
        if random.randint(0, 1) == 1:
            print("추천 숙소로 등록함")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_recommend__A7KKE"]/div/label/span[@class="Checkbox_form_text__jzyJr"]').click()
            time.sleep(1)
        else:
            print("추천 숙소아님")

        # 추가하기 버튼 클릭
        driver.find_element(By.XPATH,'//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

#일반적인 경우, 병원,마트 등등
def nomal_price(driver):
    for x in range(2):
        driver.find_element(By.XPATH,'//div[@class="Button_btn_group__vjO_z"]/button[@class="btn Button_btn_add__5Xnfi"]').click() #시술 가격 추가
        time.sleep(1)

        # 메뉴명 입력하기
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("상품 " + str(x))
        time.sleep(1)

        # 가격
        price_random = random.randint(0, 1)  # 직접 입력할지 변동가격 체크할지,,,

        # 0부터 9까지의 숫자 중 5개 랜덤 선택
        chosen = [str(random.randint(0, 9)) for _ in range(5)]
        # 선택한 숫자들을 하나의 문자열로 만들기
        price = ''.join(chosen)

        # 가격 직접 입력
        if price_random == 0:
            driver.find_element(By.XPATH,'//div[@class="Input_root__am964 BusinessDetails_price_form__mNeK0"]/input[@class="Input_common_input__vGI1D"]').send_keys(
                price)
            time.sleep(1)

        # 변동가격 선택
        else:
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_row__vdTNq"]/div/label/i[@class="Checkbox_state_icon__jY3M3"]').click()
            time.sleep(1)

        #상품 사진 추가
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[3]/div/div[1]/label').click()
        time.sleep(1)
        fileupload(img_photo())
        time.sleep(1)

        # 추천 시술로 등록하기
        if random.randint(0, 1) == 1:
            print("추천 시술로 등록함")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_recommend__A7KKE"]/div/label/span[@class="Checkbox_form_text__jzyJr"]').click()
            time.sleep(1)
        else:
            print("추천 시술아님")

        # 추가하기 버튼 클릭
        driver.find_element(By.XPATH, '//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)


#가격정보
def priceInf(driver,category):
    """photo_price(driver)

    if category in ["호텔","콘도/리조트"]:
        lodgment_price(driver)

    elif category in ["미용실","네일샵"]:
        surgery_price(driver)

    else:
        nomal_price(driver)"""

    # 다음 탭으로 이동
    driver.find_element(By.XPATH, '//div/div/button[@class="btn Button_btn_green__PyMEj"]').click()
    time.sleep(1)
