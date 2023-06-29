from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from PyKakao import Karlo
from PIL import Image
import uuid


@csrf_exempt
def user_list(request):
    if request.method == 'POST': # POST 방식일 때
        data = JSONParser().parse(request) # 요청들어온 데이터를 JSON 타입으로 파싱
        
        KAKAO_API_KEY = 'c3aa6fa36b6927a09b25673f6847c64b'
        karlo = Karlo(service_key = KAKAO_API_KEY)

        # Token 값 들고오기
        tokens = data["tokens"]
        
        # 이미지 생성하기 REST API 호출
        # Karlo에게 이미지 생성 요청
        img_dict = karlo.text_to_image(tokens, 4)
        
        tempList = img_dict.get("images")
        nameList = list();

        for temp in tempList :
            # 생성된 이미지 정보
            img_str = temp.get("image")
            
            uuid_name = uuid.uuid1()
            nameList.append({"name": '{}.png'.format(uuid_name)})
            
            name_temp = 'C://Users//HyungJoon//Documents//0_OSSP//resources//images//{}.png'.format(uuid_name)

            # base64 string을 이미지로 변환
            img_temp = karlo.string_to_image(base64_string = img_str, mode = 'RGBA')
            img_temp.save(name_temp)

        return JsonResponse(nameList, safe=False)
    

#Karlo에게 이미지 생성 요청
# 이미지 생성하기 REST API 호출
# img_dict = karlo.text_to_image(prompt, 4)

# 생성된 이미지 정보
