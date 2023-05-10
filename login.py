import time
from selenium.webdriver.common.by import By
def login(driver):
    #스마플 > 로그인
    driver.find_element(By.XPATH,'//div[@class="Popup_popup_check__1Yver"]/label/span[@class="Popup_check_box__VRQnP"]').click() #팝업 닫기 > 일주일간 안봄체크
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,'fn-booking.fn-booking-close1').click() #팝업 닫기 클릭
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div/div[1]/a').click() #오른쪽 상단 로그인 버튼 클릭
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="id"]').send_keys("아이디 입력") #아이디 입력
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys("비밀번호 입력") #비밀번호 입력
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click() #로그인 버튼 클릭
    time.sleep(1)

    if len(driver.find_elements(By.XPATH,'//div[@class="modal_layout"]')) != 0:
        print("등록완료 얼럿 노출됨!")
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
