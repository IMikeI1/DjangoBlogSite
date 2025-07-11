from django import forms
from django.contrib.auth.models import User
from .models import Post


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label='Заголовок')
#     text = forms.CharField(widget=forms.Textarea, label='Текст поста')
#     author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')
#     image = forms.ImageField(required=False, label='Изображение')


class PostForm(forms.ModelForm):
    # Дополняем конструктор родительского класса
    def __init__(self, *args, **kwargs):
        # Получаем author из именнованных элементов (его передали во views)
        author =  kwargs.pop('author')
        # Вызываем конструктор родительского
        super().__init__(*args, **kwargs)
        # Устанавливаем начальное знаечение поля author
        self.fields['author'].initial = author
        # Отключаем видимость это поля в форме
        self.fields['author'].disable = True
        self.fields['author'].widget = forms.HiddenInput()
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'author') # поля, которые используется
        # exclude = ('author', 'created_ad') # поля, которые не используются (выбрать что-то одно)

        labels = {
            'title': 'Заголовок',
            'text': 'Текст поста',
            'image': 'Изображение'
        }

class FilterForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор', required=False)
    created_at = forms.DateField(label='Дата публикации', widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'], required=False)