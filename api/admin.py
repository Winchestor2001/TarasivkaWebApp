from django.contrib import admin

from .models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1


class GalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'phone_number']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name']
    exclude = ('vendor_code',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # exclude = ('vendor_code',)
    list_display = ['name', 'price', 'available', 'type']

    inlines = [CharacteristicInline, GalleryInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['social', 'link']

