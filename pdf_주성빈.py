
customers = [
{"name": "김철수", "phone": "010-1234-5678", "agree": True},
{"name": "이영희", "phone": "010-2345-6789", "agree": False},
{"name": "박민수", "phone": "010-3456-7890", "agree": True},
{"name": "최지훈", "phone": "010-4567-8901", "agree": False},
{"name": "정수진", "phone": "010-5678-9012", "agree": True},
]
sent_count = 0
for coupon in customers:
#    sent_count = 0
    if coupon['agree'] == False:
        print(f'[스킵]{coupon['name']}고객님은 수신 거부 상태입니다.')
        continue
    else:
        print(f'[발송]{coupon['name']}님께 20% 할인 쿠폰이 전송되었습니다.')
        sent_count += 1
print(f'\n 작업 완료 : 총 {sent_count}명에게 발송되었습니다.')

#----------------------------------------------------

docs = [
{
"title": " 파이썬기초문법가이드",
"content": "변수, 반복문, 리스트와 딕셔너리를 활용해 기초를 다집니다.",
"category": "프로그래밍"
},
{
"title": " 생성형AI 서비스동향",
"content": " 대형언어모델(LLM) 을 활용한 다양한 업무 자동화 사례가 늘고 있습니다.",
"category": "인공지능"
}
]

# 1. 보기좋게 출력 (한글로, 줄변경)
def print_documents(documents):
    for document in docs:
        print(f'제목 : {document['title']}\n카테고리 : {document['category']}\n내용 : {document['content']}')
        print('\n-----------------------------------------\n')
print()

print_documents(docs)

# 2번. 키워드가 포함된 문서를 찾기
def search_documents(documents, keyword):
    for document in docs:
        if keyword in document['title'] or keyword in document['content']:
            print(f'{keyword}이(가) 포함된 문서 : {document['title']}')

search_documents(docs, '니다.')

# 3번 전체 문서 개수를 세기
def count_documents(documents):
    count = 0
    for i in docs:
        for j in i:
            count += 1
    print(count)
count_documents(docs)

# 4번. 특정 카테고리에 속한 문서만 고르기
def filter_by_category(documents, category):
    for docu in docs:
        if docu['category'] == category:
            print(f'{docu['category']}이(가) 포함된 문서 : {docu['title']}')
    return
filter_by_category(docs, '인공지능')
