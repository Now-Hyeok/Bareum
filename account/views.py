from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
import requests
import json
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import models
# Create your views here.

@csrf_exempt
def login_user(req):
    if req.method == 'POST':
        login_id = req.POST.get('userLoginid')
        password = req.POST.get('password')
        
        #사용자 인증
        user = authenticate(req, username=login_id, password=password)

        if user is not None:
            login(req, user)
            return JsonResponse({'success': '로그인이 완료되었습니다.',
                                 'login id':login_id, 
                                 'username':user.user_name})
        else:
            return JsonResponse({'error': '로그인에 실패했습니다.'}, status=400)
        
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    
@csrf_exempt
def logout_user(req):
    logout(req)
    return JsonResponse({'success': '로그아웃이 완료되었습니다.'})

@csrf_exempt
def signup(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        login_id = data.get('userLoginid')
        password = data.get('password')
        user_name = data.get('userName')
        print(login_id, password, user_name)
        user = models.User(
            user_login_id = login_id,
            user_login_password = password,
            user_name = user_name,
        )
        user.save()
        return JsonResponse({'login id':login_id, 'username':user_name, 
                             'result': 'success', 
                             'message': '회원가입이 완료되었습니다.'})
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    
    

@method_decorator(csrf_exempt, name='dispatch')
class KakaoLogin(View):

    def dispatch(self, request, *args, **kwargs):
        return super(KakaoLogin, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
        except:
            ...
        access_token = data['access_token']
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        response = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
        user_data = response.json()
        print(user_data)
        # 이미 가입한 회원인지 확인후
        # 기존사용자가 아니면 새 사용자로 생성하고
        # 로그인로직실행 하면될듯
        return JsonResponse({"message": "success"})
    