import time

from Price_inf import *

#객실정보 추가
def additon_room_inf(driver):
    for x in range(2):
        # 객실 추가
        driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div/button[@class="btn Button_btn_add__5Xnfi"]').click()
        time.sleep(1)

        # 객실명
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("객실 " + str(x))
        time.sleep(1)

        #객실 소개
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/textarea[@class="Input_common_input__vGI1D Input_textarea__GajFm"]').send_keys("창 밖으로 동해 바다가 보이지 않는 방입니다.")
        time.sleep(1)

        #객실 사진
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div[1]/label').click()
        time.sleep(1)
        fileupload(img_photo())
        time.sleep(1)

        #객실 시설
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div/label[' + str(random.randint(1,12)) + ']/span').click()
        time.sleep(1)

        #객실 서비스
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[5]/div/label[' + str(random.randint(1,24)) + ']/span').click()
        time.sleep(1)

        #인원정보
         #기준인원
        num1 = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[6]/div/div[1]/div[2]/input')
        num1.clear()
        time.sleep(1)
        num1.send_keys("2")
        time.sleep(1)

         #최대인원
        num2 = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[6]/div/div[2]/div[2]/input')
        num2.clear()
        time.sleep(1)
        num2.send_keys("4")
        time.sleep(1)

        #가격정보
        for tr in range(1,4):
            for td in range(1,4):
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[7]/table/tbody/tr['+str(tr)+']/td['+str(td)+']/div/input').send_keys("100,000")
                time.sleep(1)

        # 추가하기 버튼 클릭
        driver.find_element(By.XPATH, '//div/div[@class="modal_layout"]/div/button[@class="btn Button_btn_green__PyMEj"]').click()
        time.sleep(1)

#상세입력 입력
def detail(driver):
    #객실정보 상세입력 버튼 클릭
    driver.find_element(By.XPATH,'//div[@class="CheckboxGroup_root__W2EF7 CheckboxGroup_inactive___o_3E"]/label[1]/span').click()
    time.sleep(1)

    #객실 추가
    additon_room_inf(driver)

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[5]/strong')).perform()

    #입퇴실 시간 입력
    #입실
    #시각입력
    driver.find_element(By.XPATH,'//div[@class="BusinessDetails_room_check__dteo7"]/div[1]/div/div[1]/button[@class="BusinessDetails_select_button__FlnH4"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//div/ul[@class="BusinessDetails_select_options__UOiSw"]/li[' + str(random.randint(1,24)) + ']').click()
    time.sleep(1)
    #분 입력
    driver.find_element(By.XPATH,'//div[@class="BusinessDetails_room_check__dteo7"]/div[1]/div/div[2]/button[@class="BusinessDetails_select_button__FlnH4"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div/ul[@class="BusinessDetails_select_options__UOiSw"]/li[' + str(random.randint(1, 6)) + ']').click()
    time.sleep(1)

    #퇴실
    #시각입력
    driver.find_element(By.XPATH,'//div[@class="BusinessDetails_room_check__dteo7"]/div[2]/div/div[1]/button[@class="BusinessDetails_select_button__FlnH4"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//div/ul[@class="BusinessDetails_select_options__UOiSw"]/li[' + str(random.randint(1,24)) + ']').click()
    time.sleep(1)
    #분 입력
    driver.find_element(By.XPATH, '//div[@class="BusinessDetails_room_check__dteo7"]/div[2]/div/div[2]/button[@class="BusinessDetails_select_button__FlnH4"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div/ul[@class="BusinessDetails_select_options__UOiSw"]/li[' + str(random.randint(1, 6)) + ']').click()
    time.sleep(1)

    #준성수기, 성수기 요금정보 입력
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div/textarea').send_keys("준성수기는 7월 14일 ~ 7월 20일 / 8월 1일 ~ 8월 10일 이며, 성수기는 7월 21일 ~ 7월 31일 입니다.")
    time.sleep(1)

    #숙박 이용시 발생하는 추가요금 정보 입력
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[5]/div/textarea').send_keys("추가인원 요금 안내 : 성인(8세 이상) 2만원, 유아 (24개월 이상~7세 미만) 1만원입니다. 바베큐장 이용 요금 : 4인 기준 2만원 (숯, 그릴 제공)")
    time.sleep(1)

#간단하게 입력
def simple(driver):
    #간단하게 입력 버튼 클릭
    driver.find_element(By.XPATH,'//div[@class="CheckboxGroup_root__W2EF7 CheckboxGroup_inactive___o_3E"]/label[2]/span').click()
    time.sleep(1)

    #가격표 사진 추가
    photo_price(driver)

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,'//div/div/button[@class="btn Button_btn_green__PyMEj"]')).perform()

    #가격정보 추가
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
        driver.find_element(By.XPATH, '//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

def roomInf(driver):
    # 상세입력 or 간단하게 입력
    '''if random.randint(0, 1) == 0:
        #상세하게
        print("상세입력")
        detail(driver)
    else:
        #간단하게
        print("간단히 입력")
        simple(driver)'''

     #자세히 > 클릭(추후 구현)

    driver.find_element(By.XPATH, '//div/div/button[@class="btn Button_btn_green__PyMEj"]').click()  # 다음 탭으로 이동
    time.sleep(1)
