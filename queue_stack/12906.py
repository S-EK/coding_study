"""
    - 연속되는 숫자 제거
    - 자료구조: Stack
    - for문 → arr를 하나씩 돌면서 확인
      - answer의 마지막 원소와 같은지에 따라서 append할지 아닐지 판단
    - 시간 복잡도: O(N)
 """

def solution(arr):
    answer = []
    
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if answer[-1] != i:
                answer.append(i)
    
    return answer