from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class TempUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'age', 'ceo', 'registrationnumber', 'name', 'noise1', 'noise2', 'noise3', 'light1', 'light2', 'light3', 'seat1', 'seat2', 'seat3',]

class Placename(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'placename', 'placeid',]

class MypageSerializer(serializers.ModelSerializer):
    place = Placename(source='place_like', many=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'age', 'ceo', 'registrationnumber', 'name', 'noise1', 'noise2', 'noise3', 'light1', 'light2', 'light3', 'seat1', 'seat2', 'seat3','place']

class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['noise1', 'noise2', 'noise3', 'light1', 'light2', 'light3', 'seat1', 'seat2', 'seat3']
    

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class UserreviewSerializer(serializers.ModelSerializer):
    review_user = TempUserSerializer()
    class Meta:
        model = Userreview
        fields = ['id', 'review_user', 'place', 'noise', 'light', 'seat']

class TempUserreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userreview
        fields = ['noise', 'light', 'seat']

class OneUserAllreviewSerializer(serializers.ModelSerializer):
    review = TempUserreviewSerializer(source='place_userreview', many=True)
    class Meta:
        model = Place
        fields = ['review']

class StudycafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studycafe
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
# class MenuSerializer(serializers.HyperlinkedModelSerializer):
    # menupicture = serializers.ImageField(use_url=True)
    class Meta:
        model = Menu
        fields = ['name', 'price',]

class CafeSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(source='cafe_set', many=True)
    class Meta:
        model = Cafe
        fields = ['id', 'storearea', 'alcoholonoff', 'dessertonoff','smokingroom', 'powersoket', 'menu', 'subdetail']

# class PlacepictureSerializer(serializers.ModelSerializer):
class TempPlacepicture(serializers.HyperlinkedModelSerializer):
    # image = serializers.ImageField(use_url=True)
    class Meta:
        model = Placepicture
        fields = ['name']


class TempComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment',]

class CommentSerializer(serializers.ModelSerializer):
    review_user = TempUserSerializer()
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Comment
        # fields = ['id', 'review_user', 'comment', 'create_at',]
        fields = '__all__'

class YYEPlaceSerializer(serializers.ModelSerializer):
    cafe = CafeSerializer(source='place_cafe', many=True)
    library = LibrarySerializer(source='place_library', many=True)
    studycafe = StudycafeSerializer(source='place_studycafe', many=True)
    placepicture = TempPlacepicture(source='placepicutre_set', many=True)
    comments = CommentSerializer(source='comment_set', many=True)
    like_users = UserSerializer(many=True)
    review = UserreviewSerializer(source='place_userreview', many=True)
    class Meta:
        model = Place        
        fields = ['id', 'library', 'cafe', 'studycafe', 'latitude', 'longitude', 'placeid', 'placename', 'review', 'location','phonenumber','placepicture','parkinglot','tableinfo1','tableinfo2','tableinfo4','tableinfo5','opentime','closetime', 'like_users', 'comments', 'placekeyword']

class PlaceCommentSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    class Meta:
        model = Place
        fields = ['comment',]

class PlaceSerializer(serializers.ModelSerializer):
    cafe = CafeSerializer(source='place_cafe', many=True)     
    placepicture = TempPlacepicture(source='placepicutre_set', many=True)
    class Meta:
        model = Place        
        fields = ['cafe', 'location', 'placepicture', 'phonenumber','parkinglot','tableinfo1','tableinfo2','tableinfo4','tableinfo5','opentime','closetime', ]
    # def create(self, validated_data):
    #     placepictures = validated_data.pop('placepicture', [])
    #     instance = Place.objects.create(**validated_data)
    #     for placepicture_data in placepictures:
    #         placepicture = Placepicture.objects.get(pk=placepicture_data.get('id'))
    #         instance.tasks.add(placepicture)
    #     return instance

    # def update(self, instance, validated_data):
    #     placepictures = validated_data.pop('placepicture', [])
    #     instance = super().update(instance, validated_data)
    #     for placepicture_data in placepictures:
    #         placepicture = Placepictures.objects.get(pk=placepicture_data.get('id'))
    #         instance.tasks.add(placepicture)
    #     return instance 



# like
class LikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id',]

class LikePlaceSerializer(serializers.ModelSerializer):
    like_users = LikeUserSerializer(many=True)
    class Meta:
        model = Place
        fields = ['like_users']

# class comSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = com
#         fields = '__all__'

# class BoardS(serializers.ModelSerializer):
#     comm = comSerializer(source="board_set", many=True)
#     class Meta:
#         model = Board
#         fields = ['comm', 'name']

