from PIL import Image
from django.http import JsonResponse
from .modules.modules_ocr import ocr
import numpy as np
import pandas as pd
from collections import defaultdict
import difflib
import os 
from product.models import Nutraceuticals, new_Nutraceuticals
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_image(request):
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]
        img = np.array(Image.open(image))
        model = ocr()
        result_ocr = model(img)
        # print(result_ocr)
        pr_list=[]
        related_pr = []
        for i in result_ocr:
            if i[2] > 0.4:
                pr_list.append(i[1])
        print(pr_list)
        result = []
        for string in pr_list:
            cur_dir = os.path.dirname(os.path.abspath(__file__))
            csv_dir = os.path.join(cur_dir, 'total_nutrition.csv')
            names = pd.read_csv(csv_dir)["name"].values

            input_string = string # 인풋으로 넣을 단어혹은 문장
            input_bytes = bytes(input_string, 'utf-8') # byte로 변환
            input_bytes_list = list(input_bytes) 
            res = defaultdict(float) # DB 안에있는 이름과 비교할때 편하게 하려고 dict로 구성
            for i in names:
                answer_bytes = bytes(i, 'utf-8') # dB 안에있는 이름을 byte화
                answer_bytes_list = list(answer_bytes)
                sm = difflib.SequenceMatcher(None, answer_bytes_list, input_bytes_list) # difflib의 sequencematcher로 byte끼리 유사도 비교
                similar = sm.ratio()

                res[i] = similar # res에 저장
                
            sorted_dict = sorted(res.items(), key=lambda x: x[1]) # 유사도에 따른 정렬
            sorted_dict = sorted_dict[::-1]
            print(sorted_dict[:3])
            for i in sorted_dict:
                if i[1] >= 0.5 and i[0] not in related_pr:
                    related_pr.append((i[0],i[1]))
                        
            # print(related_pr[:5])
        related_pr = sorted(related_pr, key=lambda x: x[1], reverse=True)
        print('유사도순 정렬 확인')
        # print(related_pr)
        last = []
        for i in related_pr:
            last.append(i[0])
        print(last)
        for i in last[:20]:
            pr_info = Nutraceuticals.objects.filter(nutraceuticals_name=i).values('nutraceuticals_name','업소명', '업체별_제품코드')
            result.append(list(pr_info))
 
        flattened_result = [item for sublist in result for item in sublist]
            
        # print(flattened_result)
        if len(flattened_result) == 0:
            return JsonResponse({'results':'fail'})
        
        return JsonResponse({'results': 'success', 'products':flattened_result})
    
    return JsonResponse({"error": "Invalid request"})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        product_name = request.POST['productName']
        brand_name = request.POST['brandName']
        pr_image = request.FILES['image']
        
        new = new_Nutraceuticals.objects.last().input_number
        pr_image.name = "captured_image{}.jpg".format(new + 1).replace(' ','')
        print(product_name, brand_name, pr_image)

        try:
            new_nutraceutical = new_Nutraceuticals(
                nutraceuticals_name=product_name,
                company_name=brand_name,
                image=pr_image
            )
            new_nutraceutical.save()

            return JsonResponse({"success": True})
        except Exception as e:
            print(e)
            return JsonResponse({"success": False})
    else:
        return JsonResponse({"success": False})
