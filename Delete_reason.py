import random
import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#업체삭제 사유
def delete_reason(driver):
    first_reason = random.randint(1, 6)
    first_reason = 1 #업체삭제할 떄, 사용

    #폐업, 업종변경, 업체중복등록
    if first_reason == 1:
        second_reason = random.randint(1, 3)
        if second_reason == 1:
            print("폐업")
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/ul/li[1]/a').click()
            time.sleep(1)

        elif second_reason == 2:
            print("업종변경")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/ul/li[2]/a').click()
            time.sleep(1)

        else:
            print("업체 중복 등록")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/ul/li[3]/a').click()
            time.sleep(1)

        # 삭제하기
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div/button').click()
        time.sleep(1)

        # 얼럿 > 삭제하기
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(1)
        # 에러메시지 노출될 때,,,
        try:
            toast_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME,'SimpleToast_root__5Ypqn.danger'))
            )
            message = toast_message.text
            print("Toast message 내용: " + message)

        except:
            # 얼럿 > 확인
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button').click()
            time.sleep(1)

    #주소,위치 변경, 업체명 변경, 전화번호 변경
    elif first_reason == 2:
        second_reason = random.randint(1, 3)
        if second_reason == 1:
            print("주소 위치 변경")
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/ul/li[4]/a').click()
            time.sleep(1)

        elif second_reason == 2:
            print("업체명 변경")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/ul/li[5]/a').click()
            time.sleep(1)

        else:
            print("전화번호 변경")
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/ul/li[6]/a').click()
            time.sleep(1)

        #업체 정보 관리 바로가기 > 업체정보로 이동,,,
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/a').click()
        time.sleep(1)

    #전화번호 노출안함
    elif first_reason == 3:
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/ul/li[7]/a').click()
        time.sleep(1)

        random_button = random.randint(1, 2)
        #업체 정보 관리 바로가기
        if random_button == 1:
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div/a').click()
            time.sleep(1)

        #업체 전화번호 숨기기
        else:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/button').click()
            time.sleep(1)
            #얼럿 노출 > 예
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
            time.sleep(1)

    #업체 주인 권한 위임,해제
    elif first_reason == 4:
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/ul/li[8]/a').click()
        time.sleep(1)
        random_button = random.randint(1, 2)
        #주인 권한을 다른 사람에게 위임할게요
        if random_button == 1:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/a').click()
            time.sleep(1)
            #권한 관리 페이지로 이동...

        #제 주인 권한을 해제할게요
        else:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/button').click()
            time.sleep(1)
            #얼럿 노출 > 해제하기
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
            time.sleep(1)

    #별점 리뷰 노출하고 싶지 않음
    elif first_reason == 5:
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/ul/li[9]/a').click()
        time.sleep(1)

        #미노출 설정하러 가기 > 업체홈으로 이동
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div').click()
        time.sleep(1)

    #일정기간 휴업 예정
    else:
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/ul/li[10]/a').click()
        time.sleep(1)
        random_button = random.randint(1, 2)
        #휴무기간 지정하기 > 업체정보 > 휴무일/영업시간탭으로 이동
        if random_button == 1:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/a[1]').click()
            time.sleep(1)

        # 새소식 작성하기 > 소식쓰기 페이지로 이동
        else:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div/a[2]').click()
            time.sleep(1)
            #새소식 쓰기 함수 call...