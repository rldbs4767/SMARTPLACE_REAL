import time

from Menu_inf import *

#스타일리스트 추가
def stylist(driver):
    for x in range(2):
        #스타일리스트 추가
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click()
        time.sleep(1)

        #스타일리스트명 입력
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[1]/div/input[2]').send_keys("스타일리스트 " + str(x))
        time.sleep(1)


        #직책 선택
        position = random.randint(1, 9)
        driver.find_element(By.XPATH,'//div[1]/div/button[@class="Select_btn_select__tYcKk"]').click() #목록 선택
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/a[' + str(position) + ']').click() #직책 선택
        time.sleep(1)

        #성별 선택
        driver.find_element(By.XPATH,'//div[2]/div/button[@class="Select_btn_select__tYcKk"]').click() #목록 선택
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/a[' + str(random.randint(1, 2)) + ']').click() #성별 선택
        time.sleep(1)

        #직급 입력 > 직책 > 기타인 경우,
        if position == 9:
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_stylist_position_etc__wQ_y4"]/div/input[@class="Input_common_input__vGI1D"]').send_keys("매니저")
            time.sleep(1)

        #스타일리스트 사진 업로드
        driver.find_element(By.XPATH,'//div[@class="BusinessDetails_file_input_form___C3Pv"]/div/label[@class="InputImageUpload_file_input__uICe6"]').click()  # 사진 추가 클릭
        time.sleep(1)
        fileupload(img_photo())  # 사진파일만 업로드
        time.sleep(1)

        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[2]/button[2]')).perform()  # 업체사진 추가 버튼까지 스크롤로 이동

        #강점 및 소개
        driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_row__vdTNq"]/div/textarea[@class="Input_common_input__vGI1D Input_textarea__GajFm"]').send_keys("스타일리스트의 강점은 없습니다. 감사합니다!")
        time.sleep(1)

        #대표 URL
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[5]/div/input[2]').send_keys("http://www.naver.com/"+str(x))
        time.sleep(1)

        #추가하기 버튼 클릭
        driver.find_element(By.XPATH, '//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

#네일샵 > 시술정보 추가
def addtion_surgery_inf_nail(driver):
    for x in range(2):
        # 시술정보 추가
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click()
        time.sleep(1)

        # 스타일명 입력
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("스타일 " + str(x))
        time.sleep(1)

        # 시술 카테고리
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/button').click()
        time.sleep(1)

        surgery_category = random.randint(1, 3)

        # 카테고리 선택
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div/a[' + str(surgery_category) + ']').click()
        time.sleep(1)

        #종류, 추가선택
        if surgery_category == 1 or surgery_category == 2:
            #종류
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div/div/label[' + str(random.randint(1, 11)) + ']/span').click()
            time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[2]/button[2]')).perform()

            #색상
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div[2]/button').click()
            time.sleep(1)
            for x in range(2):
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/ul/li[' + str(random.randint(2, 23)) + ']/label/span').click()
                time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div[3]/button')).perform()

            #디자인
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div[3]/button').click()
            time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div[3]/div/ul/li[16]/label/span')).perform()
            for x in range(6):
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[4]/div[3]/div/ul/li[' + str(random.randint(2, 16)) + ']/label/span').click()
                time.sleep(1)

        elif surgery_category == 3:
            #종류
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div/div/label[' + str(random.randint(1, 2)) + ']/span').click()
            time.sleep(1)

        #시술 사진
        for x in range(2):
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_row__vdTNq"]/div/div/label[@class="InputImageUpload_file_input__uICe6"]').click()  # 사진 추가 클릭
            time.sleep(1)
            fileupload(img_photo())  # 사진파일만 업로드
            time.sleep(1)

        #추가하기 버튼 클릭
        driver.find_element(By.XPATH, '//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

#미용실 > 시술정보 추가
def addtion_surgery_inf_hair(driver):
    for x in range(2):
        # 시술정보 추가
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[2]/button').click()
        time.sleep(1)

        # 스타일명 입력
        driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("스타일리스트 " + str(x))
        time.sleep(1)

        #시술 카테고리
        surgery_category = random.randint(1, 5)

         #카테고리 선택
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[1]/div/label[' + str(surgery_category) + ']/span').click()
        time.sleep(1)


         #남여기장 선택
        choose_sex = random.randint(0, 1)
        if choose_sex == 0:
            #드롭다운 박스 클릭
            driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld Select_type_small__P97FK"]/button').click()
            time.sleep(1)

            #남성 선택
            driver.find_element(By.XPATH,'//div[@class="Select_select_list__S5kgz"]/a[@class="Select_item__J07Z3"]').click()
            time.sleep(1)

            #기장 선택
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[2]/label[' + str(random.randint(1, 3)) + ']').click()
            time.sleep(1)

            #default 값이 여성
        else:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[2]/label[' + str(random.randint(1, 4)) + ']').click()
            time.sleep(1)

        # 선택한 카테고리에 따른 선택케이스 추가하기...
        if surgery_category == 1:
            print("컷 선택하기")
            #컷
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/button').click()
            time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[13]/label/span')).perform()
            #남자 2~19
            if choose_sex == 0:
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[' + str(random.randint(2, 19)) + ']/label/span').click()
                time.sleep(1)
            #여자 2~21
            elif choose_sex == 1:
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[' + str(random.randint(2, 21)) + ']/label/span').click()
                time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[3]/button')).perform()

            #펌
            print("펌 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[3]/button').click()
            time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/ul/li[16]/label/span')).perform()
            # 남자 2~22
            if choose_sex == 0:
                for x in range(2):
                    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/ul/li[' + str(random.randint(2, 22)) + ']/label/span').click()
                    time.sleep(1)
            # 여자 2~21
            elif choose_sex == 1:
                for x in range(2):
                    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[3]/div/ul/li[' + str(random.randint(2, 21)) + ']/label/span').click()
                    time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[4]/button')).perform()

            #염색
            print("염색 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[4]/button').click()
            time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/ul/li[23]/label/span')).perform()
            for x in range(2):
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[4]/div/ul/li[' + str(random.randint(2, 41)) + ']/label/span').click()
                time.sleep(1)
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[5]/button')).perform()

            #스타일링 4개 2~5
            print("스타일링 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[5]/button').click()
            time.sleep(1)
            for x in range(2):
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[5]/div/ul/li[' + str(random.randint(2, 5)) + ']/label/span').click()
                time.sleep(1)

        elif surgery_category == 2:
            # 스타일링 4개
            print("스타일링 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[' + str(random.randint(2, 5)) + ']/label/span').click()
            time.sleep(1)

        elif surgery_category == 3:
            # 스타일링 4개
            print("스타일링 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[' + str(random.randint(2, 5)) + ']/label/span').click()
            time.sleep(1)

        elif surgery_category == 4:
            # 스타일링 4개
            print("스타일링 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[' + str(random.randint(2, 5)) + ']/label/span').click()
            time.sleep(1)

        else:
            #스타일링 6개
            print("스타일링 선택하기")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/ul/li[' + str(random.randint(2, 7)) + ']/label/span').click()
            time.sleep(1)

        #시술 사진
        for x in range(2):
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[3]/div/div[1]/label').click()  # 사진 추가 클릭
            time.sleep(1)
            fileupload(img_photo())  # 사진파일만 업로드
            time.sleep(1)

        #스타일이 어울리는 얼굴/헤어 정보
        for x in range(6):
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[4]/div/label[' + str(random.randint(1, 11)) + ']').click()
            time.sleep(1)

        #담당 스타일리스트
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[5]/div/button').click()
        time.sleep(1)

        #스타일리스트 선택하기
        stylist_num = len(driver.find_elements(By.XPATH,'//div[@class="Select_root__3Hhld Select_type_small__P97FK"]/div/a[@class="Select_item__J07Z3"]'))
        if stylist_num != 0:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div[5]/div/div/a[' + str(random.randint(1, stylist_num)) + ']').click()
            time.sleep(1)

        #스타일 팁 & 추천 코멘트
        driver.find_element(By.XPATH,'//div[@class="BusinessDetails_modal_row__vdTNq"]/div/textarea[@class="Input_common_input__vGI1D Input_textarea__GajFm"]').send_keys("스타일 팁은 없습니다. 감사합니다!")
        time.sleep(1)

        # 추가하기 버튼 클릭
        driver.find_element(By.XPATH, '//div[@class="modal_footer"]/button[@class="btn_green "]').click()
        time.sleep(1)

#기장에 따른 추가 요금 입력
def addition_price(driver):
    if random.randint(0, 1) == 1:
        print("기장추가 요금 있음")
        driver.find_element(By.XPATH,'//div[@class="BusinessDetails_switch_checkbox__eeWqT"]/div/div/label/span').click() #기장 추가 요금 있음
        time.sleep(1)

        #어깨아래 요금 입력
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[2]/div[1]/div/input').send_keys("20000")
        time.sleep(1)

        #가슴아래 요금 입력
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/div/input').send_keys("30000")
        time.sleep(1)
    else:
        print("기장 추가 요금 없음 ")

#시술 정보
def surgeryInf(driver,category):
    if category in ["미용실"]:
        stylist(driver)
        addtion_surgery_inf_hair(driver)
        addition_price(driver)

    #네일샵
    else:
        addtion_surgery_inf_nail(driver)

    # 다음 탭으로 이동
    driver.find_element(By.XPATH, '//div/div/button[@class="btn Button_btn_green__PyMEj"]').click()
    time.sleep(1)
