from django.contrib.auth.password_validation import validate_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from travel.models import *


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['Name','License']

class DeparturePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['Place_Name']

class DepartureTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['DepartureDay']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image
        fields=['Path']

class AlbumSerializer(serializers.ModelSerializer):
    image= serializers.SerializerMethodField()
    def get_image(self, pk):
        image1=pk.image_id.all()
        return [{'Name':a.Name, 'Path': str(a.Path)} for a in image1]
    class Meta:
        model= Album
        fields=['id','image']



class TourSerializer(serializers.ModelSerializer):
    vehicle = TransportSerializer()
    # DeparturePlace=DeparturePlaceSerializer()
    # Destination= DeparturePlaceSerializer()
    DepartureTime=DepartureTimeSerializer()
    class Meta:
        model = Tour
<<<<<<< HEAD
        fields = ['Id_Tour', 'Tour_Name', 'DeparturePlace','Destination' ,'vehicle','DepartureTime','Ngày đăng']
=======
        fields = ['id','Id_Tour', 'Tour_Name', 'DeparturePlace','Destination' ,'vehicle','DepartureTime','DatePost']
>>>>>>> b307bd4109546f830f90cea27ab160ddd99e2d12





class TourSerializerDetail(serializers.ModelSerializer):
    vehicle = TransportSerializer()
    DeparturePlace = DeparturePlaceSerializer()
    Destination = DeparturePlaceSerializer()
    DepartureTime = DepartureTimeSerializer()
    cmt_tour=serializers.SerializerMethodField()
    rating_tour=serializers.SerializerMethodField()
    album= AlbumSerializer()

    def get_cmt_tour(self,pk):
        tour_cmt=pk.cmt_tour_set.all()
        return [{'user':a.user.first_name + " "+a.user.last_name,'content':a.content} for a in tour_cmt]

    def get_rating_tour(self,pk):
        tour_rating=pk.rating_tour_set.all()
        return [{'user':rt.user.first_name+" "+rt.user.last_name,'NumberOfStart':rt.NumberOfStart} for rt in tour_rating]
    class Meta:
        model = Tour
        fields = ['album','cmt_tour','rating_tour','Id_Tour', 'Tour_Name', 'DeparturePlace','Destination' ,'vehicle','DepartureTime','Description','Days','Nights','Adult_price','Children_price']





class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'address','vaitro','Avatar']
=======
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'address']
>>>>>>> b307bd4109546f830f90cea27ab160ddd99e2d12
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class CustomerSerializer(UserSerializer):
    class Meta:
        model = Customer
        fields =['Avatar']


class StaffSerializer(UserSerializer):
    class Meta:
        model = Staff
        fields = UserSerializer.Meta.fields + ['DateAdd']


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['password']

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance



class BookTourSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookTour
        fields = ['FirstName_BookTour','LastName_BookTour','Phone_BookTour','Email_BookTour', 'id_tour_id', 'Quantity_Adult', 'Quantity_Children', 'State']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar', 'address','vaitro']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['Name_News','Content']

class Like_TourSerializer(serializers.ModelSerializer):
    tour= TourSerializer()
    class Meta:
        model= Like_Tour
        fields=['tour','Active']

class Like_NewsSerializer(serializers.ModelSerializer):
    news= NewsSerializer()
    class Meta:
        model= Like_News
        fields=['news','Active']



class CMTSerializer(serializers.ModelSerializer):
    class Meta:
        model= CMT
        fields=['content','user']

class RatingTourSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating_Tour
        fields='__all__'
class CMT_TourSerializer(serializers.ModelSerializer):
    class Meta:
        model=CMT_Tour
        fields= CMTSerializer.Meta.fields+['tour']

class CMT_NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CMT_News
        fields= CMTSerializer.Meta.fields+['news']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields= ['Name_News','image_thumbnail']

class NewsDetailSerializer(NewsSerializer):
    class Meta:
        model=News
        fields= NewsSerializer.Meta.fields+['Content']