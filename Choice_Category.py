import time
import random
from selenium.webdriver.common.by import By

def categoryChoice(driver):
#랜덤하게 업종 입력
    enter_keyword = ["음식점","미용실","네일샵","호텔","콘도","리조트","모텔","병원","마트","학교"]
    category_random = random.randint(0,len(enter_keyword)-1)
    category_random = 4
    time.sleep(1)

    driver.find_element(By.CLASS_NAME,'BrandSearch_input_search__Lk_es').send_keys(enter_keyword[category_random]) #주요 업종 입력하기
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div/form/button/i').click() #업종 검색
    time.sleep(1)


    #업종선택
    #큰 카테고리의 개수 뽑아내기
    categoryGroup = driver.find_elements(By.CLASS_NAME, 'BrandPopup_group_tit__K8C0z')
    print(len(categoryGroup))

    #큰 카테고리에서 입력 키워드의 카테고리 선별
    random_categoryGroup = random.randint(1,len(categoryGroup))
    print(random_categoryGroup)

    category_keyword = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div/div[' + str(random_categoryGroup) + ']/a[1]').text
    print("카테고리 키워드:",category_keyword)

    if "음식점" in category_keyword:
        category = "음식점"
    elif "미용실" in category_keyword:
        category = "미용실"
    elif "네일샵" in category_keyword:
        category = "네일샵"
    elif "숙박 > 호텔" in category_keyword:
        category = "호텔"
    elif "모텔" in category_keyword:
        category = "모텔"
    elif "콘도,리조트" in category_keyword:
        category = "콘도/리조트"
    elif "숙박" == category_keyword:
        category = "숙박"
    elif "건강,의료" in category_keyword:
        category = "병원"
    elif "슈퍼,마트" in category_keyword or "생활,편의 > 편의점" in category_keyword:
        category = "마트"
    elif "교육,학문" in category_keyword:
        if "학원" in category_keyword:
            category = "학원"
        else:
            category = "학교"
    else:
        category = "기타"

    #하위 업종이 10개 초과시, 목록 펼치기, default값은 class = fn fn-up2임(목록펼쳐진 상태)
    fn_down = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div/div[' + str(random_categoryGroup) + ']/a/i[@class="fn fn-down2"]')
    if len(fn_down) == 1:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div/div[' + str(random_categoryGroup) + ']/a[1]/i').click()
        time.sleep(5)

    #하위 업종의 개수 뽑아내기
    categoryGroup_down = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div/div/div/div/div/div/div[' + str(random_categoryGroup) + ']/a[@class="BrandPopup_item__qCHez"]')
    #print("하위 업종의 수: ",len(categoryGroup_down))

    #하위 업종의 개수 뽑아내기 > 랜덤으로 2depth 선별
    random_categoryGroup_down = random.randrange(1,len(categoryGroup_down)+1)
    #print("몇 번째 하위업종: ",random_categoryGroup_down)

    #하위 업종의 개수 뽑아내기 > 랜덤으로 하위 업종 선별 > 브랜드 선택
    choice_brand = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div/div/div[' + str(random_categoryGroup) + ']/a[' + str(random_categoryGroup_down+1) + ']')
    print("선택한 브랜드:",choice_brand.text)
    choice_brand.click()
    time.sleep(1)


    return category