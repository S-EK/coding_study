"""
- 자료구조: Queue
- while문 → progresses에 있는 모든 기능이 배포될 때까지 반복
    - for문 → 배포되지 않은 기능들의 개발 진도 갱신
    - while문 → 배포되지 않은 기능이 존재 &  우선 순위가 최우선인 기능의 개발이 종료
        - 조건에 해당하는 기능을 전부 순차적으로 배포 (count +1)
    - if문 → 진도를 갱신했을 때, 배포된 기능이 존재하면 해당 기능의 개수 삽입
- 시간 복잡도: ..?
"""

from collections import deque

def solution(progresses, speeds):
    count = 0
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count != 0:
            answer.append(count)
            count = 0
    
    return answer