import random

#0 ~ 26
img_path = [
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\윤미진_메이크업.png",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\와이비엠.png",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\고유번호증(교회).png",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\고유번호증(공인협의회).png",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\26번계정_초밥지이입.png",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\사등(다경).png",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\사등(브로우티).jfif",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\연세위치과(폐업체).jpg",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\재직증명서.png",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_9110.JPG",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_9111.JPG",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8899.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8986.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_9109.JPG",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8972.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8676.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8672.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_6651.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8523.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8671.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8572.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8993.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사진\\IMG_8996.jpeg",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\사등.pdf",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\엔테크서비스 사업자등록증.pdf",
        "C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\베풀장어.jpg",
        #"C:\\Users\\USER\\Desktop\\스마플\\사업자등록증\\사등(금지단어포함).png"
    ]

#이미지 랜덤 함수
def img():
    img_random = random.randint(0, len(img_path) - 1)
    print(img_path[img_random])
    return img_path[img_random]

#이미지 > 사진만 뽑는 랜덤함수
def img_photo():
    img_random = random.randint(9, 22)
    return img_path[img_random]