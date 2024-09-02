from django.db import models

class NameOfPageChoice(models.IntegerChoices):
    R1 = 1, "الصفحة الرئيسية",
    R2 = 2, "المجتمع",
    R3 = 3,"العملاء",
    R4 = 4,"منسوبينا",
    R5 = 5,"خدماتنا",
    R6 = 6,"برنامج حصاد",
    R7 = 7,"مواقع الفروع",
    R8 = 8,"جديدنا",
    R9 = 9,"من نحن",

class TitleForPageChoice(models.IntegerChoices):
    R1 = 1, "المجتمع",
    R2 = 2,"العملاء",
    R3 = 3,"منسوبينا",
    R4 = 4,"خدماتنا",
    R5 = 5,"برنامج حصاد",
    R6 = 6,"من نحن",
    R7 = 7,"كيف تبي طلبك",
    R8 = 8,"من حقك تعرف ",