from django.http import JsonResponse


def machine(request):
    if request.method == 'GET':
        return JsonResponse({'ok': 'ok'})
    pass