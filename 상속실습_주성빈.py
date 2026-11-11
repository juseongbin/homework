# 온라인 쇼핑몰에서 주문한 상품의 배송 유형에 따라 배송 정보를 관리하는 프로그램을 작성하세요.
# 일반 배송과 빠른 배송은 공통적인 배송 정보를 가지고 있지만, 배송비와 배송 처리 방식이 다릅니다.

class Delivery:
    now = '상품 준비중'

    def __init__(self, customer_name : str, address : str):
        self.customer_name = customer_name
        self.address = address

    def show_info(self):
        print(self.customer_name)
        print(self.address)

    def track_delivery(self):
        print(self.customer_name)
        print(self.now)

class StandardDelivery(Delivery):
    arrivalday = '주문일로부터 2~3일 이내'
    delivery_fee = '3,000원'
    delivery_type = '일반 배송'
    def __init__(self, customer_name, address):
        super().__init__(customer_name, address)

        print('='*25)
        print('[일반배송정보]')
        print(f'''고객명 : {self.customer_name}
배송지 : {self.address}
배송 유형 : {self.delivery_type}
배송비 : {self.delivery_fee}
예상 도착 : {self.arrivalday}
[일반 배송 조회]
[배송 조회] : {self.customer_name} 고객님
현재 배송 상태 : 배송 출발
[택배 접수]\n택배사에 배송 접수를 완료했습니다.''')
        print('='*25)

class QuickDelivery(Delivery):
    delivery_fee = '6,000원'
    delivery_type = '빠른 배송'
    arrivalday = '주문 당일'
    def __init__(self, customer_name, address, rider_name : str, rider_number : str):
        super().__init__(customer_name, address)
        self.rider_name = rider_name
        self.rider_number = rider_number

        print('='*25)
        print(f'''[빠른 배송 정보]
고객명 : {self.customer_name}
배송지 : {self.address}
배송 유형 : {self.delivery_type}
배송비 : {self.delivery_fee}
예상 도착 : {self.arrivalday}
[빠른 배송 조회]
[배송조회] {self.customer_name}
현재 배송 상태 : 배송 중
[라이더 전화 연결]
담당 라이더 : {rider_name}
라이더 전화번호 : {rider_number}
담당 라이더에게 전화 연결을 요청합니다.''')
        print('='*25)

standard = StandardDelivery('김민수', '서울시 강남구')
quick = QuickDelivery('이서연', '서울시 송파구', '박철수', '010-1234-5678')