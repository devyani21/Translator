
from django.shortcuts import render
from translate import Translator


# Create your views here.


def home(request):
    return render(request,'home.html')


def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print(text, lang)

    # translate the text
    translator = Translator(to_lang=lang)
    translated = translator.translate(text)

    tr = translated
    return render(request, 'translated.html',{'translated':tr})
