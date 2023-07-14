from rest_framework.serializers import ModelSerializer

from tarasivka.settings import MAIN_DOMAIN
from .models import *
from environs import Env

env = Env()
env.read_env()


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
        images = []
        for d in data:
            images.append(MAIN_DOMAIN + d['image'])
        return images

    def get_characteristic(self, obj):
        characteristic = Characteristic.objects.filter(product=obj)
        i = CharacteristicSerializer(instance=characteristic, many=True)
        chars = {}
        for k in i.data:
            chars.update({k['name']: k['meaning']})
        return chars

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


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

    def edit_ckeditor(self, obj):
        about = About.objects.all().first()
        context = about.context

        new_context = context.replace("src=\"", f"src=\"{env.str('MAIN_DOMAIN')}")
        return new_context

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['context'] = self.edit_ckeditor(instance)
        return ret


class SliderSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = ("image",)

