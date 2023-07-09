from rest_framework.serializers import ModelSerializer

from tarasivka.settings import MAIN_DOMAIN
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'name')


class ProductGallerySerializer(ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ('image',)


class CharacteristicSerializer(ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('name', 'meaning')


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def get_images(self, obj):
        images = ProductGallery.objects.filter(product=obj)
        i = ProductGallerySerializer(instance=images, many=True)
        data = i.data
        for d in data:
            d['image'] = MAIN_DOMAIN + d['image']
        return data

    def get_characteristic(self, obj):
        characteristic = Characteristic.objects.filter(product=obj)
        i = CharacteristicSerializer(instance=characteristic, many=True)
        return i.data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['images'] = self.get_images(instance)
        ret['characteristic'] = self.get_characteristic(instance)
        return ret


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('location', 'phone_number')


class SocialLinkSerializer(ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ('social', 'link')

