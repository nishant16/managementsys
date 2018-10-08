# comment
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from hotels.models import Hotel, Customer, Staff
from .serializers import HotelSerializer, CustomerSerializer, StaffSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import list_route, detail_route


class HotelView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def list(self, request):
        """
        Return a list of all users.
        """
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        hotel = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(hotel)  # object of the model is passed when serialize(content type converted to python datatype )
        return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  # here the create method of serializer will call and save
            return Response({'status': 'Hotel name registered successfully'})

    def partial_update(self, request, pk=None):
        hotel = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Hotel name changed successfully'})

    @detail_route(methods=['POST'])
    def pswrd(self, request, pk=None):
        # just a dummy not doing anything
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'status': 'Password set successfully'})

        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
