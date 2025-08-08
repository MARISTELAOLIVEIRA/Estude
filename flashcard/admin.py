from django.contrib import admin
from .models import Categoria, Flashcard, Desafio, FlashcardDesafio

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(Desafio)
admin.site.register(FlashcardDesafio)
# This code registers the Categoria and Flashcard models with the Django admin site,
