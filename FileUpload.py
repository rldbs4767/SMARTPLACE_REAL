import time
import autoit

import random
from img_path import *
from selenium.webdriver.common.keys import Keys
from autoit import AutoItError
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#파일 업로드 함수
def fileupload(img):
    handle = "[CLASS:#32770; TITLE:열기]"
    autoit.win_wait_active("열기", 10)
    time.sleep(1)
    autoit.control_send(handle, "Edit1", img)
    time.sleep(1)
    autoit.control_click(handle, "Button1")
    time.sleep(1)

#서류 재업로드 함수
def modify_file(driver):
    while(1):
        #2. 유효하지않은 파일(재직증명서, 폐업한 업체파일)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)  #페이지 스크롤 다운
        time.sleep(1)
        print("사업자수정화면에서 스크롤 내리고!")

        try:
            wait = WebDriverWait(driver, 10)
            confirm = wait.until(EC.element_to_be_clickable((By.XPATH,'//div/button[@class="btn Button_btn_green__PyMEj"]')))
            confirm.click()  # 사업자정보 재확인 클릭
            time.sleep(1)
            print("사업자정보 재확인 클릭함!!!!")
            pass
        except TimeoutException:
            print("TimoutException 발생")
            pass

        if(driver.find_element(By.XPATH,'//div[@class="BizRegister_content_inner__2WZQx"]/strong[@class="BizRegister_content_title__KPz1m"]').text == "국세청 사업자정보가 확인되었습니다."):  #정상 파일 첨부시, 수정화면 벗어남
            print("정상파일 첨부되었습니다~")
            break

        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/div/button').click() #국세청 api실패 얼럿 > 확인
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,'FileUploaderButton_btn_cancel__hS_8Q').click() #첨부파일 삭제
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,'FileUploaderButton_file_label__3AbBD').click() #사업자등록증 재첨부 버튼 클릭
        time.sleep(1)
        print("파일재첨부")
        fileupload(img()) #다시 파일첨부
        time.sleep(3)

        #재첨부한 파일(사진)이 ocr실패하는 경우,
        if(len(driver.find_elements(By.CLASS_NAME,'OcrScanning_btn__BV7qH')) != 0):
            OCR_Fail(driver)
            break

#OCR실패한 경우,
def OCR_Fail(driver):
    print("OCR 분석실패!!!")
    random_button = random.randint(0, 1)
    random_button = 0

    if (random_button == 0):
        print("다시 촬영하기!")
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[3]/button[1]').click()  #다시 촬영하기
        time.sleep(1)
        fileupload(img()) #다시 파일첨부
        time.sleep(4)

        if len(driver.find_elements(By.XPATH,'//div[@class="BizRegister_business_license_info__JxJF6"]/div[@class="BizRegister_license_info__hS7zz"]')) != 0:  #정상 파일 첨부시, 수정화면 벗어남
            print("정상 파일 첨부됨")

        else:
            OCR_fail_page = len(driver.find_elements(By.CLASS_NAME, 'OcrScanning_btn__BV7qH'))
            print("또 실패했네...")

            #사진같은 사등파일이 아닌 경우,
            if (OCR_fail_page != 0):
                print("실패하고 나서 다시 촬영하기(파일첨부)")
                OCR_Fail(driver)
                time.sleep(1)

            #비유효파일(재직증명서,휴폐업자 파일)
            else:
                print("실패하고 나서 직접 입력하기(화면이동)")
                modify_file(driver)
                time.sleep(1)

    else:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[3]/button[2]').click()  # 직접 입력하기
        print("직접 입력하기 클릭함!!!!!")
        time.sleep(1)
        modify_file(driver)
        time.sleep(1)

#추가서류 업로드 창
def BusisnessDetail_modal(driver):
    official_confirmation_button = random.randint(0, 2)
    toast_message_error = 1 #토스트메시지 에러 노출값 초기설정
    count_upload = 0 #추가서류 개수

    #토스트메시지가 미노출될 경우, 다음 단계로 넘어감(while loop 탈출)
    while toast_message_error != 0:

        # 추가서류만 업로드
        if official_confirmation_button == 0:
            print("추가서류만 업로드함!")
            driver.find_element(By.XPATH,'//div/span[@class="FileUploaderButton_file_label__3AbBD"]').click()  # 추가서류 업로드
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
                print("추가서류 업로드창에서 토스트메시지 노출되지 않음")
                toast_message_error = 0 #토스트메시지 노출되지 않음


        # 추가서류 업로드 & 공식확인 버튼 체크
        elif official_confirmation_button == 1:
            print("추가서류 업로드 및 공식확인도 체크했음")
            driver.find_element(By.CLASS_NAME,'Checkbox_state_icon__jY3M3').click()  # 공식확인 체크
            time.sleep(1)
            driver.find_element(By.XPATH,'//div/span[@class="FileUploaderButton_file_label__3AbBD"]').click()  # 추가서류 업로드
            fileupload(img())
            time.sleep(1)

            # 추가서류 > 비유효파일이 들어간 경우, ex) PDF파일
            try:
                toast_message_pdf = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'SimpleToast_root__5Ypqn.danger'))
                )
                message = toast_message_pdf.text
                print("Toast message 내용: " + message)
                toast_message_error = 1

            except:
                print("추가서류 업로드창에서 토스트메시지 노출되지 않음")
                toast_message_error = 0

        # 공식확인 버튼만 체크
        elif official_confirmation_button == 2:
            print("공식확인만 체크함!")
            toast_message_error = 0
            driver.find_element(By.CLASS_NAME,'Checkbox_state_icon__jY3M3').click()  # 공식확인 체크
            time.sleep(1)

        #추가서류 업로드 10개한 경우, 토스트메시지 노출 여부확인. random 함수의 0~3까지 범위 변경
        """else:
            print("파일 10개 업로드해보자!!")
            while count_upload <= 10:
                driver.find_element(By.XPATH,'//div/span[@class="FileUploaderButton_file_label__3AbBD"]').click()  #추가서류 업로드
                fileupload(img())
                count_upload += 1

                #첨부파일이 11개일때, 토스트메시지 노출
                try:
                    toast_message_error = 1
                    toast_message_over10 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME,'SimpleToast_root__5Ypqn.danger'))
                    )
                    message = toast_message_over10.text

                    if message == "파일의 확장자 또는 실제 파일 유형이 올바르지 않습니다.":
                        count_upload -= 1
                        print("Toast message 내용: " + message)
                        time.sleep(3)
                        continue

                    print("Toast message 내용: " + message)
                    print("추가서류가 10개 초과함.")
                    toast_message_error = 0

                except:
                    print("업로드한 파일 개수: ",count_upload)
                    time.sleep(1)"""

