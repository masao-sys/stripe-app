from django.db import models


class UserType(models.TextChoices):
    FREE = 'FREE', '無料'
    PAID = 'PAID', '有料'
    SUPPORTER = 'SUPPORTER', 'サポーター'
