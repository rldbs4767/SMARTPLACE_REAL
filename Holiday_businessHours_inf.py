import random
import time
from telnetlib import EC

from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#캘린더 > 활성화된 날짜 선별하는 함수
def choice_possible_day(driver):
    # 활성화된 날짜 선택하기...힘들었다...
    total_day = driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[@class="Calendar_day__bCrAv"]/td[contains(@class,"Calendar_day__bCrAv")]')
    possible_day = []

    for choice_day in total_day:
        if "Calendar_dimmed__1OFPb" not in choice_day.get_attribute('class'):  # 이미 선택되어 있는 휴무일
            if "Calendar_unavailable__TE_F_" not in choice_day.get_attribute('class'):  # 비활성화된 날짜
                #해당 월에 선택가능한 날짜가 없는 경우, 다음달로 넘어가서 선택진행!
                if len(choice_day.text.strip()) == 0: #possible_day의 텍스트를 가져와서 앞뒤 공백을 제거하고, 그 길이가 0인지 확인!
                    print("이번 달에는 선택할 수 있는 날이 없다!")
                    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/button[2]').click()
                    time.sleep(1)
                    calender_modal(driver)
                else:
                    possible_day.append(choice_day)

    return possible_day, total_day

#캘린더
def calender_modal(driver,cycle_random,next_month):

    possible_day, total_day = choice_possible_day(driver)
    cnt = 0

    fixed = []
    for x in range(len(possible_day)):
        fixed.append(possible_day[x].text)
    print("선택가능한 날짜:",fixed)

    select = random.randint(1, 2) #특정 날짜로 선택 or 기간으로 선택

    # 날짜 하나 선택
    if select == 1 or next_month == 1:
        print("날짜 하나 선택!")

        if next_month == 1:
            print("다음달로 넘어와서 다른 날짜 하나 선택!")
            random_select = random.randint(0, len(possible_day) - 1)

            print("선택한 날짜:", possible_day[random_select].text)
            possible_day[random_select].click()
            time.sleep(1)

        # 첫 번째에 해당월에 마지막 날을 선택한 경우, 다음달로 넘어감
        elif len(possible_day) == 0:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/button[2]').click()
            time.sleep(1)
            print(driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]').text)
            calender_modal(driver, cycle_random, 1)

        else:
            random_select = random.randint(0, len(possible_day)-1)

            print("선택한 날짜:", possible_day[random_select].text)
            possible_day[random_select].click()
            time.sleep(1)

        # 완료 버튼 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        print("-------------------------------------------------------------------------------------")


    # 날짜 두개 선택 => 기간으로 설정
    else:
        print("기간으로 선택!")
        for x in range(2):

            #첫 번째에 해당월에 마지막 날을 선택한 경우, 다음달로 넘어감
            if len(possible_day) == 0:
                driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/button[2]').click()
                time.sleep(1)
                print(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]').text)
                calender_modal(driver,cycle_random,1)
                break

            random_select = random.randint(0, len(possible_day) - 1)

            print("선택한 날짜:",possible_day[random_select].text)
            possible_day[random_select].click()
            time.sleep(1)
            cnt += 1

            # 날짜는 2개까지만 선택가능
            if cnt == 2:
                # 완료 버튼 클릭
                driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
                time.sleep(1)
                print("-------------------------------------------------------------------------------------")
                break

            # 두번째 날짜 선택
            else:
                to_remove = []
                for second_select in range(len(possible_day)):
                    if random_select >= second_select:
                        to_remove.append(possible_day[second_select]) #제거할 요소를 to_remove에 넣음
                for item in to_remove:
                    possible_day.remove(item) #한방에 제거..^^

                second_day = []
                for x in range(len(possible_day)):
                    second_day.append(possible_day[x].text)
                print("두 번째로 선택가능한 날짜들:",second_day)


    # 에러메시지 노출될 때,,,기간이 겹치는 경우,,,
    try:
        toast_message = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME,'SimpleToast_root__5Ypqn.danger'))
        )
        message = toast_message.text
        print("Toast message 내용: " + message)
        time.sleep(1)

        print("첫 번째 날짜 선택:",possible_day[random_select].text)
        possible_day[random_select].click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/button[2]').click() #다음달로 이동
        time.sleep(1)
        print(driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]').text)
        calender_modal(driver,cycle_random,1)


    except TimeoutException:
        print("토스트메시지 미노출")

#그 외 휴무일
def etc_holiday(driver):
    for x in range(3):
        print("그 외 휴무일...")
        #날짜로 추가
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[4]/button').click()
        time.sleep(1)

        # 매년, 매달, 한번만 랜덤 선택
        cycle_random = random.randint(1, 3)
        if cycle_random == 1:
            print("매년")
        elif cycle_random == 2:
            print("매달")
        else:
            print("한번만")
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[3]/div[1]/label[' + str(cycle_random) + ']/span').click()
        time.sleep(1)

        calender_modal(driver,cycle_random,0)

#임시공휴일 휴무
def temporary_holiday(driver):
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[3]/button').click()
    time.sleep(1)

    num = len(driver.find_elements(By.XPATH,'//div[@class="modal_scroll"]/div[@class="BusinessDetails_list_wrap__o9GRM"]/ul/li[@class="BusinessDetails_item__XZuKL"]'))
    for x in range(3):
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[4]/div/div[2]/div[2]/div[1]/ul/li[' + str(random.randint(1,num)) + ']/label/span').click()
        time.sleep(1)

    #저장하기
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[4]/div/div[2]/div[2]/button[1]').click()
    time.sleep(1)

#공휴일 중 휴무일
def closedDay_in_publicHoliday(driver):
    check = random.randint(1,3)

    #설,추석 당일만 휴무 체크
    if check == 1:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[2]/div[1]/label[1]/span').click()
        time.sleep(1)

    #전체 휴무 체크
    elif check == 2:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[2]/div[1]/label[2]/span').click()
        time.sleep(1)

    #랜덤 체크
    else:
        for x in range(4):
            if random.randint(0, 1) == 0:
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/label[' + str(random.randint(1, 9)) + ']/span').click()
                time.sleep(1)
            else:
                driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div[' + str(random.randint(1, 2)) + ']/label[' + str(random.randint(1, 3)) + ']/span').click()
                time.sleep(1)

#정기 휴무일
def regular_holiday(driver):
    print("정기 휴무일...")
    #드롭다운 박스 클릭
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div[1]/button').click()
    time.sleep(1)

    choice = random.randint(1,3)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div[1]/div/a[' + str(choice) + ']').click()
    time.sleep(1)

    #매주
    if choice == 1:
        #요일 선택
        for x in range(3):
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div[2]/div/label[' + str(random.randint(1, 7)) + ']').click()
            time.sleep(1)

    #격주
    elif choice == 2:
        #요일 선택
        for x in range(3):
            driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/label[' + str(random.randint(1, 7)) + ']').click()
            time.sleep(1)

        #활성화된 날짜 선택하기...힘들었다...
        total_day = driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/table/tbody/tr[@class="Calendar_day__bCrAv"]/td[contains(@class,"Calendar_day__bCrAv")]')
        select_day = []
        for possible_day in total_day:
            if "Calendar_unavailable__TE_F_" not in possible_day.get_attribute('class'):
                select_day.append(possible_day)
        random_select = random.randint(0, len(select_day)-1)
        print("선택한 날짜:",select_day[random_select].text)
        select_day[random_select].click()
        time.sleep(1)

        #완료 버튼 클릭
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)

    #매월
    else:
        #몇번째인지 선택
        for x in range(3):
            driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/button[' + str(random.randint(1, 5)) + ']').click()
            time.sleep(1)
        #요일선택
        for x in range(3):
            driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/label[' + str(random.randint(1, 7)) + ']/span').click()
            time.sleep(1)

        #완료 버튼 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)

#휴무일
def holiday_inf(driver):
    #휴무일이 있나요?
    #휴무일이 있어요
    holiday = random.randint(0, 1)
    holiday = 0

    if holiday == 0:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div/label[1]').click()
        time.sleep(1)
        # 정기 휴무일이 있나요?
        regular_holiday(driver)

        # 공휴일 중 휴무일이 있나요?
        closedDay_in_publicHoliday(driver)

        # 임시공휴일 휴무도 추가해주세요.
        temporary_holiday(driver)

        # 그 외 휴무일이 있다면?
        etc_holiday(driver)

    #휴무일이 없어요
    else:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[3]/div/label[2]').click()
        time.sleep(1)

#라스트오더
def lastorder(driver, use1, use2):

    #기준 리스트 클릭
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(1)

    if use1 == 0 or use2 == 0:
        select = random.randint(1, 2)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/a[' + str(select) + ']').click()
        time.sleep(1)
        if select == 2:
            return 0

    else:
        select = random.randint(1, 4)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/a[' + str(select) + ']').click()
        time.sleep(1)
        if select == 4:
            return 0

    #시간 선택
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/a[' + str(random.randint(1,24)) + ']').click()
    time.sleep(1)

    # 에러메시지 노출될 때,,,
    try:
        toast_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'SimpleToast_root__5Ypqn.danger'))
        )
        message = toast_message.text
        print("Toast message 내용: " + message)
        calender_modal(driver)
    except:
        print("토스트메시지 미노출")

#브레이크 타임
def breaktime(driver):
    setting = random.randint(0, 1)
    if setting == 1:
        #설정하기 클릭
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/button').click()

        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div[2]/div[2]/div/button') #모든 영업일 같음

        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div/div[3]/div/button') #평일 주말 달라요
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div[2]/div[2]/div/button')

        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div/div[3]/div/button') #요일별로 달라요
        time.sleep(1)

        # 에러메시지 노출될 때,,,
        try:
            toast_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'SimpleToast_root__5Ypqn.danger'))
            )
            message = toast_message.text
            print("Toast message 내용: " + message)
            calender_modal(driver)
        except:
            print("토스트메시지 미노출")
        return 1

    else:
        return 0

#영업일 선택
def business_date_choice(driver,category):
    # 모든, 평일/주말, 요일별로 선택
    choice = random.randint(1, 3)
    choice = 1

    #모든 영업일이 같아요
    if choice == 1:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[1]/label[1]/span').click()
        time.sleep(1)

        full_time = random.randint(0, 1)

        full_time = 1

        #24시간 운영하지 않는 경우,
        if full_time == 0:
            # 영업시간

             #시작시각
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/button').click()
            time.sleep(1)
            start_time = random.randint(1,24)
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/ul/li[' + str(start_time) + ']').click()
            time.sleep(1)

             #종료시각
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[1]/button').click()
            time.sleep(1)

            total_time = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]/ul/li[contains(@class,"BusinessDetails_option__NzJL8")]')
            select_time = []
            for possible_time in total_time:
                if "BusinessDetails_disabled__JwoXZ" not in possible_time.get_attribute('class'): #선택불가능한 시각 걸러내기
                    select_time.append(possible_time)
            random_select = random.randint(0, len(select_time) - 1)
            while (select_time[random_select].text <= str(start_time)): #시작시각보다 이전인 종료시각인 경우, 다시 선택하기!
                random_select = random.randint(0, len(select_time) - 1)
            print("선택한 시각:",select_time[random_select].text)
            select_time[random_select].click()
            time.sleep(1)

            # 브레이크타임
            #use1 = breaktime(driver)
            #use2 = 1

            # 라스트오더
            #if category in ["음식점","병원"]:
            #    lastorder(driver, use1, use2)

        #24시간 운영해요!
        else:
            driver.find_element(By.XPATH,'//div[@class="BusinessDetails_box_wrap__aW6fy"]/div/label/span[@class="BusinessDetails_form_text__X2ElZ"]').click()
            time.sleep(1)

            # 브레이크타임
            #breaktime(driver)

    #평일/주말 달라요
    elif choice == 2:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[1]/label[2]/span').click()
        time.sleep(1)

        # 평일(월~금)
        # 브레이크타임
        #use1 = breaktime(driver)

        # 주말
        # 브레이크타임
        #use2 = breaktime(driver)

        # 라스트오더
        #if category in ["음식점", "병원"]:
        #    lastorder(driver, use1, use2)

    #요일별로 달라요
    else:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[4]/div[1]/label[3]/span').click()
        time.sleep(1)

        # 요일 선택
        # 영업시간
        # 브레이크타임
        #use1 = breaktime(driver)
        #use2 = 1
        # 요일 추가
        # 라스트오더
        #if category in ["음식점", "병원"]:
        #    lastorder(driver, use1, use2)

#법정공휴일 영업시간
def statutory_holiday_businessHours(driver):
    #법정공휴일 영업시간
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[5]/button').click()
    time.sleep(1)

    #휴무일로 지정된 법정공휴일 안내 얼럿 노출
    if len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div/div')) != 0:
        #얼럿 > 확인
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div[3]/button').click()
        time.sleep(1)

    # 영업시간
        # 시작시각
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[5]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/button').click()
        time.sleep(1)
        start_time = random.randint(1, 24)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[5]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/ul/li[' + str(start_time) + ']').click()
        time.sleep(1)

        # 종료시각
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[5]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/button').click()
        time.sleep(1)

        total_time = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/ul/li[contains(@class,"BusinessDetails_option__NzJL8")]')
        select_time = []
        for possible_time in total_time:
            if "BusinessDetails_disabled__JwoXZ" not in possible_time.get_attribute('class'):  # 선택불가능한 시각 걸러내기
                select_time.append(possible_time)
        random_select = random.randint(0, len(select_time) - 1)
        while (select_time[random_select].text <= str(start_time)):  # 시작시각보다 이전인 종료시각인 경우, 다시 선택하기!
            random_select = random.randint(0, len(select_time) - 1)
        print("선택한 시각:", select_time[random_select].text)
        select_time[random_select].click()
        time.sleep(1)

        # 브레이크타임
        breaktime(driver)

#임시 영업 일정
def umcommon_businessHours(driver):
    print("평상시와 다르게 운영")
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[6]/div[1]/button').click()
    time.sleep(1)

    # 다음달로 이동
    if random.randint(0, 1) == 0:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/button[2]').click()
        time.sleep(1)

    # 활성화된 날짜 선택하기...힘들었다...
    total_day = driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[@class="Calendar_day__bCrAv"]/td[contains(@class,"Calendar_day__bCrAv")]')
    select_day = []
    for possible_day in total_day:
        if "Calendar_dimmed__1OFPb" not in possible_day.get_attribute('class'):  # 이미 선택되어 있는 휴무일
            if "Calendar_unavailable__TE_F_" not in possible_day.get_attribute('class'):  # 비활성화된 날짜
                print("선택가능한 날짜:", possible_day.text)
                select_day.append(possible_day)

    # 두번째 선택한 날짜가 두 번째 날짜보다 커야함
    first_select = -1
    for x in range(2):
        random_select = random.randint(0, len(select_day) - 1)
        while (random_select <= first_select):
            random_select = random.randint(0, len(select_day) - 1)
        print("선택한 날짜:", select_day[random_select].text)
        select_day[random_select].click()
        time.sleep(1)
        select_day.remove(select_day[random_select])  # 이미 선택한 날짜는 리스트에서 제외
        first_select = random_select

    # 완료 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[2]').click()
    time.sleep(1)

    #반복되는 임시휴무일이 존재함을 안내해주는 얼럿 노출
    if len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div[3]/div/div')) != 0:
        print("반복되는 임시휴무일이랑 겹침")
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div/div/div[2]/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[2]/button[1]').click() #모달 > 취소버튼 클릭
        time.sleep(1)
#영업시간
def businessHours_inf(driver,category):
    print("영업시간")

    #영업 시간을 알려주세요.
    business_date_choice(driver,category)

    #법정공휴일 영업시간
    #statutory_holiday_businessHours(driver)

    #평상시와 다르게 영업시간을 운영하는 날짜가 있다면?
    #umcommon_businessHours(driver)

    #영업시간이나 휴무일 관련 추가 안내
    #입력하기
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[8]/button').click()
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div[8]/div/input[2]').send_keys("영업시간이나 휴무일 관련 안내는 따로 없습니다!")
    time.sleep(1)


#휴무일/영업시간
def holiday_businesshoursInf(driver,category):

    holiday_inf(driver)

    if category not in ["호텔","콘도/리조트","모텔","숙박"]:
        businessHours_inf(driver,category)

    driver.find_element(By.XPATH, '//div/div/button[@class="btn Button_btn_green__PyMEj"]').click()  # 다음 탭으로 이동
    time.sleep(1)

