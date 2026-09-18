from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from rest_framework import generics

from .models import Word
from .forms import WordForm, RegisterForm
from .serializers import WordSerializer


class WordListView(ListView):
    model = Word
    template_name = 'words/word_list.html'
    context_object_name = 'words'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.GET.get('lang')
        if lang:
            queryset = queryset.filter(language=lang)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_lang'] = self.request.GET.get('lang', '')
        return context


class WordDetailView(DetailView):
    model = Word
    template_name = 'words/word_detail.html'
    context_object_name = 'word_obj'


def trainer(request):
    words = list(Word.objects.all())
    return render(request, 'words/trainer.html', {'words': words})


@staff_member_required
def edit_words(request):
    return render(request, 'words/edit_words.html', {'words': Word.objects.all()})


@staff_member_required
def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('edit-words')
    else:
        form = WordForm()
    return render(request, 'words/word_form.html', {'form': form, 'title': 'Добавить слово'})


@staff_member_required
def edit_word(request, id):
    word = get_object_or_404(Word, id=id)
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES, instance=word)
        if form.is_valid():
            form.save()
            return redirect('edit-words')
    else:
        form = WordForm(instance=word)
    return render(request, 'words/word_form.html', {'form': form, 'title': 'Редактировать слово'})


@staff_member_required
def delete_word(request, id):
    try:
        Word.objects.get(id=id).delete()
        return HttpResponseRedirect('/edit/')
    except Word.DoesNotExist:
        return HttpResponseNotFound("<h2>Слово не найдено</h2>")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('word-list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


class WordAPIList(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordAPIDetail(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer