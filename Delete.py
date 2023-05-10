from bs4 import BeautifulSoup

from URL_confirm import url_confirm_smartplaceHome
from login import *
from Delete_reason import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def DELETE():
    print("업체 삭제 시작한다잉~")

    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지

    #크롬드라이버 자동 설치(셀리니움 4버전)
    service = Service(ChromeDriverManager(path="ChromeDriver").install())
    driver = webdriver.Chrome(service=service, options=options)

    #스마플 qa환경 진입
    url = "https://test-new.smartplace.naver.com/"
    driver.get(url)

    #스마플 > 롤링 팝업 종료 및 로그인
    login(driver)
    time.sleep(1)

    # 정상 url 접속여부 확인
    check_url = url_confirm_smartplaceHome(driver, url)
    # 비정상 url인 경우,,,
    if check_url == 0:
        # Enter 키 입력 시 실행 재개
        input("Press Enter to resume...")

    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/div[2]/ul/li[3]/a').click() #내 업체 클릭
    time.sleep(1)

    keyword = "자동화"

    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/input[2]').send_keys(keyword+Keys.RETURN) #업체명에 자동화가 들어간 업체 검색
    time.sleep(1)

    check_company = len(driver.find_elements(By.CLASS_NAME,'BusinessList_no_content__bbJcr'))
    time.sleep(1)

    if check_company != 0:
        company_num = 0
        print("검색하신 키워드에 해당하는 업체가 없습니다.")

    else:
        company_num = len(driver.find_elements(By.CLASS_NAME, 'BusinessList_business_item__AZgLu'))
        time.sleep(1)
        print("삭제하는 업체 개수: ", company_num)
        order = 1

        for x in range(company_num):
            # 등록대기
            # '내 플레이스 보기'가 비활성화 되어있는 것으로 등록대기 상태 업체 확인...
            if len(driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/div/div/ul/li[' + str(order) + ']/div/div/div[2]/div/button[@class="BusinessList_btn__nHKJs BusinessList_disabled__d9Ilk"]')) != 0:

                # 보유 업체가 100개 이상인 경우, 업체상태 표기안됨...ㅠㅠ오류임...
                if len(driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/div/div/ul/li[' + str(order) + ']/div/div[2]/div[2]/button')) == 0:
                    order += 1
                    pass

                else:
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/div/div/ul/li[' + str(order) + ']/div/div[2]/div[2]/button').click()  # 등록취소 버튼 클릭
                    time.sleep(1)
                    driver.find_element(By.XPATH,'//div[@class="Modal_bottom__zeqAA"]/button[@class="Modal_btn_confirm__JBzc2"]').click()  # 얼럿 > 취소하기 버튼 클릭
                    time.sleep(1)

                    # 삭제를 원하는 업체명검색
                    try:
                        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/input[2]'))
                        )
                        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/input[2]').send_keys(keyword + Keys.RETURN)
                        time.sleep(1)

                    except TimeoutException:
                        print("타임에러...")

            # 정상
            else:
                # ''' 클릭
                try:
                    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/div/div/ul/li[' + str(order) + ']/div/div/div[2]/button')))
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[2]/div/div/ul/li[' + str(order) + ']/div/div/div[2]/button').click()
                    time.sleep(1)

                except TimeoutException:
                    print("타임에러...")

                layer_select = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/div/div/ul/li[' + str(order) + ']/div/div/div[2]/div[2]')
                soup = BeautifulSoup(layer_select.get_attribute('innerHTML'), 'html.parser')
                a_tags = soup.find_all('a')
                # print("a 태그의 개수:",len(a_tags))
                # 예약서비스일 경우,,,삭제안함
                if len(a_tags) == 6:
                    order += 1
                    pass

                # 정상 업체인 경우, a태그 = 5개
                else:
                    # 업체삭제 클릭
                    driver.find_element(By.XPATH,'//div[@class="BusinessList_layer_select__Za7O_"]/a[@class="BusinessList_select_item__UQp_T"][2]').click()
                    time.sleep(1)

                    # 업체삭제 사유 선택하기...
                    delete_reason(driver)

                    # 삭제를 원하는 업체명검색
                    try:
                        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/input[2]')))
                        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/input[2]').send_keys(keyword + Keys.RETURN)
                        time.sleep(1)

                    except TimeoutException:
                        print("타임에러...")

        print("삭제완료!")
    driver.close()

    #업체 등록
    print("다시 업체등록시작....")
    from Register import REGISTER
    REGISTER()
