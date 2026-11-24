#더치페이 계산을 도와주는 split_bill(total_amount_str, people_count_str) 함수를 만들어보세요.
#1. 입력값을 숫자로 변환 (문자가 섞여 있으면 ValueError 발생)
#2. 1인당 금액 계산 (인원에 0을 넣으면 ZeroDivisionError 발생)

def split_bill(total_amount_str, people_count_str):
    try:
        amount = int(total_amount_str)
        people = int(people_count_str)
        result = int(amount/people)
        print(f'정산 결과 : 1인당 {result}원 입니다.')
        return(result)
    except ValueError:
        print('[입력 오류] 금액과 인원수에는 숫자만 입력해야 합니다.')
    except ZeroDivisionError:
        print('[계산 오류] 정산 인원은 0명일 수 없습니다.')
    except TypeError:
        print('[입력 오류] 숫자만 입력해 주세요')

# 1. 정상 실행
print("테스트 1: 정상 입력")
split_bill("150000", "4")

# 2. 0명 입력 (ZeroDivisionError 발생)
print("테스트 2: 0명 입력")
split_bill("150000", "0")

# 3. 텍스트/공백 입력 (ValueError 발생)
print("테스트 3: 텍스트 입력")
split_bill("15만원", "4")

#------------------------------------
# 로또 번호 생성기
#import random 을 이용해서 1~45까지의 숫자를 7개 뽑아주세요.
#리스트에 담아 출력하시면 됩니다.
#주의! 로또 번호 특성상 중복된 숫자는 뽑을 수 없습니다.

import random

ball = 1
lotto = []
while ball < 46:
    lotto.append(ball)
    ball += 1
print(lotto)

winning_ball = []
#----------------------
random.shuffle(lotto)
print('shuffle', lotto[:7])
#---------------------

i = 0
winning_ball = []
while i < 7:
    winning_ball.append(random.randint(1, 45))
    i += 1
print('randint', winning_ball)
#---------------------
print('choices', random.choices(lotto, k=7))