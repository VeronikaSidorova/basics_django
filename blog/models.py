from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview_image = models.ImageField(
        upload_to="blog/image",
        null=True,
        blank=True,
        verbose_name="Превью (изображение)",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views_count += 1
        self.save()
        # Отправка письма при достижении 100 просмотров
        if self.views_count == 18:
            send_mail(
                "Достижение 100 просмотров",
                f'Статья "{self.title}" достигла 100 просмотров!',
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=True,
            )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Посты"
        permissions = [
            ("can_edit_post", "Can edit post"),
            ("can_delete_post", "Can delete post"),
        ]
