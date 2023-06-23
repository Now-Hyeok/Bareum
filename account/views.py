from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
import requests
import json
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from . import models
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def myupdate(request):
     if request.method == 'POST':
        data = json.loads(request.body)

        nickname = data.get('nickname')
        birthday = data.get('birthday')
        height = data.get('height')
        weight = data.get('weight')
        gender = data.get('gender')
        id = data.get('userdata')
        #유저 아이디 확인해서 동일한 아이디에 

       
    
# Create your views here.

@csrf_exempt
def login_user(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        login_id = data.get('userLoginid')
        password = data.get('password')
        print(login_id, password)
        
        #사용자 인증
        user = authenticate(login_id=login_id, password=password)
        print(user)
        if user is not None:
            login(req, user)
            csrf_token = get_token(req)
            response = JsonResponse({'success': '로그인이 완료되었습니다.',
                                     'login_id': login_id, 
                                     'username': user.user_name,
                                     'member_id': user.member_id
                                     })
            response["Token"] = csrf_token
            return response
        else:
            return JsonResponse({'error': '로그인에 실패했습니다.'}, status=400)
        
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    
def logout_user(req):
    logout(req)
    return JsonResponse({'success': '로그아웃이 완료되었습니다.'})

@csrf_exempt
def signup(req):

    if req.method == 'POST':

        data = json.loads(req.body.decode('utf-8'))

        login_id = data.get('userLoginid')

        password = data.get('password')

        user_name = data.get('userName')

        print(login_id, password, user_name)

       

        if models.User.objects.filter(login_id = login_id).exists():

            return JsonResponse({'result':'fail'})

       

        user = models.User.objects.create_user(login_id = login_id,

                                               password = password,

                                               user_name = user_name)

       

        return JsonResponse({'login id':login_id, 'user_nickname':user_name,

                             'result': 'success',

                             'message': '회원가입이 완료되었습니다.'})

    else:

        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    

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
        user_id = str(user_data['id'])
        email = user_data['kakao_account']['email']
        name = user_data['properties']['nickname']
        if models.User.objects.filter(login_id = email).exists():
            user = authenticate(login_id=email, password=user_id)
            login(request, user)
        else:
            user = models.User.objects.create_user(login_id = email,
                                       password = user_id,
                                       user_name = name,
                                       email=email)
            user = authenticate(login_id=email, password=user_id)
            login(request, user)
            
        response = JsonResponse({'success': '로그인이 완료되었습니다.',
                     'login id': email, 
                     'username': user.user_name,
                     'member_id': user.member_id
                     })
            
        return response

@login_required
def check_session(req):
    #로그인 안되있으면 302 리턴
    return JsonResponse({"logged_in": True})

