"""
- 자료구조: Queue
- 데이터
    - prices → queue, 주식 가격
    - count → 하락하지 않는 날짜의 수 카운트
- while 문 → 주식 가격을 처음부터 끝까지 하나씩 확인
    - 매 주식 가격마다 날짜의 수 0으로 초기화
    - for 문 → prices에 남은 주식을 순차적으로 돌면서 가격이 하락하는 순간, count 값 갱신을 멈추고 반복문 탈출
- 시간 복잡도:
"""

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        
        count = 0
        for i in prices:
            if price > i:
                count += 1
                break
            count += 1
        
        answer.append(count)
    
    return answer