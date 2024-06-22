from django.contrib.auth.hashers import make_password
from django.db import models
from ckeditor.fields import RichTextField


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


class VaiTro(models.TextChoices):
    Staff = "Staff"
    Customer = "Customer"
    Admin="Admin"

class StateOfOrder(models.TextChoices):
    WaitforPaid="Wait for Paid"
    Paid = "Paid"
    Complete = "Complete"
    Reject ="Reject"



class User(AbstractUser):

    password = models.CharField(max_length=300, null=False)
    sdt = models.CharField(max_length=10, null=False)
    address = models.TextField(max_length=300, null=True)
    # vaitro = models.CharField(max_length=100, default=VaiTro.Customer)
    vaitro= models.CharField(choices=VaiTro.choices, max_length=30, default="Customer")
    Avatar = models.ImageField(upload_to='Travel/%Y/%m/', max_length=1000, null=False)
    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Staff(User):
    DateAdd = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Staff"


class Customer(User):

    class Meta:
        verbose_name = "Customer"
class Transport(models.Model):
    Name= models.TextField()
    License= models.CharField(max_length=15)
    def __str__(self):
        return "%s %s"% (self.Name,self.License)

class Place(models.Model):
    Id_Place = models.CharField(max_length=20, unique=True, null=False)
    Place_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Place_Name


class Image(models.Model):
    Name= models.CharField(max_length=500, null= True)
    Path = models.ImageField(upload_to='imageForTour/%Y/%m')

    created_date= models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.Name

class Album(models.Model):
    Name= models.CharField(max_length=500, null=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    image_id= models.ManyToManyField(Image)
    def __str__(self):
        return self.Name





class Schedule(DateGeneral):
    DepartureDay= models.DateField(auto_now_add=True)
    def __str__(self):
        return  str(self.DepartureDay)

class Tour(DateGeneral):
    Id_Tour = models.CharField(max_length=40, null=False)
    Tour_Name = models.CharField(max_length=100)
    Description= RichTextField()
    DeparturePlace = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='Place.Tour_set+')
    DepartureTime = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    Destination = models.ForeignKey(Place, on_delete=models.CASCADE)
    Days = models.IntegerField()
    Nights = models.IntegerField()
    Active = models.BooleanField(default=True)
    vehicle= models.ForeignKey(Transport, on_delete=models.CASCADE, null=True, default="____")
    Adult_price= models.FloatField(null=True, default=0)
    Children_price = models.FloatField(null=True, default=0)
    album= models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.Tour_Name



class News(DateGeneral):
    Name_News = models.CharField(max_length=600, null=False)
    image_thumbnail= models.ImageField(upload_to='news/%Y/%m')
    active=models.BooleanField(default=True)
    Content= RichTextField()


    def __str__(self):
        return self.Name_News




class CMT(DateGeneral):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()

    class Meta:
        abstract = True


class CMT_News(CMT):
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.content, self.user, self.news)

class CMT_Tour(CMT):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s %s" % (self.content, self.user, self.tour)


class Rating_Tour(DateGeneral):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NumberOfStart = models.IntegerField()

    class Meta:
        unique_together = ('tour', 'user')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Like_Tour(Like):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    Active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('tour', 'user')


class Like_News(Like):
    news = models.ForeignKey(News, on_delete=models.PROTECT)
    Active= models.BooleanField(default=False)

    class Meta:
        unique_together = ('news', 'user')





class BookTour(models.Model):
    id_customer_bt=models.ForeignKey(Customer, on_delete=models.CASCADE)
    book_date=models.DateTimeField(auto_now=True)
    FirstName_BookTour= models.CharField(max_length=20,default="")
    LastName_BookTour = models.CharField(max_length=20, default="")
    Phone_BookTour = models.CharField(max_length=10, default="")
    Email_BookTour = models.CharField(max_length=50, default="")
    DeparturePlace = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='Place.Tour_set+')
    DepartureTime = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    Destination = models.ForeignKey(Place, on_delete=models.CASCADE)
    Days = models.IntegerField()
    Nights = models.IntegerField()
    vehicle = models.ForeignKey(Transport, on_delete=models.CASCADE, null=True, default="____")
    id_tour_id= models.ForeignKey(Tour,on_delete=models.PROTECT)
    Quantity_Adult= models.IntegerField(default=1)
    Quantity_Children= models.IntegerField(default=0)
    State= models.CharField(choices=StateOfOrder.choices,max_length=50)

# class Paid(DateGeneral):
#     id_booktour= models.ForeignKey(BookTour, on_delete=models.CASCADE)



