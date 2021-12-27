from django.http import JsonResponse
from django_q.tasks import async_task

def index(request):
    json_payload = {
        "message": "Hello world!"
    }
    #you have to call async_task function from app level or lib level
    async_task("django_q_app.services.sleep_and_print", 10)
    async_task("math.copysign", 5, -7, hook="django_q_app.services.print_result")
    return JsonResponse(json_payload)
