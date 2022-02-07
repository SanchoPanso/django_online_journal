from django.db import models

from datetime import datetime
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User


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


# Модель комментариев
class Comment(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Дата")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Статья")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям блога"
        ordering = ["-date"]


admin.site.register(Blog)
admin.site.register(Comment)
