from login import *
from Choice_Category import *
from BizRegister_select_license import *
from Additional_inf import *
from Surgery_inf import *
from Room_inf import *
from Holiday_businessHours_inf import *
from URL_confirm import *
from Delete import DELETE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def REGISTER():

    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지

    #크롬드라이버 자동 설치(셀리니움 4버전)
    service = Service(ChromeDriverManager(path="ChromeDriver").install())

    execute = 0
    n = 100

    while execute < n:
        driver = webdriver.Chrome(service=service, options=options)

        #스마플 qa환경 진입
        url = "https://new.smartplace.naver.com/"
        driver.get(url)

        #스마플 > 롤링 팝업 종료 및 로그인
        login(driver)

        #정상 url 접속여부 확인
        check_url = url_confirm_smartplaceHome(driver,url)
        #비정상 url인 경우,,,
        if check_url == 0:
            # Enter 키 입력 시 실행 재개
            input("Press Enter to resume...")

        # 로그인 후 업체 신규등록
         #1. 업종별로 필요서류 확인
          #1-1 사업자등록증만 > 약관동의 > 파일업로드창
          #1-2 사업자등록증 & 추가서류 > 약관동의 > 각각 파일업로드창
          #1-3 사업자등록증 필요없는 경우,,,,

        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div[2]/div[2]/ul/li[1]/a').click() #업체 신규등록
        time.sleep(1)

        category = categoryChoice(driver) #카테고리 및 업종 선택
        print("업종:",category)

        #추가서류 필요한 업종 > 특정 모달 레이아웃 노출여부 확인
        modal_check = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]')

        #서류안내 얼럿 노출
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/div/div[2]/div[2]/button[2]').click() #얼럿 > 다음버튼 클릭
        time.sleep(1)

        #신규등록 진행할지, 중복확인하고 끝낼지,,,
        ongoing = select_license(driver,modal_check)
        """
            1. 사업자등록증으로 확인
            2. 사업자등록증없이 확인(미구현)
            3. 서류가 없는 경우
        """

        #중복조회시, 무시하고 신규등록 진행
        if ongoing:
            #업체정보 입력
            if category in ["음식점"]:
                print("기본정보, 메뉴정보, 부가정보, 휴무일-영업시간")
                basicInf(driver,category)
                menuInf(driver)
                additionalInf(driver,category)
                holiday_businesshoursInf(driver, category)

            elif category in ["미용실","네일샵"]:
                print("기본정보, 부가정보, 시술정보, 가격정보, 휴무일-영업시간")
                basicInf(driver,category)
                additionalInf(driver,category)
                surgeryInf(driver,category)
                priceInf(driver,category)
                holiday_businesshoursInf(driver, category)

            elif category in ["병원"]:
                print("기본정보, 부가정보, 가격정보, 휴무일-진료시간")
                basicInf(driver,category)
                additionalInf(driver,category)
                priceInf(driver, category)
                holiday_businesshoursInf(driver, category)

            elif category in ["모텔","숙박"]:
                print("기본정보, 모텔-부가정보, 객실정보, 휴무일")
                basicInf(driver,category)
                additionalInf(driver, category)
                roomInf(driver)
                holiday_businesshoursInf(driver, category)

            elif category in ["호텔","콘도/리조트"]:
                print("기본정보, 부가정보, 가격정보, 휴무일")
                basicInf(driver,category)
                additionalInf(driver,category)
                priceInf(driver, category)
                holiday_businesshoursInf(driver, category)

            elif category in ["마트","학교","학원","기타"]:
                print("기본정보, 부가정보, 가격정보, 휴무일-영업/운영시간")
                basicInf(driver,category)
                additionalInf(driver,category)
                priceInf(driver,category)
                holiday_businesshoursInf(driver, category)


        driver.close() # 자동화 종료

        execute += 1
        print("프로그램 실행 횟수: ",execute)
        print("---------------------------------------------------")

        if execute == n:
            print("프로그램 완전 종료합니다.")

    # 업체삭제
    print("업체 삭제 시작...")
    DELETE()

#업체등록
print("업체등록시작...")
REGISTER()
