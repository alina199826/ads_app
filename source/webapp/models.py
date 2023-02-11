
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


STATUS = [('to_modern', 'на модерацию'), ('published', 'опубликовано'), ('rejected', 'отклонено'), ('to_delete', 'на удаление')]


class Ads(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='photos', verbose_name='фотография')
    text = models.CharField(max_length=50, null=False, blank=False, verbose_name='заголовок')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='описание')
    author = models.ForeignKey(get_user_model(), null=False, blank=False, on_delete=models.SET_DEFAULT, default=1,
                               related_name='author_ad',
                               verbose_name="Автор объявления")
    category = models.ForeignKey('webapp.Category', max_length=20, null=False, blank=False, on_delete=models.CASCADE,
                                verbose_name="категория")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="price")
    status = models.CharField(max_length=20, null=False, blank=False, choices=STATUS, default=STATUS[0][0],
                                verbose_name="статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        permissions = [("choice_ads", "Отбирать объявления")]

    def get_absolute_url(self):
        return reverse('webapp:ad_view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.pk}. {self.text}'

class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='категория')

class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='comments',
                               verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    ad = models.ForeignKey('webapp.Ads', on_delete=models.CASCADE, related_name='comments',
                                verbose_name="объявление")


    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'