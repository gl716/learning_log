from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'app1/index.html')


def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'app1/topics.html', context)


def topic(request, topic_id):
    """show topic and entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'app1/topic.html', context)


def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # Post data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:topics')
    # display a blank or invalid form.
    context = {'form': form}
    return render(request, 'app1/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # no data submitted; create a blank form.
        form = EntryForm()
    else:
        # Post data submitted; process data
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('app1:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'app1/new_entry.html', context)
