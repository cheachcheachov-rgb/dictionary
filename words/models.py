from django.db import models
from django.urls import reverse


class Word(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'Английский'),
        ('de', 'Немецкий'),
        ('fr', 'Французский'),
        ('es', 'Испанский'),
        ('it', 'Итальянский'),
    ]

    word = models.CharField(max_length=100, verbose_name="Слово")
    translation = models.CharField(max_length=200, verbose_name="Перевод")
    example = models.TextField(verbose_name="Пример использования")
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, verbose_name="Язык")
    image = models.ImageField(upload_to='word_images/', verbose_name="Изображение", null=True, blank=True)

    def __str__(self):
        return f"{self.word} — {self.translation}"

    def get_absolute_url(self):
        return reverse('word-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        ordering = ['word']