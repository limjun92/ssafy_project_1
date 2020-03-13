from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import settings

class User(AbstractUser):
    age = models.IntegerField(
        validators=(MinValueValidator(0, '올바른 나이를 입력해주세요.'),
                    MaxValueValidator(150, '올바른 나이를 입력해주세요.')),
        default=25
    )
    ceo = models.BooleanField(default=False)
    registrationnumber = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    noise1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    noise2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    noise3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    light1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    light2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    light3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    seat1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    seat2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    seat3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], null=True, default=1)
    # light1 = models.TextField(null=True)

    def __str__(self):
        return self.username

# class Question(models.Model):
#     title = models.CharField(max_length=100)
#     choice_1 = models.CharField(max_length=100)
#     choice_2 = models.CharField(max_length=100)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     pick = models.IntegerField()
#     comment = models.CharField(max_length=100)

class Place(models.Model):
    placeid = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    placename = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True) # 위치
    phonenumber = models.CharField(max_length=100, blank=True, null=True)  # 전화번호
    parkinglot = models.BooleanField(default=False) #주차장
    tableinfo1 = models.IntegerField(blank=True, null=True)
    tableinfo2 = models.IntegerField(blank=True, null=True)
    tableinfo4 = models.IntegerField(blank=True, null=True)
    tableinfo5 = models.IntegerField(blank=True, null=True)
    
    surroundinginformation = models.CharField(max_length=100, blank=True, null=True) # 주변정보
    # opentime = models.IntegerField(blank=True, null=True) # 오픈 시간
    # closetime = models.IntegerField(blank=True, null=True) # 닫는 시간
    opentime = models.TimeField(blank=True, null=True)
    closetime = models.TimeField(blank=True, null=True)
    
    like_users = models.ManyToManyField(User, related_name="place_like", blank=True, null=True)
    placekeyword = models.TextField(blank=True, null=True)
    # def __str__(self):
    #     return self.placename

class Studycafe(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_studycafe', blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

class Library(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_library', blank=True, null=True)
    convenience = models.BooleanField(default=False)
    notebook = models.BooleanField(default=False)

class Cafe(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_cafe', blank=True, null=True)
    storearea = models.FloatField(default=False) # 매장 넓이
    alcoholonoff = models.BooleanField(default=False)# 알콜판매
    dessertonoff = models.BooleanField(default=False)
    smokingroom = models.BooleanField(default=False)
    powersoket = models.IntegerField(blank=True, null=True)
    subdetail = models.CharField(max_length=500, default=False)

class Menu(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="cafe_set", blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    # info = models.CharField(max_length=500, blank=True, null=True)
    # menupicture = models.CharField(max_length=500, blank=True, null=True)    
    def __str__(self):
        return self.name

class Placepicture(models.Model): 
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='placepicutre_set', blank=True, null=True)    
    name = models.CharField(max_length=1000)

class Userreview(models.Model):
    review_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_userreview", blank=True, null=True)
    noise = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    light = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    seat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    
class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='comment_set', blank=True, null=True)
    comment = models.CharField(max_length=100)
    review_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} : {}".format(self.place, self.comment)

# class Board(models.Model):
#     name = models.CharField(max_length=100)

# class com(models.Model):
#     name = models.CharField(max_length=100)
#     board = models.ForeignKey(Board,on_delete=models.CASCADE, related_name="board_set")
