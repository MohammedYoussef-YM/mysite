from django.db import models
from .choices import *

# Create your models here.

class slide(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.ImageField(upload_to='img')
    name_page= models.IntegerField(choices=NameOfPageChoice.choices,default=NameOfPageChoice.R1)
    title = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'
    class Meta:
        verbose_name = "السلايد"
        verbose_name_plural = "السلايدات"

class YourOrder(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img')
    url = models.URLField()
   
    def __str__(self):
        return f'{self.id}: {self.image}'
    class Meta:
        verbose_name = "كيف تبي طلبك"
        verbose_name_plural = "كيف تبي طلبك"
        
class mustKnow(models.Model):
    id = models.AutoField(primary_key=True)
    video_url = models.FileField(upload_to='vid')

    class Meta:
        verbose_name = "من حقك تعرف"
        verbose_name_plural = "من حقك تعرف"
        
class lastOffers(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    video_url = models.FileField(upload_to='vid')

    class Meta:
        verbose_name = "آخر عرض"
        verbose_name_plural = "آخر العروض"

class globalQuality(models.Model):
    id = models.AutoField(primary_key=True)
    image_cirtificate_1 = models.ImageField(upload_to='img')
    image_cirtificate_2 = models.ImageField(upload_to='img')
    image_cover = models.ImageField(upload_to='img')
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "الجودة العالمية"
        verbose_name_plural = "الجودة العالمية"
        
class communityService(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='img')

   
    def __str__(self):
        return f'{self.id}: {self.title}'       
    class Meta:
        verbose_name = "خدمة المجتمع"
        verbose_name_plural = "خدمة المجتمع"
        
class downloadApp(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img')
    image_android_app = models.ImageField(upload_to='img')
    image_apple_app = models.ImageField(upload_to='img')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "حمل التطبيق"
        verbose_name_plural = "حمل التطبيق"
        
class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=555)
    answer = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "المجتمع"
        verbose_name_plural = "المجتمع"
        
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=555)
    answer = models.TextField()


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "العملاء"
        verbose_name_plural = "العملاء"
        
class Members(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=555)
    answer = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "منسوبينا"
        verbose_name_plural = "منسوبينا"      
        
class Services(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255,default="100")
    number = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title        
    class Meta:
        verbose_name = "خدماتنا"
        verbose_name_plural = "خدماتنا"
        
class Hasad(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=555)
    answer = models.TextField()

    def __str__(self):
        return self.title        
    class Meta:
        verbose_name = "حصاد"
        verbose_name_plural = "برنامج حصاد"

class locationBranch(models.Model):
    id = models.AutoField(primary_key=True)
    branch = models.CharField(max_length=100,default="الفرع الرئيسي")
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title        
    class Meta:
        verbose_name = "مواقع الفروع"
        verbose_name_plural = "مواقع الفروع"
        
class offers(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=255,default="percent")
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.CharField(max_length=100,default="صالح حتى 30 سبتمبر")

    def __str__(self):
        return self.title        
    class Meta:
        verbose_name = "عروض خاصة"
        verbose_name_plural = "عروض خاصة"
        
class news(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title        
    class Meta:
        verbose_name = "اخبار المطعم"
        verbose_name_plural = "اخبار المطعم"
               
class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
            
    class Meta:
        verbose_name = "من نحن"
        verbose_name_plural = "من نحن"
        
class TitleForPageChoice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    name_page = models.IntegerField(choices=TitleForPageChoice.choices,default=TitleForPageChoice.R1)

    def __str__(self):
        return self.title      

    class Meta:
        verbose_name = "عنوان الصفحة"
        verbose_name_plural = "عناوين الصفحات"
        