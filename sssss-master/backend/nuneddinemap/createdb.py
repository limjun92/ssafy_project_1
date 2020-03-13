from .models import Place


def sss():
    place1 = [26910025, 35.1751491987338, 126.915321920255,'투썸플레이스 광주전남대점','광주 북구 중흥동호동로 25','062-268-2388', False, 1, 2, 22, 5, '나만의 즐거움을 만날 수 있는 프리미엄 디저트 카페 A Twosome Place','10:00:00', '02:00:00']
    place = Place.objects.create(placeid=place1[0],latitude=place1[1],longitude=place1[2],placename=place1[3],location=place1[4],phonenumber=place1[5],parkinglot=place1[6],tableinfo1=place1[7],tableinfo2=place1[8],tableinfo4=place1[9],tableinfo5=place1[10],surroundinginformation=place1[11],opentime=place1[12],closetime=place1[13])    
    place.save()


sss()

