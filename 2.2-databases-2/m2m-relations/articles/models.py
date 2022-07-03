from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    themes = models.ManyToManyField('Theme', through='ArticleScope',
                                    through_fields=('article', 'theme', 'is_main')
                                    )


    class Meta:
        db_table = 'Articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Theme(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название темы')

    class Meta:
        db_table = 'Themes'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    is_main = models.BooleanField(verbose_name='Основная тема')

    class Meta:
        db_table = 'articles and themes'