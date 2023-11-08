from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Message
import json

def index(request):
    return HttpResponse('Hi! This is index page.')

@csrf_exempt
@require_POST
def log_message(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        message_content = data.get('message')
        if message_content:
            message = Message(content=message_content)
            message.save()
            return JsonResponse({'message': 'Message logged successfully'})
        else:
            return JsonResponse({'error': 'Invalid message data'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)