from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from .models import Record


class Auth(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/admin"):
            return None
        if request.method == "POST":
            token = request.COOKIES.get("token")
            if token != "123456":
                return JsonResponse({"code": 5000, "message": "没有权限喵~"})
        return None
