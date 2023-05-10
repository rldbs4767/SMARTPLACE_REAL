import time

from selenium import webdriver
from FileUpload import *
from img_path import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#한글 업체명 입력
def create_company_name(driver,category):
    automation_num = random.randint(0, 100)  # 업체명 번호 랜덤생성
    company_name = category + '(자동화' + str(automation_num) + ')'

    wait = WebDriverWait(driver,5)
    korean_businessName = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div/div[1]/input[2]')))

    # 한글업체명 영역 클릭 후, 기존 업체명 삭제
    korean_businessName.click()
    korean_businessName.send_keys(Keys.CONTROL + "a")
    korean_businessName.send_keys(Keys.BACKSPACE)

    # 한글업체명 입력
    korean_businessName.send_keys(company_name)
    time.sleep(1)

    return company_name

#영문 업체명 입력
def translated_text(company_name):
    # 네이버 파파고에서 영문 업체명 번역해서 가져오기!
    # 드라이버 생성
    driver = webdriver.Chrome()

    # URL 열기
    driver.get("https://papago.naver.com/")
    time.sleep(1)

    # 한글을 영어로 번역하기 위해 한글 업체명 입력
    driver.find_element(By.XPATH,'//*[@id="txtSource"]').send_keys(company_name)
    time.sleep(1)

    # 번역 버튼 클릭
    driver.find_element(By.XPATH,'//*[@id="btnTranslate"]').click()
    time.sleep(1)

    # 영어 번역 결과 가져오기
    target_textarea = driver.find_element(By.XPATH,'//*[@id="txtTarget"]/span').text
    time.sleep(2)
    driver.close()

    print("영문 업체명:", target_textarea)
    return target_textarea

#사업자등록증 외 증빙서류 첨부하기
def additionalFile_upload(driver):
    toast_message_error = 1

    while toast_message_error != 0:
            driver.find_element(By.XPATH, '//div/label[@class="BusinessDetails_file_label__Vte8Y"]').click()
            time.sleep(1)
            fileupload(img())
            time.sleep(1)

            #추가서류 > 비유효파일이 들어간 경우, ex) PDF파일
            try:
                toast_message = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME,'SimpleToast_root__5Ypqn.danger'))
                )
                message = toast_message.text
                print("Toast message 내용: " + message)
                toast_message_error = 1  # 토스트메시지 노출됨

            except:
                toast_message_error = 0
                print("정상적으로 증빙서류 첨부함")

#업체사진 추가
def photo_uplaod(driver):
    photo_upload = driver.find_element(By.XPATH, '//div/label[@class="InputImageUpload_file_input__uICe6"]')
    actions = ActionChains(driver)
    actions.move_to_element(photo_upload).perform() #업체사진 추가 버튼까지 스크롤로 이동
    time.sleep(1)
    photo_upload.click()
    time.sleep(1)
    fileupload(img_photo())  # 사진파일만 업로드
    time.sleep(2)

#상세설명 입력하기
def detail_company_inf(driver):
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[1]/div[5]/div/textarea')).perform()  # 상세설명 입력하는 영역까지 스크롤로 이동
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[1]/div[5]/div/textarea').send_keys("실제로 운영하는 업체가 아닙니다. 감사합니다!@%^&*142")
    time.sleep(1)

#대표키워드 입력하기
def keyword_enter(driver):
    keyword_random = random.randint(0, 4)
    keyword = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[6]/div[2]/div[1]/input[2]')

    actions = ActionChains(driver)
    actions.move_to_element(keyword).perform()  # 대표키워드 입력하는 영역까지 스크롤로 이동
    time.sleep(1)

    if keyword_random == 0:
        print("키워드:막힘")
        keyword.send_keys("막힘")  # 대표키워드 허용
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[6]/div[2]/div[1]/button').click()  # 추가버튼
        time.sleep(1)

    elif keyword_random == 1:
        print("키워드:휴대폰성지")
        keyword.send_keys("휴대폰성지")  # 대표키워드 선검수
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[6]/div[2]/div[1]/button').click()  # 추가버튼
        time.sleep(1)

    elif keyword_random == 2:
        print("키워드:홀덤")
        keyword.send_keys("홀덤")  # 대표키워드 사등확인
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[6]/div[2]/div[1]/button').click()  # 추가버튼
        time.sleep(1)

    elif keyword_random == 3:
        print("키워드:방문서비스")
        keyword.send_keys("방문서비스")  # 대표키워드 서류요청
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[6]/div[2]/div[1]/button').click()  # 추가버튼
        time.sleep(3)

        #앞에서 추가서류나 공식확인 체크가 안되어 있는 경우, 얼럿 노출됨
        if len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div')) != 0:
            print("추가서류나 공식확인체크를 해야함!!")
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH, '//div/label[@class="InputImageUpload_file_input__uICe6"]')).perform()
            driver.find_element(By.XPATH,'//div/button[@class="Modal_btn_confirm__JBzc2"]').click()  # 얼럿 > 확인
            time.sleep(1)
            actions.move_to_element(driver.find_element(By.XPATH, '//div/label[@class="BusinessDetails_file_label__Vte8Y"]')).perform() #사업증등록증 외 증빙서류 영역으로 스크롤 이동
            time.sleep(1)
            additionalFile_upload(driver)
        else:
            print("추가서류제출하거나 공식확인 체크가 이미 되어있음")

    elif keyword_random == 4:
        print("키워드:투표소")
        keyword.send_keys("투표소")  # 대표키워드 불가
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[6]/div[2]/div[1]/button').click()  # 추가버튼
        time.sleep(1)

        #얼럿 노출때까지 대기했다가,,,,확인버튼 클릭
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div/div/button')))
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/div/button').click()  # 얼럿 > 확인
            time.sleep(1)

        except TimeoutException:
            print("타임에러...")

        driver.find_element(By.XPATH, '//div/div/span/button[@class="Tags_btn_close__1rR8j"]').click()  # 대표키워드 삭제
        time.sleep(1)

#전화번호 선택
def select_tel(driver):
    # 0부터 9까지의 숫자 중 8개 랜덤 선택
    chosen = [str(random.randint(0, 9)) for _ in range(8)]

    # 선택한 숫자들을 하나의 문자열로 만들기
    tel_num = ''.join(chosen)

    driver.find_element(By.XPATH,'//div[@class="BusinessDetails_basic_phone__FsjdJ"]/div/div/button[@class="Select_btn_select__tYcKk"]').click()  # 국번 체크박스 선택
    time.sleep(1)
    """
    (1, 18) #02 ~ 064
    (19, 24) #010 ~ 019
    (25, 56) #0303 ~ 1899
    """
    area_code = random.randint(0, 1)

    # 국번 랜덤 선택(02 ~ 064)
    if area_code == 1:
        driver.find_element(By.XPATH,'//div[@class="Select_select_list__S5kgz Select_show_scrollbar__IbUJB"]/a[' + str(random.randint(1, 18)) + ']').click()
        time.sleep(1)

    # 국번 랜덤 선택(0303 ~ 1899)
    else:
        driver.find_element(By.XPATH,'//div[@class="Select_select_list__S5kgz Select_show_scrollbar__IbUJB"]/a[' + str(random.randint(25, 56)) + ']').click()
        time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'Input_common_input__vGI1D.Input_alert__uvdie').send_keys(tel_num)  # 나머지 전화번호 입력
    time.sleep(1)

#주소 입력하기
def address(driver):
    address_region = driver.find_element(By.CLASS_NAME,'BusinessDetails_basic_address_search__gh5iw')
    actions = ActionChains(driver)
    actions.move_to_element(address_region).perform()  # 주소 입력하는 영역까지 스크롤로 이동
    time.sleep(1)
    address_region.click()  # 주소입력
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="brandType"]').send_keys("재원리 산 356")
    time.sleep(1)
    driver.find_element(By.XPATH,'//div/div/div/form/button[@class="BrandSearch_btn_search__8FcGV"]').click()  # 돋보기 클릭
    time.sleep(1)
    driver.find_element(By.XPATH,'//ul/li/label/span[@class="AddressPopup_icon_check__lXr0h"]').click()  # 재원리 356 클릭
    time.sleep(1)
    driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/input[@class="Input_common_input__vGI1D"]').send_keys("가나다라마바사123@")  # 상세주소 입력
    time.sleep(1)
    driver.find_element(By.XPATH,'//div/button[@class="AddressPopup_btn_green__bzq57"]').click()  # 입력하기 클릭
    time.sleep(1)

#업체 위치 확인하기------>추가할 기능이 있음!!!
def check_company_location(driver):

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[8]/strong')).perform()  # 업체위치 확인하는 영역까지 스크롤로 이동
    time.sleep(1)

    # 이 위치가 맞아요
    if random.randint(0, 1) == 0:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[9]/div[3]/label[1]/span').click()
        time.sleep(1)

    # 아니요, 위치가 달라요 ----> 제대로 구현 못함,,,,
    else:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[9]/div[3]/label[2]/span').click()
        time.sleep(1)

        # 현재 위치
        current_location_pin = driver.find_element(By.XPATH,'//*[@id="naver_map_draggable"]/img')

        #위도와 경도 설정
        new_latitude = '300'
        new_longitude = '300'

        print("위치 이동했다!!!!")

        #얼럿 닫기
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[8]/div[3]/div[2]/div/button').click()
        time.sleep(1)

        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[9]/div[3]/label[1]/span').click()
        time.sleep(1)

        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.XPATH,'//div[@class="Input_root__am964"]/textarea[@class="Input_common_input__vGI1D Input_textarea__GajFm"]')).perform()  # 찾아오는길 영역까지 스크롤로 이동

#찾아오는 길 설명하기
def explain_road(driver):
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[10]/div/textarea')).perform()  # 찾아오는 길 설명하는 영역까지 스크롤로 이동
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[10]/div/textarea').send_keys("찾아오는길이 어렵습니다!")
    time.sleep(1)



#기본정보
def basicInf(driver,category):

    #얼럿노출(서류확인이 필요하다, 금지된 단어가 포함되어 있다 등등)
    if len(driver.find_elements(By.XPATH,'//div/div/div[@class="Modal_content__QjAjA"]')) != 0:
        driver.find_element(By.XPATH,'//div/div/div/div/button[@class="Modal_btn_confirm__JBzc2"]').click() #확인버튼
        time.sleep(1)
        print("얼럿 닫음!")

    # 한글 업체명 입력하기
    company_name = create_company_name(driver,category)
    time.sleep(1)

    # 업체명에 서류가 필요한 단어가 포함일 떄, 노출되는 얼럿에 대한 구현
    if len(driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div')) != 0:
        print("얼럿 확인함!")
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div/div/button').click()
        time.sleep(1)
        additionalFile_upload(driver)

        actions = ActionChains(driver)
        actions.move_to_element(driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div/div[2]/input[2]')).perform()  #영어 업체명 입력하는 영역까지 스크롤로 이동

    # 영어 업체명 입력하기
    english_company_name = translated_text(company_name)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[1]/div[2]/div/div[2]/input[2]').send_keys(english_company_name)
    time.sleep(1)


    #사업자등록증 외 증빙서류 첨부하기
    print("서류첨부영역 노출여부: ",bool(driver.find_elements(By.CLASS_NAME,'BusinessDetails_basic_document__Nv9Ch')))
    if driver.find_elements(By.CLASS_NAME,'BusinessDetails_basic_document__Nv9Ch'):
        print("사업자등록증 외 증빙서류 첨부해보자!")
        additionalFile_upload(driver)

    # 업체 사진 추가하기
    photo_uplaod(driver)

    # 상세설명 입력하기
    detail_company_inf(driver)

    # 대표키워드 입력하기
    keyword_enter(driver)

    #전화번호 입력하기
     #select_tel(driver)

    #주소 입력하기
    address(driver)

    #우리 업체 위치 확인하기 ---> 아니요, 위치가 달라요도 구현해야함,,,,
    check_company_location(driver)

    #찾아오는 길 설명하기
    explain_road(driver)


    driver.find_element(By.XPATH,'//div/div/button[@class="btn Button_btn_green__PyMEj"]').click() #다음 탭으로 이동
    time.sleep(1)

    if len(driver.find_elements(By.XPATH,'//div[@class="Modal_root__CTV01"]/div/div[@class="Modal_title__R0DrL"]')) != 0:
        print("지역번호가 달라요~")
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div[2]/button[2]').click() #얼럿 > 계속
        time.sleep(1)

    #1. 스마트콜을 사용할 때, 약관동의가 노출됨
    if driver.find_element(By.XPATH,'//div/div/label/input[@class="blind CheckboxSwitch_input__Id_wr"]').is_selected():
        print("스마트콜 동의받자!")
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[2]/button').click() #약관동의 > 동의하기

    print("다음 정보 입력하자...")
    time.sleep(8)  # 로딩 시간이 걸림

    if category == "음식점":
        print("메뉴정보 입력하자!")
    else:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div[2]/button').click() #얼럿 > 추가정보 입력하기
        time.sleep(1)