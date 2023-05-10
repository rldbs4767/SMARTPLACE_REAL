def url_confirm_smartplaceHome(driver,url):

    current_url = driver.current_url
    print(current_url)

    if(current_url == url):
        print("정상 스마플 홈")
        return 1

    else:
        print("비정상 url")
        return 0