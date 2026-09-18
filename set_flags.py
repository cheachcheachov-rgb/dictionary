import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dictionary.settings')
django.setup()

from words.models import Word

# Соответствие языка и файла флага
FLAGS = {
    'en': 'word_images/angl.jpg',
    'de': 'word_images/germ.jpg',
    'fr': 'word_images/fran.jpg',
    'es': 'word_images/ispan.jpg',
    'it': 'word_images/ital.jpg',
}

updated = 0
for word in Word.objects.all():
    if word.language in FLAGS:
        word.image = FLAGS[word.language]
        word.save()
        updated += 1

print(f"Обновлено слов: {updated}")
print(f"Всего слов в базе: {Word.objects.count()}")