"""
- 자료구조: Queue
- 데이터
    - bridge → queue, 다리 위에 올라간 트럭
    - truck_weights → queue, 다리를 지나가지 않은 트럭들의 무게
    - current → 현재 다리에 있는 트럭들의 전체 무게
- while 문 → 트럭들이 전부 지나갈 때까지 반복
    - 1초가 지남 → 다리에 있는 트럭 무게 갱신 (한 대 빠져나감)
    - if 문 → 새로 트럭이 들어와도, 무게 제한을 넘기지 않으면 트럭 삽입
    - 무게 제한을 넘길 거 같으면 트럭이 못 들어왔다는 의미로 0 삽입
- 시간 복잡도:
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    current = 0
    
    while truck_weights:
        answer += 1
        
        current -= bridge.popleft()
        
        if current + truck_weights[0] <= weight:
            current += truck_weights[0]
            truck = truck_weights.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
    
    return answer