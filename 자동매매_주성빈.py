account_balance = 1000000
daily_loss = 0
MAX_DAILY_LOSS = -100000


def execute_trade(profit_or_loss):
    # 거래 결과를 계좌 잔액에 반영
    # 손실이 발생하면 누적 손실 갱신
    # 거래 가능 여부 반환
    global account_balance
    global daily_loss
    account_balance += profit_or_loss
    if profit_or_loss >= 0:
        print(f'계좌잔액 : {account_balance}원, 오늘손익 : {daily_loss}원')
        return True
    else: #profit_or_loss < 0:
        daily_loss += profit_or_loss
        if daily_loss <= MAX_DAILY_LOSS:
            print(f'계좌잔액 : {account_balance}원, 오늘손익 : {daily_loss}원')
            return False
        else:
            print(f'계좌잔액 : {account_balance}원, 오늘손익 : {daily_loss}원')
            return True
    print(f'계좌잔액 : {account_balance}원, 오늘손익 : {daily_loss}원')
def can_trade():
    # 현재 누적 손실을 기준으로 거래 가능 여부 판단
    global MAX_DAILY_LOSS
    global daily_loss
    if MAX_DAILY_LOSS <= daily_loss:
        return False

print("거래 1:", execute_trade(50000))
print("거래 2:", execute_trade(-30000))
print("거래 3:", execute_trade(-40000))
print("거래 4:", execute_trade(-30000))

print("최종 계좌 잔액:", account_balance)
print("누적 손실:", daily_loss)
print("추가 거래 가능:", can_trade())