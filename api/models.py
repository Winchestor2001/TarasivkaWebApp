from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'


class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200, verbose_name='назва')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Product(models.Model):
    TYPE = (
        ('Топ продажів', 'Топ продажів'),
        ('новинка', 'новинка'),
    )
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    name = models.CharField(max_length=200, verbose_name='Назва')
    description = RichTextUploadingField(verbose_name='Опис', null=True, blank=True)
    price = models.FloatField(default=0, verbose_name='Ціна')
    discount = models.FloatField(default=0, verbose_name='Знижка')
    available = models.BooleanField(default=True, verbose_name='Доступний')
    type = models.CharField(max_length=100, choices=TYPE, verbose_name='Типу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Галерея товарів'
        verbose_name_plural = 'Галерея товарів'


class Contact(models.Model):
    location = models.TextField(verbose_name='Місцезнаходження')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефону')
    email = models.CharField(max_length=100, verbose_name='Почта', blank=True, null=True)

    def __str__(self):
        return "Contact"

    class Meta:
        verbose_name = 'Кконтакт'
        verbose_name_plural = 'Контакти'


class About(models.Model):
    context = RichTextUploadingField(verbose_name='Приблизно')

    def __str__(self):
        return "Приблизно"

    class Meta:
        verbose_name = 'Приблизно'
        verbose_name_plural = 'Приблизни'


class SocialLink(models.Model):
    SOCIAL = (
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('telegram', 'telegram'),
        ('instagram', 'instagram'),
        ('youtube', 'youtube')
    )
    social = models.CharField(max_length=50, choices=SOCIAL, verbose_name='Соціальні')
    link = models.CharField(max_length=100, verbose_name='Посилання')

    def __str__(self):
        return "Social"

    class Meta:
        verbose_name = 'Соціальне посилання'
        verbose_name_plural = 'Соціальні посилання'


class Characteristic(models.Model):
    CHARS = (
        ('Вага', 'Вага'),
        ('Штук', 'Штук'),
        ('Тип м’яса', 'Тип м’яса'),
        ('Гатунок', 'Гатунок'),
        ('Термін придатності', 'Термін придатності'),
        ('ТУ', 'ТУ'),
        ('Оболонка/тара', 'Оболонка/тара'),
        ('Пакування', 'Пакування'),
        ('Температура зберігання', 'Температура зберігання'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=100, verbose_name='Назва', choices=CHARS)
    meaning = models.CharField(max_length=100, verbose_name='Значення')

    def __str__(self):
        return "{}".format(self.product)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return "Slider"

    class Meta:
        verbose_name = 'Зображення слайдера'
        verbose_name_plural = 'Зображення слайдера'

