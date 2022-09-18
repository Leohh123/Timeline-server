import re
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from .models import Record

WHITE_LIST = [re.compile(p) for p in [
    r"/admin",
    r"/comment/add"
]]


class Auth(MiddlewareMixin):
    def process_request(self, request):
        for r in WHITE_LIST:
            if r.match(request.path):
                return None
        if request.method == "POST":
            token = request.COOKIES.get("token")
            if token != "123456":
                return JsonResponse({"code": 5000, "message": "没有权限喵~"})
        return None
