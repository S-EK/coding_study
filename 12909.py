"""
- 자료구조: Queue
- while 문 → 입력된 문자열을 전부 확인할 때까지
    - 첫 번째 if 문 → 여는 괄호가 없는데 닫는 괄호가 나오면, 올바르지 않음으로 판단
    - 두 번째 if 문 → 여는 괄호인지, 닫는 괄호인지에 따라 해당하는 변수 개수 갱신
    - 세 번째 if 문 → 여는 괄호 개수보다 닫는 괄호 개수가 더 많으면, 올바르지 않음으로 판단
- if 문 → 여는 괄호 개수와 닫는 괄호 개수가 다르면, 올바르지 않음으로 판단
- 시간 복잡도: O(N)
"""

from collections import deque

def solution(s):
    opening = 0
    closing = 0
    s = deque(s)
    
    while len(s) != 0:
        x = s.popleft()
        
        if opening == 0 and x == ')':
                return False
        
        if x == '(':
            opening += 1
        else:
            closing += 1
            
        if opening < closing:
            return False

    if opening != closing:
        return False
    
    return True