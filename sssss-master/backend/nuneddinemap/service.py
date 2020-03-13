from .models import *
import base64
from PIL import Image
from io import BytesIO
from django.conf import settings #or from my_project import settings
import os
# from konlpy.tag import Komoran
import json
# komoran = Komoran()
import requests

def place_parser_from_reqeust(request):
    placeid = request.data['placeid']    
    latitude = request.data['latitude']   
    longitude = request.data['longitude']   
    placename = request.data['placename']
    location = request.data['location']
    phonenumber = request.data['phonenumber']
    parkinglot = request.data['parkinglot']
    tableinfo1 = request.data['tableinfo1']
    tableinfo2 = request.data['tableinfo2']
    tableinfo4 = request.data['tableinfo4']
    tableinfo5 = request.data['tableinfo5']
    
    opentime = request.data['opentime']
    closetime = request.data['closetime']
    place = Place.objects.create(placename=placename,latitude=latitude,longitude=longitude,placeid=placeid,location=location,phonenumber=phonenumber,parkinglot=parkinglot,tableinfo1=tableinfo1,tableinfo2=tableinfo2,tableinfo4=tableinfo4,tableinfo5=tableinfo5,opentime=opentime,closetime=closetime)    
    place.save()
    return place

    

# make placepicture instance and save image data
def placepicture_parser_from_request(request,place):
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
        os.makedirs(settings.MEDIA_ROOT+'/placepicture')
        os.makedirs(settings.MEDIA_ROOT+'/menupicture')
    placepicture = request.data['placepicture']    
    print("media root")
    print(settings.MEDIA_ROOT)
    print("URL")
    print(settings.MEDIA_URL)
    for image in placepicture:        
        URL = settings.MEDIA_URL+'placepicture/'
        path = settings.MEDIA_ROOT+'/placepicture/'

        filename = image['picture']
        data = image['data']        
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]
        im = Image.open(BytesIO(base64.b64decode(imgstr)))

        path += filename
        URL+= filename        
                
        placepicture = Placepicture.objects.create(name=URL,place=place)
        #image data save and save picture into the db
        im.save(path,ext)
        placepicture.save()


def cafe_parser_from_request(request, place):
    place_id = place.id
    cafe_data = request.data['cafe']
    storearea = cafe_data['storearea']
    alcoholonoff = cafe_data['alcoholonoff']
    dessertonoff = cafe_data['dessertonoff']
    smokingroom = cafe_data['smokingroom']
    powersoket = cafe_data['powersoket']
    subdetail = cafe_data['subdetail']
    cafe = Cafe.objects.create(place_id=place_id, storearea=storearea,alcoholonoff=alcoholonoff,dessertonoff=dessertonoff,smokingroom=smokingroom,powersoket=powersoket,subdetail=subdetail)
    cafe.save()
    return cafe

def menu_parser_from_request(request,cafe):
    menu_data_araay = request.data['menu'] 
    if Menu.objects.filter(cafe_id=cafe.id):  
        tempmenu = cafe.cafe_set.all()
        tempmenu.delete()
    for menu_data in menu_data_araay:
        # URL = ""
        # path = ""
        name = menu_data['name']
        price = menu_data['price']
        # info = menu_data['info']
        # filename,data = menu_data['menupicture']
        # if ';base64,' in data:
        #     URL = settings.MEDIA_URL+'/menupicture/'
        #     path = settings.MEDIA_ROOT+'/menupicture/'
            # filename = picture['name']
            # data = picture['data']        
            # format, imgstr = data.split(';base64,')
            # ext = format.split('/')[-1]
            # im = Image.open(BytesIO(base64.b64decode(imgstr)))

            # path += filename
            # URL+= filename        
            # im.save(path,ext)
        menu = Menu.objects.create(name=name,price=price,cafe=cafe)        
        menu.save()


def library_parser_from_request(request, place):
    place_id = place.id
    library_data = request.data['library']
    convenience = library_data['convenience']
    notebook = library_data['notebook']
    library = Library.objects.create(place_id=place_id, convenience=convenience,notebook=notebook)
    library.save()


def studycafe_parser_from_request(request, place):
    place_id = place.id
    studycafe_data = request.data['studycafe']
    price = studycafe_data['price']
    explanation = studycafe_data['explanation']
    studycafe = Studycafe.objects.create(place_id=place_id, price=price,explanation=explanation)
    studycafe.save()


def place_update(request, place):
    placeid = request.data['placeid']    
    latitude = request.data['latitude']   
    longitude = request.data['longitude']   
    placename = request.data['placename']
    location = request.data['location']
    phonenumber = request.data['phonenumber']
    parkinglot = request.data['parkinglot']
    tableinfo1 = request.data['tableinfo1']
    tableinfo2 = request.data['tableinfo2']
    tableinfo4 = request.data['tableinfo4']
    tableinfo5 = request.data['tableinfo5']
    opentime = request.data['opentime']
    closetime = request.data['closetime']
    # place.update(placeid=placeid,latitude=latitude,longitude=longitude,placename=placename,location=location,phonenumber=phonenumber,parkinglot=parkinglot,
    # tableinfo1=tableinfo1,tableinfo2=tableinfo2,tableinfo4=tableinfo4,
    # tableinfo5=tableinfo5,opentime=opentime,closetime=closetime)
    place.placeid = placeid
    place.latitude = latitude
    place.longitude = longitude
    place.placename = placename
    place.location = location
    place.phonenumber = phonenumber
    place.parkinglot = parkinglot
    place.tableinfo1 = tableinfo1
    place.tableinfo2 = tableinfo2
    place.tableinfo4 = tableinfo4
    place.tableinfo5 = tableinfo5
    place.opentime = opentime
    place.closetime = closetime
    place.save()
    return place

def library_update(request, place):
    convenience = request.data['library']['convenience']    
    notebook = request.data['library']['notebook'] 
    library = Library.objects.get(place_id = place.id)
    library.convenience = convenience
    library.notebook = notebook
    library.save()

def studycafe_update(request, place):
    price = request.data['studycafe']['price']    
    explanation = request.data['studycafe']['explanation']  
    studycafe = Studycafe.objects.get(place_id = place.id)
    studycafe.price = price
    studycafe.explanation = explanation
    studycafe.save()

def cafe_update(request, place):
    storearea = request.data['cafe']['storearea']
    alcoholonoff = request.data['cafe']['alcoholonoff']
    dessertonoff = request.data['cafe']['dessertonoff']
    smokingroom = request.data['cafe']['smokingroom']
    powersoket = request.data['cafe']['powersoket']
    subdetail = request.data['cafe']['subdetail']
    cafe = Cafe.objects.get(place_id = place.id)
    cafe.storearea = storearea
    cafe.alcoholonoff = alcoholonoff
    cafe.dessertonoff = dessertonoff
    cafe.smokingroom = smokingroom
    cafe.powersoket = powersoket
    cafe.subdetail = subdetail
    cafe.save()
    return cafe

# def menu_update(request, cafe):
#     menu = Menu.objects.get(cafe_id = cafe.id)
#     for i in request.data['menu']:
#         name = i['name']
#         price = i['price']
#         menu.name = name
#         menu.price = price
#         menu.save()
    # name = request.data['menu']['name']    
    # price = request.data['menu']['price']  
    

def NLP1(sentense):
    analysis = []
    analysis = komoran.pos(sentense)
    print("코리아")
    print(analysis)
    word_dict = {}
    analysis_len = len(analysis)
    if analysis[0][1] == 'VA':
        temp = analysis[0][0] + '다'
        if len(temp) > 2:
            word_dict[temp] = 1
    for idx in range(1, analysis_len):
        if analysis[idx][1] == 'VA':
            if analysis[idx-1][1] == 'MAG':
                temp = analysis[idx-1][0] + analysis[idx][0] + '다'
                if len(temp) > 2:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
            else:
                temp = analysis[idx][0] + '다'
                if len(temp) > 2:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
        elif analysis[idx][1] == 'NNG':
            if analysis[idx-1][1] == 'XPN':
                temp = analysis[idx-1][0] + analysis[idx][0]
                if len(temp) > 2:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
            else:
                temp = analysis[idx][0]
                if len(temp) > 1:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
        elif analysis[idx][1] == 'VX':
            temp = analysis[idx][0]
            if len(temp) > 1:
                if temp in word_dict:
                    word_dict[temp] += 1
                else:
                    word_dict[temp] = 1
    print(word_dict)
    return word_dict



def NLP(comments, com):
    # pass
    word_dict = json.loads(comments)

    sentense2 = com
    sentense = ''
    for i in range(len(sentense2)):
        if sentense2[i] == '.' or sentense2[i] == '?' or sentense2[i] == '!' or sentense2[i] == ','or sentense2[i] == '(' or sentense2[i] == ')' or sentense2[i] == '-':
            sentense += ' '
        else:
            sentense += sentense2[i]

    analysis = []
    analysis = komoran.pos(sentense)
    # print(analysis)

    analysis_len = len(analysis)
    if analysis[0][1] == 'VA':
        temp = analysis[0][0] + '다'
        if len(temp) > 2:
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 1
    for idx in range(1, analysis_len):
        if analysis[idx][1] == 'VA':
            if analysis[idx-1][1] == 'MAG':
                temp = analysis[idx-1][0] + analysis[idx][0] + '다'
                if len(temp) > 2:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
            else:
                temp = analysis[idx][0] + '다'
                if len(temp) > 2:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
        elif analysis[idx][1] == 'NNG':
            if analysis[idx-1][1] == 'XPN':
                temp = analysis[idx-1][0] + analysis[idx][0]
                if temp in word_dict:
                    word_dict[temp] += 1
                else:
                    word_dict[temp] = 1
            else:
                temp = analysis[idx][0]
                if len(temp) > 2:
                    if temp in word_dict:
                        word_dict[temp] += 1
                    else:
                        word_dict[temp] = 1
        elif analysis[idx][1] == 'VX':
            temp = analysis[idx][0]
            if len(temp) > 1:
                if temp in word_dict:
                    word_dict[temp] += 1
                else:
                    word_dict[temp] = 1

    return word_dict


# 카카오맵 장소 정보 파싱
def kakaoPlaceInfo(placeId):
    url = "https://place.map.kakao.com/main/v/"+str(placeId)
    response = requests.get(url)
    kakao_place_data = response.json()
    placeName = kakao_place_data["basicInfo"]["placenamefull"]  # 장소 이름
    placeAddress = kakao_place_data["basicInfo"]["address"]["region"]["fullname"] + kakao_place_data["basicInfo"]["address"]["newaddr"]["newaddrfull"]  # 장소 주소
    
    # 장소 번호
    if "phonenum" in kakao_place_data["basicInfo"].keys():
        placePhonenum = kakao_place_data["basicInfo"]["phonenum"]   
    else:
        placePhonenum = "062-123-4567"
    
    # 장소 소개글
    if "introduction" in kakao_place_data["basicInfo"].keys():
        placeIntroduction = kakao_place_data["basicInfo"]["introduction"]   
    else:
        placeIntroduction = placeName
    
    # 장소 영업시간
    if "openHour" in kakao_place_data["basicInfo"].keys():
        placeOpenHour = kakao_place_data["basicInfo"]["openHour"]["periodList"][0]["timeList"][0]["timeSE"]
    else:
        placeOpenHour = "00:00 ~ 24:00"

    # 장소 카테고리
    placeCategoryCode = int(kakao_place_data["basicInfo"]["cateid"])
    # 86: 카페(음식점), 174: 커피음식점(음식점), 923: 커피전문점(음식점) / 829: 도서관(교육,학문), 18427: 도서관(교육,학문) / 23758: 스터디카페(음식점)
    if (placeCategoryCode == 86) or (placeCategoryCode == 174) or (placeCategoryCode == 923):
        placeCategory = "카페"
    elif (placeCategoryCode == 829) or (placeCategoryCode == 18427):
        placeCategory = "도서관"
    else:
        placeCategory = "스터디카페"

    # 장소 이미지
    if "mainphotourl" in kakao_place_data["basicInfo"].keys():
        placeImg = kakao_place_data["basicInfo"]["mainphotourl"]   
    elif placeCategory == "카페":
        placeImg = "https://www.jeongdong.or.kr/static/portal/img/HKPU_04_04_pic1.jpg"    # 카페 대체 이미지 필요
    elif placeCategory == "도서관":
        placeImg = "http://www.eroun.net/news/photo/201809/3146_14309_4241.jpg"    # 도서관 대체 이미지 필요
    else:
        placeImg = "http://www.futurekorea.co.kr/news/photo/201812/113882_113664_442.jpg"    # 스터디카페 대체 이미지 필요

    # 추가 이미지 가져오기
    placePhotoList = []
    if "photo" in kakao_place_data.keys():
        photoList = kakao_place_data["photo"]["photoList"][0]["list"]
        for i in photoList:
            placePhotoList.append(i["orgurl"])
    else:
        pass    # 디폴트 이미지로 대체    

    # 장소 댓글
    placeCommentList = []
    # 1.comment
    if "comment" in kakao_place_data.keys():
        if "list" in kakao_place_data["comment"].keys():
            commentList = kakao_place_data["comment"]["list"]
            for i in commentList:
                if ("contents" in i.keys()) and (i["contents"] != "") and ("username" in i.keys()):
                    placeCommentList.append({'username':i["username"], 'contents':i["contents"]})
    else:
        pass

    # 2.kakaoStory
    if "kakaoStory" in kakao_place_data.keys():
        if "list" in kakao_place_data["kakaoStory"].keys():
            kakaoStoryList = kakao_place_data["kakaoStory"]["list"]
            for i in kakaoStoryList:
                if ("body" in i.keys()) and (i["body"] != "") and ("creator" in i.keys()):
                    placeCommentList.append({'username':i["creator"], 'contents':i["body"]})
    else:
        pass

    # 3.blogReview
    if "blogReview" in kakao_place_data.keys():
        if "list" in kakao_place_data["blogReview"].keys():
            blogReviewList = kakao_place_data["blogReview"]["list"]
            for i in blogReviewList:
                if ("contents" in i.keys()) and (i["contents"] != "") and ("blogname" in i.keys()):
                    placeCommentList.append({'username':i["blogname"], 'contents':i["contents"]})
    else:
        pass

    placeData = {
        'placeName' : placeName,
        'placeImg' : placeImg,
        'placePhonenum' : placePhonenum,
        'placeIntroduction' : placeIntroduction,
        'placeAddress' : placeAddress,
        'placeOpenHour' : placeOpenHour,
        'placeCategory' : placeCategory,
        'placePhotoList' : placePhotoList,
        'placeCommentList' : placeCommentList,
    }
    return placeData



# 댓글 키워드 뽑아내기 - DB에 기존 데이터가 없을 때
def NLP_comment(sentense):
    preprocess_sentense = ''
    for i in range(len(sentense)):
        if sentense[i] == '.' or sentense[i] == '?' or sentense[i] == '!' or sentense[i] == ',' or sentense[i] == '(' or sentense[i] == ')' or sentense[i] == '-':
            preprocess_sentense += ' '
        else:
            preprocess_sentense += sentense[i]

    analysis = []
    analysis = komoran.pos(preprocess_sentense)

    str = ''
    word_dict = {}
    for i in analysis:
        if ('NN') in i[1]:
            str = i[0]
        elif ('VA') in i[1]:
            str += (i[0] + "음")       
            if str in word_dict:
                word_dict[str] += 1
            else:
                word_dict[str] = 1
            str = ''
        elif ('NA') in i[1]:
            str = i[0]
            if str in word_dict:
                word_dict[str] += 1
            else:
                word_dict[str] = 1

    return word_dict
    
# 댓글 키워드 뽑아내기 - DB에 기존 데이터가 있을 때
def NLP_comment_db(comments, sentense):
    word_dict = json.loads(comments)
    if word_dict is None:
        word_dict = {}
    preprocess_sentense = ''
    for i in range(len(sentense)):
        if sentense[i] == '.' or sentense[i] == '?' or sentense[i] == '!' or sentense[i] == ',' or sentense[i] == '(' or sentense[i] == ')' or sentense[i] == '-':
            preprocess_sentense += ' '
        else:
            preprocess_sentense += sentense[i]

    analysis = []
    analysis = komoran.pos(preprocess_sentense)

    str = ''
    for i in analysis:
        if ('NN') in i[1]:
            str = i[0]
        elif ('VA') in i[1]:
            str += (i[0] + "음")       
            if str in word_dict:
                word_dict[str] += 1
            else:
                word_dict[str] = 1
            str = ''
        elif ('NA') in i[1]:
            str = i[0]
            if str in word_dict:
                word_dict[str] += 1
            else:
                word_dict[str] = 1
    return word_dict

# 카카오 장소 이미지 가져오기
def getImage(address_name, place_name, place_category):
    print("eee")
    queryString = str(address_name) + " " + str(place_name) + " "  + str(place_category)
    url = "https://dapi.kakao.com/v2/search/image?query="+queryString
    headers = {"Authorization": "KakaoAK dcec71e023f9c1ef32498ea45540e114"}
    print("ddd")
    result = requests.get(url, headers=headers)
    kakaoResponse = json.loads(str(result.text))
    img_list = kakaoResponse["documents"]
    resultList = []
    print(result)
    if len(img_list) > 0:
        print(len(img_list))
        for i in range(len(img_list)):
            if i>=1:
                break
            resultList.append(img_list[i]["image_url"])
        # for img in img_list:
        #     resultList.append(img["image_url"])
    placeData = {
        'placeImgList' : resultList,
    }
    return placeData
