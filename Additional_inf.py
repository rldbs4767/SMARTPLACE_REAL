from Menu_inf import *

from selenium.webdriver.common.by import By

# 부가서비스 선택하기
def addition_service(driver):
    serivce_num = len(driver.find_elements(By.XPATH,'//div[@class="CheckboxGroup_root__W2EF7 BusinessDetails_additional_service__2DdbO"]/label')) #부가서비스 개수

    n = random.randint(1, serivce_num)
    for x in range(n):
        choice = random.randint(1, serivce_num)

        #부가서비스 선택
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[2]/label[' + str(choice) + ']').click()
        time.sleep(1)

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,'//div[@class="Button_btn_group__vjO_z"]/button[@class="btn Button_btn_add__5Xnfi"]')).perform()  # 추가하기 버튼까지 스크롤로 이동

# 테마 선택하기
def theme(driver):
    theme_num = len(driver.find_elements(By.XPATH,'//div[@class="CheckboxGroup_root__W2EF7 BusinessDetails_additional_theme__IQvEa"]/label'))
    n = random.randint(1, theme_num)
    for x in range(n):
        choice = random.randint(1, theme_num)
        #x테마 선택
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[3]/div[2]/label[' + str(choice) + ']').click() #테마 선택하기
        time.sleep(1)

# 운영중인 홈페이지, SNS, 커뮤니티 선택하기
def contents(driver,category):

    #컨텐츠가 10개임
    contents_num = 9
    print("컨텐츠 선택")
    for x in range(contents_num):
        choice = random.randint(1, contents_num)


        driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld Select_type_small__P97FK"]/button[@class="Select_btn_select__tYcKk"]').click() # '선택' 드롭다운 박스 클릭
        time.sleep(1)

        content = driver.find_element(By.XPATH,'//div[@class="Select_select_list__S5kgz Select_show_scrollbar__IbUJB"]/a[' + str(choice) + ']')
        content.click() #컨텐츠 선택
        time.sleep(1)

        content = driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld Select_type_small__P97FK"]/button[@class="Select_btn_select__tYcKk"]')

        if content.text == "블로그":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div/input[@class="Input_common_input__vGI1D"]').send_keys("nvqa_place13")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "카페":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "모두":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div/input[@class="Input_common_input__vGI1D"]').send_keys("www.naver.com")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "일반":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div/input[@class="Input_common_input__vGI1D"]').send_keys("new.smartplace.naver.com/")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "예약":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "밴드":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div/input[@class="Input_common_input__vGI1D"]').send_keys("nvqa_place13")
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "페이스북":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "인스타그램":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        elif content.text == "유투브":
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        else:
            #스마트스토어
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[3]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 추가하기
            time.sleep(1)

        contents_num -= 1

    if(category in ["호텔","콘도/리조트"]):
        reserve_website(driver)

# 호텔업종 > 예약 웹사이트
def reserve_website(driver):
    website_num = 4
    n = random.randint(1, website_num)
    for x in range(n):
        choice = random.randint(1, website_num)

        driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld"]/button[@class="Select_btn_select__tYcKk"]').click()  # '선택' 드롭다운 박스 클릭
        time.sleep(1)

        website = driver.find_element(By.XPATH,'//div[@class="Select_select_list__S5kgz"]/a[' + str(choice) + ']')
        website.click()  # 웹사이트 선택
        time.sleep(1)

        website = driver.find_element(By.XPATH,'//div[@class="Select_root__3Hhld"]/button[@class="Select_btn_select__tYcKk"]')

        if website.text == "네이버 예약":
            print("웹사이트:네이버 예약")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[3]/button').click()  # 추가하기
            time.sleep(1)

        elif website.text == "웹사이트":
            print("웹사이트:웹사이트")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[2]/input[2]').send_keys("www.hotelscombined.co.kr/")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[3]/button').click()  # 추가하기
            time.sleep(1)

        elif website.text == "여행사":
            print("컨텐츠:여행사")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[2]/input[2]').send_keys("kr.trip.com/")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[3]/button').click()  # 추가하기
            time.sleep(1)

        else:
            print("컨텐츠:직접입력")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[2]/input[2]').send_keys("www.naver.com")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[3]/input[2]').send_keys("네이버")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[4]/div[4]/button').click()  # 추가하기
            time.sleep(1)

        website_num -= 1

# 모텔 > 홍보문구, 노출기간 설정 작성
def promotional_text(driver):
    # 홍보문구 작성
    driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/textarea[@class="Input_common_input__vGI1D Input_textarea__GajFm"]').send_keys("북한강이 보이는 풀빌라 펜션아닙니다~")
    time.sleep(1)

    #노출기간 설정
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click() #설정하기 클릭
    time.sleep(1)
    # default = 항상 노출
    choice = random.randint(0, 1)
    choice = 0
    if choice == 0:
        print("기간 설정")
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/button[2]').click()
        time.sleep(1)

        # 활성화된 날짜 선택하기...힘들었다...
        total_day = driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[@class="Calendar_day__bCrAv"]/td[contains(@class,"Calendar_day__bCrAv")]')
        select_day = []
        for possible_day in total_day:
            if "Calendar_unavailable__TE_F_" not in possible_day.get_attribute('class'):
                print("선택가능한 날짜:", possible_day.text)
                select_day.append(possible_day)

        #두번째 선택한 날짜가 두 번째 날짜보다 커야함
        first_select = -1
        for x in range(2):
            random_select = random.randint(0, len(select_day) - 1)
            while(random_select <= first_select):
                random_select = random.randint(0, len(select_day) - 1)
            print("선택한 날짜:", select_day[random_select].text)
            select_day[random_select].click()
            time.sleep(1)
            select_day.remove(select_day[random_select]) #이미 선택한 날짜는 리스트에서 제외
            first_select = random_select

        # 완료 버튼 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)

    else:
        print("항상 노출")

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,'//div[@class="Button_btn_group__vjO_z"]/button[@class="btn Button_btn_add__5Xnfi"]')).perform()  # 추가하기 버튼까지 스크롤로 이동

# 모텔 > 부가서비스
def motel_addition_service(driver):
    driver.find_element(By.XPATH,'//div[@class="BusinessDetails_contents_row__N81XQ"]/div[2]/button[@class="btn Button_btn_add__5Xnfi"]').click()  # 부가서비스 선택
    time.sleep(1)

    #부대시설
    n = 5
    for x in range(n):
        choice = random.randint(1, 12)
        #x테마 선택
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/label[' + str(choice) + ']').click() #테마 선택하기
        time.sleep(1)

    #주변테마
    n = 5
    for x in range(n):
        choice = random.randint(1, 7)
        # x테마 선택
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/label[' + str(choice) + ']').click()  # 테마 선택하기
        time.sleep(1)

    driver.find_element(By.XPATH,'//div[@class="modal_root undefined"]/div[@class="modal_layout"]/div[@class="Button_btn_group__vjO_z"]/button').click() #확인버튼 클릭
    time.sleep(1)

# 부가 정보
def additionalInf(driver,category):

    """if category == "모텔":
        promotional_text(driver) #모텔 > 홍보문구
        motel_addition_service(driver) #모텔 > 부가서비스
        time.sleep(1)

    if category not in ["모텔"]:
        addition_service(driver) #부가서비스 선택하기

    if category in ["음식점","미용실","네일샵"]:
        theme(driver) #테마 선택하기

    contents(driver,category) #컨텐츠 선택하기"""

    driver.find_element(By.XPATH,'//div/div/button[@class="btn Button_btn_green__PyMEj"]').click() #다음 탭으로 이동
    time.sleep(1)