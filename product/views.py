from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from .models import Nutraceuticals
from .serializers import NutraSerializer
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from .models import Review, BareumReview,BareumReviewImage
from .serializers import ReviewSerializer, BareumReviewSerializer, TotalRankingSerializer
from django.core.files.storage import default_storage

from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

from django.db.models import F, Q


@csrf_exempt
def search_nutraceuticals(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_query = data['searchQuery']
        filtered_nutraceuticals = Nutraceuticals.objects.filter(nutraceuticals_name__contains=search_query).annotate(
                lowest_value=F('review__lowest'),
                star=F('review__average_rating')
            )
        response_data = []
        for nutraceutical in filtered_nutraceuticals:
            response_data.append({
                'id': nutraceutical.업체별_제품코드,
                'name': nutraceutical.nutraceuticals_name,
                'score': nutraceutical.score,
                'company_name': nutraceutical.업소명,
                'lowest_value': nutraceutical.lowest_value,
                'star': nutraceutical.star,
            })
        sorted_response_data = sorted(response_data, key=lambda x: x["score"], reverse=True)
        print(sorted_response_data)
        return JsonResponse({'search_res': sorted_response_data}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})



class ProductDetailView(APIView):
    serializer = NutraSerializer 
    def get(self,request,product_code):
        try:
            product = Nutraceuticals.objects.get(pk=product_code)
        except Nutraceuticals.DoesNotExist:
            
            return JsonResponse({"message": "Product not found"}, status=404)
        serializer = self.serializer(product)
        return Response(data= serializer.data, status=status.HTTP_200_OK)        
        
class ReviewList(APIView):
    def get(self, request,product_code):
        try:
            reviews = Review.objects.filter(제품코드_id=product_code)
        except Review.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BareumReviewList(APIView):
    def get(self,request,product_code):
        try:
            reviews = BareumReview.objects.filter(제품코드_id=product_code)
        except BareumReview.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)
        serializer = BareumReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self,request,product_code):
        reviews = request.POST['reviews']
        rating = request.POST['rating']

        try:
            nutra = Nutraceuticals.objects.get(업체별_제품코드=product_code)
            review = BareumReview.objects.create(
                제품코드_id = nutra.업체별_제품코드,
                nutraceuticals_name = nutra.nutraceuticals_name,
                company_name = nutra.업소명,
                reviews = reviews,
                rating = rating,
                writer = request.user,            
            )

            if len(request.FILES) > 0:
                for key in request.FILES:
                    image_file = request.FILES[key]
                    image = BareumReviewImage()
                    image.review_img_url = default_storage.save(
                        "review_images/%s" % (image_file.name,),
                        image_file
                    )
                    image.review = review
                    image.save()
                    
        except Nutraceuticals.DoesNotExist:
            return Response({"error": "제품이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_201_CREATED)
    

        
class MyReviewList(APIView):
    def get(self,request,member_id):
        try:
            reviews = BareumReview.objects.filter(writer=member_id)
        except BareumReview.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)
        serializer = BareumReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
from rest_framework.pagination import PageNumberPagination
    
class RankingPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    max_page_size = 100
    
class TotalRankingList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            top_nutra = Nutraceuticals.objects.order_by('-score')
            paginator = RankingPagination()
            paginated_ranking = paginator.paginate_queryset(top_nutra,request)
            serializer = TotalRankingSerializer(paginated_ranking, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        
        
class AgeRankingList(APIView):
    def get(self, request):
        try:
            ingredients = request.GET.get('ingredients', '')
            ingredients_list = ingredients.split(',')
            queryset = Nutraceuticals.objects.none() 
            
            for ingredient in ingredients_list:
                column_condition = Q(**{ingredient + '__gt': 0})
                queryset |= Nutraceuticals.objects.filter(column_condition)  
                
            top_nutra = queryset.order_by('-score')
            paginator = RankingPagination()
            paginated_ranking = paginator.paginate_queryset(top_nutra, request)
            serializer = TotalRankingSerializer(paginated_ranking, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class BrandRankingList(APIView):
    def get(self, request):
        try:
            all_brands = Nutraceuticals.objects.values_list('업소명', flat=True).distinct()
            brand_rankings = []

            for brand in all_brands:
                top_nutra = Nutraceuticals.objects.filter(업소명=brand).order_by('-score')[:3]
                serializer = TotalRankingSerializer(top_nutra, many=True)
                total_score = sum(item['score'] for item in serializer.data)
                brand_ranking = {
                    "brand": brand,
                    "ranking": serializer.data,
                    "total_score": total_score,
                }
                brand_rankings.append(brand_ranking)

            brand_rankings.sort(key=lambda x: x['total_score'], reverse=True)

            paginator = RankingPagination()
            paginated_rankings = paginator.paginate_queryset(brand_rankings, request)

            return paginator.get_paginated_response(paginated_rankings)

        except Exception as e:
            print(str(e))
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CateogryRankingList(APIView):
    def get(self, request):
        try:
            ingredients = request.GET.get('ingredients', '')
            ingredients_list = ingredients.split(',')
            queryset = Nutraceuticals.objects.none() 
            
            for ingredient in ingredients_list:
                column_condition = Q(**{ingredient + '__gt': 0})
                queryset |= Nutraceuticals.objects.filter(column_condition)  
                
            top_nutra = queryset.order_by('-score')
            paginator = RankingPagination()
            paginated_ranking = paginator.paginate_queryset(top_nutra, request)
            serializer = TotalRankingSerializer(paginated_ranking, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
class IngredientRankingList(APIView):
    def get(self, request, ingredient):
        try:
            top_nutra = Nutraceuticals.objects.filter(**{ingredient + '__gt': 0.0}).order_by('-score')
            paginator = RankingPagination()
            paginated_ranking = paginator.paginate_queryset(top_nutra,request)
            serializer = TotalRankingSerializer(paginated_ranking, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)