# 3. 전화번호 이메일 추출
messages = [
    "연락처는 010-1234-5678이고 이메일은 kim@example.com입니다.",
    "이메일은 lee@example.com입니다.",
    "전화번호는 010-2222-3333입니다.",
    "연락처는 010-3333-4444, 010-5555-6666입니다.",
    "이메일은 kim@example.com, lee@example.com입니다.",
    "이메일은 park@example.com이고 전화번호는 01012345678입니다.",
    "안녕하세요. 주문한 상품이 도착하지 않았습니다.",
    "",
    None
]
import re

for i in range(len(messages)):
    try:
        if messages[i] is None:
            raise TypeError('문자열 데이터가 아닙니다.')

        message = messages[i]
        email = re.search(r'.+@.+\.com', message)
        phone = re.search(r'(\d{3}-\d{4}-\d{4})', message)

        result = {'이메일' : email.group() if email else '없음',
                  '전화번호' : phone.group() if phone else '없음'}

        if not email and not phone:
            raise ValueError('연락처 정보를 찾을수 없습니다.')

        print(f'[{i+1}]번 데이터')
        print(result)
        print()

    except(TypeError, ValueError) as e:
        print(f'[{i+1}]번 데이터')
        print(f'처리 실패 : {e}')
        print()
