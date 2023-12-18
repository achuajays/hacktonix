from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect
from .models import UserDetails, Message

def user_details(request, user_id):
    user = UserDetails.objects.get(pk=user_id)
    return render(request, 'app/user_details.html', {'user': user})


def send_message(request, sender_id, receiver_id):
    if request.method == 'POST':
        sender = UserDetails.objects.get(pk=sender_id)
        receiver = UserDetails.objects.get(pk=receiver_id)
        content = request.POST.get('content', '')

        if content:
            Message.objects.create(sender=sender, receiver=receiver, content=content)
            return redirect('user_details', user_id=receiver_id)

    return render(request, 'app/send_message.html', {'sender_id': sender_id, 'receiver_id': receiver_id})


# views.py

from django.shortcuts import render
from .models import UserDetails

def chat(request):
    users = UserDetails.objects.all()
    return render(request, 'app/chat.html', {'users': users})


# views.py
# views.py

from django.shortcuts import render, get_object_or_404
from django.db.models import Q  # Correct import for the Q object
from .models import UserDetails, Message

def view_messages(request, sender_id, receiver_id):
    sender = get_object_or_404(UserDetails, pk=sender_id)
    receiver = get_object_or_404(UserDetails, pk=receiver_id)

    # Fetch all messages between sender and receiver
    messages = Message.objects.filter(
        (Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender))
    ).order_by('timestamp')

    return render(request, 'app/message.html', {'sender': sender, 'receiver': receiver, 'messages': messages, 'receiver_id': receiver_id})

# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def chat(request):
    users = UserDetails.objects.all()
    return render(request, 'app/chat.html', {'users': users})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('chat')  # Redirect to the chat view after successful login
        else:
            # Handle invalid login
            return render(request, 'app/login.html', {'error': 'Invalid login credentials'})
    
    return render(request, 'app/login.html')


# views.py

from django.contrib.auth import logout
from django.shortcuts import render, redirect

def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to the login page after logout
