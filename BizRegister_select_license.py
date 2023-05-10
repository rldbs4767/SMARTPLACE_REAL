from Basic_inf import *

#서류가 없는 경우,
def no_document(driver):
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div[1]/button[2]').click() #서류가 없을 경우 클릭
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div[4]/div[1]/div/input[2]').send_keys("학교오@") #업체명 입력
    time.sleep(1)
    select_tel(driver)
    address(driver)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div[5]/button').click() #중복업체 조회하기
    time.sleep(1)

def select_license(driver,modal_check):
    file_ok = random.randint(0,1)

    #서류가 없는경우
    if (len(driver.find_elements(By.XPATH,'//div/button[@class="BizRegister_item__ErqXb"][3]'))==1) & (file_ok == 0):
        no_document(driver)

    #사업자등록증으로 확인
    else:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div[1]/button[1]/span').click() #사업자등록증으로 확인
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div/div[2]/div[2]/button').click()  # 약관동의 > 동의하기
        time.sleep(1)

        #사업자등록증 및 추가서류 첨부하기

        # 사업자등록증 & 추가서류
        if len(modal_check) == 1:
            print("사업자등록증 & 추가서류 첨부하면 됨.")
            # 정상 사업자등록증 > select_num = 1
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/span').click()  #사업자등록증
            #fileupload(img())
            fileupload(img_path[1])
            time.sleep(1)

            BusisnessDetail_modal(driver) #추가서류 업로드 & 공식확인체크 모달

            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div/div[2]/div[2]/button').click()  #등록하기
            time.sleep(4)

            # 사업자정보가 정상적이지 않은 결과화면
            modify_page = len(driver.find_elements(By.CLASS_NAME,'BizRegister_business_modify__vfRgo'))
            OCR_fail_page = len(driver.find_elements(By.CLASS_NAME,'OcrScanning_btn__BV7qH'))

            # 1.재직증명서나 사등파일이 유효하지 않은 경우,
            if (modify_page != 0):
                modify_file(driver)
                time.sleep(3)

            # 2. 사진같이 사등파일이 아닌 경우
            if (OCR_fail_page != 0):
                OCR_Fail(driver)
                time.sleep(1)

        # 사업자등록증만
        else:
            print("사업자등록증만 첨부하면 됨.")
            # 정상 사업자등록증 > select_num = 1
            #fileupload(img())
            fileupload(img_path[1])
            time.sleep(5)

            # 사업자정보가 정상적이지 않은 결과화면
            modify_page = len(driver.find_elements(By.CLASS_NAME,'BizRegister_business_modify__vfRgo'))
            OCR_fail_page = len(driver.find_elements(By.CLASS_NAME,'OcrScanning_btn__BV7qH'))

            #1.재직증명서나 사등파일이 유효하지 않은 경우,
            if (modify_page != 0):
                modify_file(driver)
                time.sleep(3)

            #2. 사진같이 사등파일이 아닌 경우
            if (OCR_fail_page != 0):
                OCR_Fail(driver)
                time.sleep(1)

        #사업자정보 확인
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)  # 페이지 스크롤 다운
        time.sleep(2)

        select_tel(driver)  # 사업자확인 > 전화번호 선택

        # 사업자등록증 & 추가서류 실패 > 재첨부 > 추가서류 재첨부
        if driver.find_element(By.XPATH,'//div[@class="BizRegister_content_inner__2WZQx"]/div/button[@class="btn Button_btn_green__PyMEj"]').text == "추가서류 제출하기":
            print("추가서류 첨부합시다~")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[2]/div[7]/button').click()  # 추가서류 제출하기 클릭
            time.sleep(1)

            BusisnessDetail_modal(driver) #추가서류 업로드 & 공식확인체크 모달

            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div[2]/button').click()  # 등록하기 클릭
            time.sleep(3)
        else:
            print("중복업체 확인합시다~")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[2]/div[4]/button').click()  # 중복업체 조회하기 클릭
            time.sleep(2)

    #중복업체가 없는 경우, 얼럿 노출여부 확인
    new_register = driver.find_elements(By.CLASS_NAME,'modal_layout')

    #1.중복 업체 없어서 신규등록하는 경우
    if len(new_register) == 1:
        driver.find_element(By.XPATH,'//button[@class="btn_green"]').click()  #얼럿 > 신규업체로 등록하기
        time.sleep(1)
        print("중복업체 없이 신규등록 완료!!")
        return 1

    #2.중복업체 나오는 경우
    else:
        no_ongoing = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div[1]/div[1]/strong').text
        #내 업체만 있는 경우,
        if no_ongoing == "조회하신 정보로 관리중인 업체가 있습니다.":
            print("내 업체에 있는 업체임...자동화종료 하자")
            return 0

        elif no_ongoing == "조회하신 정보로 등록된 업체가 있습니다.":
            print("이미 등록되어 있는 업체임...자동화종료 하자")
            return 0

        #내 업체가 있거나 다른 중복업체가 있는 경우,
        else:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)  #페이지 스크롤 다운
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div[2]/button').click() #중복 업체 조회하기 버튼 클릭
            time.sleep(1)
            driver.find_element(By.CLASS_NAME,'Modal_btn_confirm__JBzc2').click() #얼럿 > 신규로 등록 버튼 클릭
            time.sleep(1)
            print("중복업체 무시하고!!! 신규등록 완료!!")
            return 1