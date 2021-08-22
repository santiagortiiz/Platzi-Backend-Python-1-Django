# Standard libraries
import pdb # Python debugger

# Django Core
from django.http import HttpResponse, response, JsonResponse

# Utilities
import json
from datetime import datetime

def hello_world(request):
    # pdb.set_trace()
    now = datetime.now().strftime('%b %d %y')
    message = f'Hello, the time is: {now}'
    data = {
        'status': 'ok',
        'message': message
    }
    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
    )

def access(request, name, age):
    
    if (age < 18): data = f'sorry {name} you are not allow to access'
    else: data = f'Go forward {name}'

    # return HttpResponse(
    #     json.dumps({
    #         'message': data
    #     }), 
    #     content_type='application/json'
    # )

    return JsonResponse(
        data = {
            'message': data
        }, 
        safe=True
    )
