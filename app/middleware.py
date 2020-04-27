from django.shortcuts import render, redirect
from django.http import HttpResponse

class AuthRequiredMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return redirect('get_login') # or http response
        return None