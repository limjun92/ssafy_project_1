from django.shortcuts import render, get_object_or_404
import requests
import json
from django.http import JsonResponse, HttpResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework.parsers import JSONParser
from .service import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
# from konlpy.tag import Komoran
# komoran = Komoran()
# Create your views here.

# @permission_classes((IsAuthenticated,)) # 허가: 인증 된 사용자만 허가(로그인 되어있어야함)
# @authentication_classes((JSONWebTokenAuthentication, )) # 인증: jtw 방식으로 들어온 사용자만 인증
from django import forms
@api_view(['POST'])
@permission_classes([AllowAny, ])
def signup(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        password = request.data.get('password')

        user = serializer.save()
        user.set_password(password) 
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        
        return JsonResponse({'token': token})
    return HttpResponse(status=400)


@api_view(['GET',])
@permission_classes([AllowAny, IsAuthenticated, ])
def userInfo(requset, id):
    user = get_object_or_404(User, id = id)
    serializers = UserSerializer(user)
    return JsonResponse(serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
@authentication_classes([JSONWebTokenAuthentication, ])
def mypage(request, id):
    user = get_object_or_404(User, id = id)
    if request.method == 'GET':
        serializers = MypageSerializer(user)
        return JsonResponse(serializers.data)
    else:
        if request.user == user:
            if request.method == 'PUT':
                serializer = UserChangeSerializer(user, request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    serializer = MypageSerializer(user)
                    return JsonResponse(serializer.data)
            else:
                username = user.username
                user.delete()
                return JsonResponse({'message': '그동안 감사했습니다. {username}님.'})
    return HttpResponse('잘못된 접근입니다.', status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def like(request):
    placeid = request.data['placeid'] 
    if Place.objects.filter(placeid=placeid): 
        pass
    else: 
        placename = request.data['placeinfo']['placename']
        latitude = request.data['placeinfo']['latitude']
        longitude = request.data['placeinfo']['longitude']
        location = request.data['placeinfo']['location']
        # phonenumber = request.data['placeinfo']['phonenumber']
        # surroundinginformation = request.data['placeinfo']['subdetail']
        # opentime
        # closetime
        place = Place.objects.create(placeid=placeid, latitude=latitude,longitude=longitude,placename=placename, location=location)
        place.save()

        if request.data['category'] == '카페':
            cafe = Cafe.objects.create(place=place)
            cafe.save()
        elif request.data['category'] == '도서관':
            library = Library.objects.create(place=place)
            library.save()
        elif request.data['category'] == "스터디카페":
            studycafe = Studycafe.objects.create(place=place)
            studycafe.save()

    place = Place.objects.get(placeid=placeid)
    user = request.user
    
    if user not in place.like_users.all():
        place.like_users.add(user)
        on_like = True
    else:
        place.like_users.remove(user)
        on_like = False
    context = {
        'count_like' : place.like_users.all().count(),
        'on_like' : on_like
    }
    return JsonResponse(context)


    # if request.method == "GET":
    #     place = get_object_or_404(Place, id=place_id)
    #     serializer = LikePlaceSerializer(place)
    #     print('뭐지', serializer.data)
    #     return JsonResponse(serializer.data)
    # if request.method == "POST":
    #     serializer = LikePlaceSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
            
    #         like = serializer.save(commit=False)
            
    #         like.save()
    #         return JsonResponse({'msg': '좋아요가 눌렸습니다.' })

@api_view(['POST'])
@permission_classes([AllowAny, ])
def registdetail(request, id):
    placeid = request.data['placeid']
    if id == 1: 
        if Place.objects.filter(placeid=placeid): 
            place = Place.objects.get(placeid=placeid)
            print(place.id)
            place = place_update(request, place)
            placepicture_parser_from_request(request,place) 
            cafe = cafe_update(request, place)
            menu_parser_from_request(request,cafe) 
            return JsonResponse({'result':'true'})
        else:
            place = place_parser_from_reqeust(request)    
            placepicture_parser_from_request(request,place)    
            cafe = cafe_parser_from_request(request, place)    
            menu_parser_from_request(request,cafe)    
            return JsonResponse({'result':'true'})
    elif id == 2: 
        if Place.objects.filter(placeid=placeid): 
            place = Place.objects.get(placeid=placeid)
            place_update(request, place)
            placepicture_parser_from_request(request,place) 
            studycafe_update(request, place)
            return JsonResponse({'result':'true'})
        else:
            place = place_parser_from_reqeust(request)    
            placepicture_parser_from_request(request,place) 
            studycafe_parser_from_request(request, place)
            return JsonResponse({'result':'true'})
    elif id == 3: 
        if Place.objects.filter(placeid=placeid): 
            place = Place.objects.get(placeid=placeid)
            print(place)
            place_update(request, place)
            placepicture_parser_from_request(request,place) 
            library_update(request, place)
            return JsonResponse({'result':'true'})
        else:
            place = place_parser_from_reqeust(request) 
            placepicture_parser_from_request(request,place) 
            library_parser_from_request(request, place)
            return JsonResponse({'result':'true'})

    
           
           
@api_view(['GET']) 
@permission_classes([AllowAny, ])
def place(request):
    place = Place.objects.all()
    serializer = YYEPlaceSerializer(place, many=True)
    return Response(serializer.data)

@api_view(['GET']) 
@permission_classes([AllowAny, ])
def place_userreview_all(request):
    review = Userreview.objects.all()
    serializer = UserreviewSerializer(review, many=True)
    return Response(serializer.data)

@api_view(['GET']) 
@permission_classes([AllowAny, ])
def place_detail(request, id=id):
    if Place.objects.filter(placeid=id): 
        place = Place.objects.get(placeid=id)
        serializer = YYEPlaceSerializer(place)
        comment = Comment.objects.filter(place=place).order_by('-id')
        serializer2 = CommentSerializer(comment, many=True)
        return JsonResponse({"result":"true","data":serializer.data, "data2":serializer2.data})
    else:
        return JsonResponse({"result":"false"}) 


@api_view(['POST']) 
@permission_classes([AllowAny, ])
def place_detail_imgs(request):    
    print(request.data)
    try:
        placeData = getImage(request.data['address_name'], request.data['place_name'], request.data['place_category'])
        return JsonResponse({"result":"true","data":placeData})
    except:
        return JsonResponse({"result":"false"}) 




@api_view(['GET',])   
@permission_classes([AllowAny, ])
def comment_get(request, id):
    place = get_object_or_404(Place, id=id)  
    comments = place.comment_set.all()
    serializer = TempComment(comments, many=True)
    return Response(serializer.data)

@api_view(['POST',])   
@permission_classes([IsAuthenticated, ])
def comment_post(request):
    placeid = request.data['placeid'] 
    comment = request.data['comment']

    if Place.objects.filter(placeid=placeid): 
        tempplace = Place.objects.get(placeid=placeid)
        comments = tempplace.comment_set.all()

        if len(comments) == 0:
            # analysis = NLP1(comment)
            analysis = NLP_comment(comment)
            if analysis == {}:
                analysis = {"제거":-1}
            result = json.dumps(analysis, ensure_ascii=False) 
            tempplace.placekeyword = result
            tempplace.save()
        else:
            pw = tempplace.placekeyword
            worddict = NLP_comment_db(pw, comment)
            # worddict = NLP_comment(pw, comment)  
            result = json.dumps(worddict, ensure_ascii=False) 
            # tempplace = Place.objects.get(placeid=placeid)
            tempplace.placekeyword = result
            tempplace.save()

        serializer = TempComment(data=request.data)
        if serializer.is_valid(raise_exception=True):  
            realcomment = serializer.save(place=tempplace, review_user=request.user)
            serializer2 = CommentSerializer(realcomment) 
            return Response(serializer2.data)
    else: 
        placename = request.data['placeinfo']['placename']
        latitude = request.data['placeinfo']['latitude']
        longitude = request.data['placeinfo']['longitude']
        location = request.data['placeinfo']['location']
        # phonenumber = request.data['placeinfo']['phonenumber']
        # surroundinginformation = request.data['placeinfo']['subdetail']
        # opentime
        # closetime
        place = Place.objects.create(placeid=placeid, latitude=latitude,longitude=longitude,placename=placename, location=location)
        place.save()

        if request.data['category'] == '카페':
            cafe = Cafe.objects.create(place=place)
            cafe.save()
        elif request.data['category'] == '도서관':
            library = Library.objects.create(place=place)
            library.save()
        elif request.data['category'] == '스터디카페':
            studycafe = Studycafe.objects.create(place=place)
            studycafe.save()

        # comment = request.data['comment']
        # review_user = request.data['review_user']['username']

        # comments = Comment.objects.create(place=place, comment=comment, review_user_id=review_user)
        # comments.save()   
        analysis = NLP_comment(comment) 
        # if analysis == {}:
        #     analysis = {"제거":-1}
        result = json.dumps(analysis, ensure_ascii=False) 

        tempplace = Place.objects.get(placeid=placeid)


        tempplace.placekeyword = result
        tempplace.save()


        serializer = TempComment(data=request.data)
        if serializer.is_valid(raise_exception=True):  
            realcomment = serializer.save(place=tempplace, review_user=request.user)
            serializer2 = CommentSerializer(realcomment) 
            return Response(serializer2.data)

    # return JsonResponse(request.data)


 


@api_view(['GET'])   
@permission_classes([AllowAny, ])
def place_keyword(request, id):
    place = Place.objects.get(placeid=id)    
    temp = place.placekeyword
    print("temp",temp)
    keyword = json.loads(temp)
    keywordList = sorted(keyword.items(), key=lambda x: x[1], reverse=True)
    resultData = []
    for i in range(len(keywordList)):
        if(i<3):
            resultData.append(keywordList[i][0])
        else:
            break
    if len(keywordList)>0 and keywordList[0][0] == "제거":
        return JsonResponse({"result":"true", "data":["편안함","맛있는","서비스가 좋은"]})
    else:
        return JsonResponse({"result":"true", "data":resultData})

@api_view(['DELETE', 'PUT']) 
@permission_classes([IsAuthenticated, ])
def comment_detail(request, place_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = TempComment(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return HttpResponse(status=400)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message':"삭제되었습니다."})

@api_view(['POST']) 
@permission_classes([IsAuthenticated, ])
def userreview_post(request):
    placeid = request.data['placeid'] 
    
    if Place.objects.filter(placeid=placeid): 
        pass
    else: 
        placename = request.data['placeinfo']['placename']
        latitude = request.data['placeinfo']['latitude']
        longitude = request.data['placeinfo']['longitude']
        location = request.data['placeinfo']['location']
        # phonenumber = request.data['placeinfo']['phonenumber']
        # surroundinginformation = request.data['placeinfo']['subdetail']
        # opentime
        # closetime
        place = Place.objects.create(placeid=placeid, latitude=latitude,longitude=longitude,placename=placename, location=location)
        place.save()

        if request.data['category'] == '카페':
            cafe = Cafe.objects.create(place=place)
            cafe.save()
        elif request.data['category'] == '도서관':
            library = Library.objects.create(place=place)
            library.save()
        elif request.data['category'] == '스터디카페':
            studycafe = Studycafe.objects.create(place=place)
            studycafe.save()
    place = Place.objects.get(placeid=placeid)
    serializer = TempUserreviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  
        reviews = serializer.save(place=place, review_user=request.user)
        serializer2 = UserreviewSerializer(reviews) 
    oneUserReviewSerializer = OneUserAllreviewSerializer(place)
    return Response(oneUserReviewSerializer.data)


def place_choice(requests, id):
    pass
    # question = get_object_or_404(Question, id=id)
    # if request.method == 'POST':
    # choice_form = ChoiceForm(request.POST)
    # if choice_form.is_valid():
    #     choice = choice_form.save(commit=False)
    #     choice.question = question
    #     choice.save()
    #     return redirect('questions:detail', id)
    

@api_view(['POST'])
@permission_classes([AllowAny, ])
def search(request):
    print(request.data)
    return Response("good")




'''
<창현>
REST API키 : c08e8b0e4c7e3a8f880b50a4d40c30dd
javascript키 : 55e38b30739707231a11bf808145516f

<준형>
REST API키 : dcec71e023f9c1ef32498ea45540e114
javascript키 : 2f286ff0204a69b26c881678e92553a9


'''

# Create your views here.
def index(request):
    return render(request, 'nuneddinemap/integrate.html')

def integrate(request):
    if request.method == 'GET':
        return render(request, 'nuneddinemap/integrate.html')
    elif request.method == 'POST':
        locationName = request.POST.get('locationName')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')

        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+str(locationName)+"&x="+str(longitude)+"&y="+str(latitude)
        headers = {"Authorization": "KakaoAK dcec71e023f9c1ef32498ea45540e114"}
        result = requests.get(url, headers=headers)
        addr = json.loads(str(result.text))
        '''
        for i in range(len(addr['documents'])):
            print(addr['documents'][i])
        print()
        '''
        context = {
            'addr':addr['documents']
        }
    return render(request, 'nuneddinemap/integrate.html', context)

'''
def search(request):
    return render(request, 'nuneddinemap/index.html')
'''

def hello(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        context = {
            'data':data
        }
    return render(request, 'nuneddinemap/aaa.html', context)
##########################################################
def new(request):
    if request.method == 'GET':
        return render(request, 'nuneddinemap/new.html')
    elif request.method == 'POST':
        data = request.POST.get('place')
        context = {

            'data':data
        }
    return render(request, 'nuneddinemap/new.html', context)



def createdb(request):
    placeurl = '/media/placepicture/'
    place1 = [26910025, 35.1751491987338, 126.915321920255,'투썸플레이스 광주전남대점','광주 북구 중흥동호동로 25','062-268-2388', False, 1, 2, 22, 5, '나만의 즐거움을 만날 수 있는 프리미엄 디저트 카페 A Twosome Place','10:00:00', '02:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    cafe1 = [0, False, True, True, 27]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    
    place2 = [350241666, 35.190050422539, 126.825273535379,'T&T북카페','광주 광산구 수완동임방울대로332번길 9-12','062-123-4567', False, 21, 0, 6, 4, '','09:00:00', '23:00:00',{}]
    place = Place.objects.create(placeid=place2[0],latitude=place2[1],longitude=place2[2],placename=place2[3],location=place2[4],phonenumber=place2[5],parkinglot=place2[6],tableinfo1=place2[7],tableinfo2=place2[8],tableinfo4=place2[9],tableinfo5=place2[10],surroundinginformation=place2[11],opentime=place2[12],closetime=place2[13],placekeyword=place2[14])    
    place.save()
    placepicture1 = ['북카페1.jpg', '북카페2.jpg', '북카페3.jpg','북카페4.jpg','북카페5.jpg','북카페6.jpg','북카페7.jpg','북카페8.jpg','북카페9.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe2 = [0, False, True, False, 30]
    cafe = Cafe.objects.create(place=place, storearea=cafe2[0],alcoholonoff=cafe2[1],dessertonoff=cafe2[2],smokingroom=cafe2[3],powersoket=cafe2[4])
    cafe.save()
    menu2 = ['에스프레소',3200,'아메리카노',3500,'카페라떼',4000,'카푸치노',4000,'바닐라라떼',4300,'카라멜라떼',4300,'헤이즐럿라떼',4300,'카라멜마끼아또',4500,'카페모카',4500,'핸드드립',4500,'그린티라떼',4500,'고구마라떼',4500,'핫초코',4500,'자몽/레몬에이드',4500,'복숭아 아이스티',3500,'레몬차',4000,'유자차',4000,'자몽차',4500,'녹차',4000,'캐모마일',4000,'얼그레이',4000,'루이보스',4000,'그린티프라페',4000,'쿠키앤크림프라페',5500,'생과일주스',5000,'플레인 요거트',5000,'딸기 요거트',5300,'블루베리 요거트',5300,'베이글',3000,'머핀',2500,'프레즐',2500]
    for i in range(0, len(menu2), 2):
        menu = Menu.objects.create(cafe=cafe, name=menu2[i], price=menu2[i+1])
        menu.save()

    place1 = [1483117770, 35.205522263639, 126.897934692043,'스타벅스 광주일곡점','광주 북구 일곡동설죽로 518','062-575-3394', False, 14, 14, 13, 1, '','08:00:00', '21:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['일곡동스타벅스.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe1 = [0, False, True, True, 32]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    place1 = [1175775715, 35.147761350131, 126.847916786334,'커피빈 광주상무역점','광주 서구 치평동상무중앙로 9','062-385-8371', False, 0, 0, 20, 0, '','07:30:00', '22:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['커피빈1.jpg','커피빈2.jpg','커피빈3.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe1 = [0, False, True, False, 15]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    place1 = [17850310, 35.1618141747946, 126.882513210157,'엔제리너스 광주광천D/T점','광주 서구 광천동무진대로 933','062-368-6004', True, 7, 0, 44, 8, '천사를 모티브로 풍부한 커피맛과 편안하게 즐길 수 있는 공간을 제공하는 커피전문 브랜드','09:00:00', '22:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['광천엔젤1.jpg','광천엔젤2.jpg','광천엔젤3.jpg','광천엔젤4.jpg','광천엔젤5.PNG']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    user1 = ['이경석','양예은','최창현','윤서영','임준형','이싸피','양싸피','최싸피','윤싸피','임싸피']
    for i in range(len(user1)):
        user = User.objects.create(age=25, ceo=False, name=user1[i], username=user1[i], password='123123123')
        user.save()
    comment1 = ['광천터미널(광주종합버스터미널) 맞은편에 있는 크고 아름다운 엔제리너스입니다.1층만 본다면 작은 카페 같지만 3층으로 올라가면(2층은 스시집) 굉장히 넓고 쾌적하고 공부하는 사람들로 넘쳐납니다.광천터미널이 시끄럽고 붐빈다면 길을 건너는 5분 간의 노력을 투자해서 여기를 오는 것을 추천합니다.','넓고 쾌적한 곳으로 직원들이 왕 친절합니다.','2층에 초밥가게도있어서 좋고 편하게 차한잔하기 좋아용~','스터디테이블있어서 편해요 마감시간 좀더 길었으면 좋겠어요','커피 맛이 좋다','좌석이 많아서 좋아요','카페가 공부할 수 있도록 자리를 만들어 놓은 느낌이다. 특히 음료시키면 주차도 2시간 무료닷','일층 엔제리너스 커피숍 인포에서 주문해서 일층,삼층,삼층가든 세곳에서 음료나 기타브런치등을 즐길수있고 바로 윗층은 맛있는 초밥집이있어 초밥,스시,사케,기타주류도 간단히 할수있어좋고 초밥을먹은경우 커피 숍에서 커피나음료 주문시 할인혜택도 쏠쏠했다. 숍에서 커피나음료 주문시 할인혜택도 쏠쏠했다.','공부하기 좋다. 겨울에는 좀 건조하다.','공간이 크고 생각보다 사람많이 없고 공부하기 좋아요. 밖의 테라스 금연인것도 좋고. 근데 흡연실에 환기가 잘 되었으면 더더 좋을듯 문 여닫힐때마다 담배냄새가 들어와서 쪼큼 싫었음.']
    sentense = ''
    for i in range(len(comment1)):
        user = User.objects.get(id=i+1)
        sentense += comment1[i]
        comment = Comment.objects.create(place=place, comment=comment1[i], review_user=user)
        comment.save()
    analysis = NLP_comment(sentense)
    result = json.dumps(analysis, ensure_ascii=False) 
    place.placekeyword = result
    place.save()
    cafe1 = [0, False, True, True, 36]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()
    menu2 = ['아메리카노',4300,'카페라떼',4800,'카푸치노',4800,'카페모카',5500,'바닐라 카페라떼',5500,'카라멜 마끼아또',5900,'콜드브루 커피',5200, '아메리치노',5100,'애플캐모마일/페퍼민트',4000,'녹차/얼그레이',4000,'레몬티/유자티',4000,'아이스티',4000,'그린티 라떼',5600,'오리지널 밀크티',5000,'로즈힙 밀크티',5000,'레모네이드',4000,'핫초코/아이스초코',4600,'자색고구마 라떼',5000]
    for i in range(0, len(menu2), 2):
        menu = Menu.objects.create(cafe=cafe, name=menu2[i], price=menu2[i+1])
        menu.save()
    
    

    place1 = [21223932, 35.2105342260774, 126.898464367035,'커피트리','광주 북구 일곡동일곡마을로 225','062-575-7232', False, 0, 2, 3, 0, '','00:00:00', '23:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    cafe1 = [0, False, True, False, 5]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    place1 = [26572310, 35.1607351937295, 126.882558663503,'스타벅스 신세계광주점','광주 서구 광천동무진대로 932','062-360-1137', True, 8, 13, 5, 4, '','07:00:00', '22:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['스타벅스신세계.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe1 = [0, False, True, False, 14]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    place1 = [1670959644, 35.2172895808253, 126.843278515835,'트리플커피 첨단본점','광주 광산구 월계동임방울대로 776','062-973-7714', True, 0, 3, 4, 0, '','10:00:00', '22:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['트리플커피1.jpg','트리플커피2.jpg','트리플커피3.jpg','트리플커피4.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe1 = [0, False, True, False, 0]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    place1 = [23447733, 35.2147335869172, 126.84346025606,'스타벅스 광주첨단점','광주 광산구 월계동첨단중앙로 104','062-971-8719', False, 10, 14, 10, 2, '','08:00:00', '22:00:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['스타벅스첨단1.jpg','스타벅스첨단2.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe1 = [0, False, True, False, 18]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    place1 = [1201123550, 35.2185481193323, 126.83728434813,'더치앤빈 광주첨단점','광주 광산구 월계동임방울대로 727-19','062-974-8646', False, 0, 10, 0, 0, '','09:00:00', '23:30:00',{}]
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13],placekeyword=place1[14])    
    place.save()
    placepicture1 = ['더치앤빈1.jpg','더치앤빈1.jpg','더치앤빈3.jpg']
    for i in range(0, len(placepicture1)):
        tempname = placeurl + placepicture1[i]
        placepicture = Placepicture.objects.create(place=place, name=tempname)
        placepicture.save()
    cafe1 = [0, False, True, False, 8]
    cafe = Cafe.objects.create(place=place, storearea=cafe1[0],alcoholonoff=cafe1[1],dessertonoff=cafe1[2],smokingroom=cafe1[3],powersoket=cafe1[4])
    cafe.save()

    return JsonResponse({"result":"true"}) 
