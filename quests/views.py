from django.shortcuts import render

from .models import Quest, ModelVisual

# Create your views here.
def quests(request):
    quests = Quest.objects.all()
    return render(request, 'quests.html', { 'quests': quests })

def quest_detail(request, slug):
    quest = Quest.objects.get(slug=slug)
    return render(request, 'quest.html', { 'quest': quest })

def model_detail(request, slug, model_slug):
    model = ModelVisual.objects.get(slug=model_slug)
    return render(request, 'model.html', { 'model': model })

