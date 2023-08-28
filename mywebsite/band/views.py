# band/views.py
from django.shortcuts import render, redirect
from .models import BandMember, Event, UserProfile
from django.contrib.auth.decorators import login_required
from datetime import date 
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    featured_tracks = [
        {'title': 'Track 1', 'artist': 'Rockin\' Legends', 'url': '/media/audio/track1.mp3'},
        {'title': 'Track 2', 'artist': 'Rockin\' Legends', 'url': '/media/audio/track2.mp3'},
    ]
    
    # Sample data for latest news updates
    latest_news = [
        {'date': '2023-08-15', 'title': 'New Album Release!', 'content': 'Our new album is out now!'},
        {'date': '2023-08-20', 'title': 'Upcoming Concert', 'content': 'Join us for a live concert on August 30th.'},
        
        ]
    
    context = {
        'featured_tracks': featured_tracks,
        'latest_news': latest_news,
    }
    
    return render(request, 'band/homepage.html', context)

from django.shortcuts import render
from .models import BandMember, Event
from datetime import date

# ... Other views ...

def band_members(request):
    # Sample band member data
    members = [
        {'name': 'Jimmy', 'role': 'Lead Guitarist', 'years_active': 10},
        {'name': 'Bass Jams', 'role': 'Lead Bass Guitarist', 'years_active': 8},
        {'name': 'MoKeys', 'role': 'Lead Keyboardist', 'years_active': 12},
        {'name': 'Leigh', 'role': 'Lead Vocalist', 'years_active': 5},

    ]

    return render(request, 'band/band_members.html', {'band_members': members})

def events(request):
    # Sample event data
    upcoming_events = [
        {'title': 'Rockin The Daisies', 'date': date(2023, 8, 25), 'location': 'Pretoria', 'description': 'A rocking concert you don\'t want to miss!', 'tickets_available': 100},
        {'title': 'Rock n Roll Night', 'date': date(2023, 9, 5), 'location': 'Goddess Café', 'description': 'Enjoy a cozy night of acoustic music.', 'tickets_available': 50},
    ]

    return render(request, 'band/events.html', {'upcoming_events': upcoming_events})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('band:user_profile')
    else:
        form = UserCreationForm()
    return render(request, 'band/signup.html', {'form': form})

@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'band/user_profile.html', context)