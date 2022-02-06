from django.db import models

from datetime import datetime
from django.contrib import admin
from django.urls import reverse


class Blog(models.Model):

    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содежание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"      # имя таблицы для модели
        ordering = ["-posted"]  # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога"           # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога"    # тоже для всех статей блога


admin.site.register(Blog)
