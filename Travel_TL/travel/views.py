import datetime

from django.shortcuts import render
from rest_framework import viewsets, generics, status, parsers, permissions
from travel.models import *
from travel import serializers,perm
import datetime
from rest_framework.decorators import action
from rest_framework.response import Response
from travel import  paginators



# Create your views here.
class TourViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Tour.objects.filter(Active=True)
    serializer_class = serializers.TourSerializer
    pagination_class = paginators.TourPaginator
    def get_queryset(self):
        queryset= self.queryset
        q= self.request.query_params.get('Price')
        if q:
            queryset=queryset.filter( Adult_price=float(q))

        DeparturePlace =self.request.query_params.get('noidi')
        Destination= self.request.query_params.get('noiden')
        if DeparturePlace :
            queryset=queryset.filter(DeparturePlace__Place_Name__icontains=DeparturePlace)
        if Destination:
            queryset = queryset.filter(Destination__Place_Name__icontains=Destination)
        DepartureTime= self.request.query_params.get('thoigiandi')

        if DepartureTime:
            queryset=queryset.filter(DepartureTime__DepartureDay__icontains=DepartureTime)
        return queryset



# class AlbumViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset = Album.objects.all()
#     serializer_class = serializers.AlbumSerializer
#     def get_queryset(self):
#         queryset= self.queryset
#         q= self.request.query_params.get('q')
#         if q:
#             queryset=queryset.filter(Tour_Name__icontains=q)
#         return queryset


class AlbumViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Album.objects
    serializer_class = serializers.AlbumSerializer

class TourViewSetDetail(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Tour.objects.filter(Active=True)
    serializer_class = serializers.TourSerializerDetail


    @action(methods=['post'],url_path='create_cmt_tour' , detail=True)
    def create_cmt_tour(self,request,pk):
        cmt_tour= self.get_object().cmt_tour_set.create(content=request.data.get('content'), user=request.user)
        return Response(serializers.CMT_TourSerializer(cmt_tour).data)

    @action(methods=['post'], url_path='create_rating_tour', detail=True)
    def create_rating_tour(self, request, pk):
        rating_tour = self.get_object().rating_tour_set.create(NumberOfStart=request.data.get('NumberOfStart'), user=request.user)
        return Response(serializers.CMT_TourSerializer(rating_tour).data)

    @action(methods=['get'], url_path='get_like_tour', detail=True)
    def like_tour(self, request, pk):
        like_tour = Like_Tour.objects
        return Response(serializers.Like_TourSerializer(like_tour, many=True).data)

    @action(methods=['post'], url_path='like_tour', detail=True)
    def like(self, request, pk):
        li, created = Like_Tour.objects.get_or_create(tour=self.get_object(),
                                                      user=request.user)

        if not created:
            li.Active = not li.Active
            li.save()

        return Response(serializers.TourSerializerDetail(self.get_object()).data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get', 'patch'], url_path='current-user', detail=False)
    def get_current_user(self, request):
        user = request.user
        if request.method.__eq__('PATCH'):
            for k, v in request.data.items():
                setattr(user, k, v)
            user.save()

        return Response(serializers.UserSerializer(user).data)



class NewsViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = News.objects.filter(active=True)
    serializer_class = serializers.NewsSerializer
    def get_queryset(self):
        queryset= self.queryset
        q= self.request.query_params.get('news')
        if q:
            queryset=queryset.filter( Name_News=q)
        return  queryset






class NewsDetailViewSet(viewsets.ViewSet,generics.RetrieveAPIView):
    queryset = News.objects
    serializer_class = serializers.NewsDetailSerializer

    @action(methods=['post'], url_path='create_cmt_news', detail=True)
    def create_cmt_tour(self, request, pk):
        cmt_news = self.get_object().cmt_news_set.create(content=request.data.get('content'), user=request.user)
        return Response(serializers.CMT_NewsSerializer(cmt_news).data)

    @action(methods=['post'], url_path='like_news', detail=True)
    def like(self, request, pk):
        li, created = Like_News.objects.get_or_create(news=self.get_object(),
                                                 user=request.user)

        if not created:
            li.Active = not li.Active
            li.save()

        return Response(serializers.NewsDetailSerializer(self.get_object()).data, status=status.HTTP_201_CREATED)


class BookTourViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = BookTour.objects
    serializer_class = serializers.BookTourSerializer
    parser_classes = [parsers.MultiPartParser, ]

    @action(methods=['delete'], url_path='delete_booktour', detail=True)
    def delete(self, request, pk):
        queryset = BookTour.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePasswordViewSet(viewsets.ViewSet,generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer


# class DeleteUserViewSet(viewsets.ViewSet, generics.DestroyAPIView):

class StaffViewSet(viewsets.ViewSet, generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser, ]
    def get_queryset(self):
        queryset= self.queryset
        ten = self.request.query_params.get('Name')
        if ten:
            queryset=queryset.filter(last_name__icontains=ten)
        return queryset

    @action(methods=['delete'], url_path='delete_staff', detail=True)
    def delete(self, request, pk):
        queryset = User.objects.filter(vaitro="VaiTro.Staff")
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], url_path='get_staff', detail=True)
    def get_staff(self, request, pk):
        staffs = User.objects.get(pk=pk)
        return Response(serializers.UserSerializer(staffs).data,
                        status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset = Customer.objects
    serializer_class = serializers.CustomerSerializer

class BookTourDetailViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = BookTour.objects
    serializer_class = serializers.BookTourSerializer


class CMT_TourViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = CMT_Tour.objects.all()
    serializer_class = serializers.CMT_TourSerializer
    permission_classes = [perm.CMTOwner]

class CMT_NewsViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = CMT_News.objects.all()
    serializer_class = serializers.CMT_NewsSerializer
    permission_classes = [perm.CMTOwner]

class Rating_TourViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Rating_Tour.objects.all()
    serializer_class = serializers.RatingTourSerializer
    permission_classes = [perm.CMTOwner]
