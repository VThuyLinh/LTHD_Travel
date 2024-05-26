from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

import enum


# Create your models here.


class DateGeneral(models.Model):
    DatePost = models.DateTimeField(auto_now_add=True, name='Ngày đăng')
    DateUpdate = models.DateTimeField(auto_now=True, name='Ngày cập nhật')

    class Meta:
        abstract = True


class VaiTro(enum.Enum):
    Staff = 1
    Customer = 2





class User(AbstractUser):
    password = models.CharField(max_length=300, null=False)
    sdt = models.CharField(max_length=10, null=False)
    address = models.TextField(max_length=300, null=True)
    vaitro = models.CharField(max_length=100, default=VaiTro.Customer)

    def __str__(self):
        self.username


class Staff(User):
    DateAdd = models.DateField(auto_now_add=True)


class Customer(User):
    Avatar = models.ImageField(upload_to='Travel/%Y/%m/', max_length=1000, null=False)

class Transport(models.Model):
    Name= models.TextField()
    License= models.CharField(max_length=15)
    def __str__(self):
        return self.Name

class Place(models.Model):
    Id_Place = models.CharField(max_length=20, unique=True, null=False)
    Place_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Place_Name


class Album(models.Model):
    Name= models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.Name

class Image(models.Model):
    Name= models.CharField(max_length=500, null= True)
    Path = CloudinaryField()
    Pic = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_date= models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.Name



class Tour(DateGeneral):
    Id_Tour = models.CharField(max_length=40, null=False)
    Tour_Name = models.CharField(max_length=100)
    Description= RichTextField()
    DeparturePlace = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='Place.Tour_set+')
    DepartureTime = models.DateTimeField(null=False)
    Destination = models.ForeignKey(Place, on_delete=models.CASCADE)
    Days = models.IntegerField()
    Nights = models.IntegerField()
    Active = models.BooleanField(default=True)
    vehicle= models.ForeignKey(Transport, on_delete=models.CASCADE, null=True, default="____")
    def __str__(self):
        return self.Id_Tour

class Tour_Image(DateGeneral):
    picture = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    tour= models.ForeignKey(Tour, on_delete=models.PROTECT, null=True)


class Price(models.Model):
    Adult = models.FloatField()
    Children = models.FloatField()


class News(DateGeneral):
    Name_News = models.CharField(max_length=600, null=False)
    Content= RichTextField()



class CMT(DateGeneral):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()

    class Meta:
        abstract = True


class CMT_News(CMT):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('news', 'user')

class CMT_Tour(CMT):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    class Meta:
        unique_together = ('tour', 'user')


class Rating_Tour(DateGeneral):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NumberOfStart = models.IntegerField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Like_Tour(Like):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tour', 'user')


class Like_News(Like):
    news = models.ForeignKey(News, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('news', 'user')
