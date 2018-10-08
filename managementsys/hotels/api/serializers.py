# comment
from rest_framework import serializers
from hotels.models import Hotel, Customer


class HotelSerializer(serializers.ModelSerializer):
    staff_set = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Hotel
        # fields = '__all__'
        fields = ('name', 'staff_set')

    # def create(self, validated_data):
    #     print "create"
    #     return None  # return the instance


    # def update(self, hotel, validated_data):
    #     hotel.name = validated_data.get('name', hotel.name)
    #     hotel.save()
    #     return hotel

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'mobile_no', 'hotel')


class StaffSerializer(serializers.Serializer):
    mobile_no = serializers.CharField()



