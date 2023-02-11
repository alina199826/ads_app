from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    phone = PhoneNumberField()

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return f"{self.user.username} 's Profile"

    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'