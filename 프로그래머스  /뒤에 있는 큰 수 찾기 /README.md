처음에는 numbers의 길이만큼 반복을 하여 임의로 numbers를 sort한 리스트 stack을 생성해 numbers[i]보다 더 큰 수가 stack내부에 있으면 해당 수를 answer리스트에 추가하고 없다면 -1을 추가 하려고 구상을 했는데, 입출력 예제 2번 처럼 [9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1] 6의 경우 처럼 앞 뒤로 자신보다 큰 수가 없으면 -1을 반환 해야 하기 때문에 해당 풀이는 접고 더 고민을 하게 되었다.
while stack and numbers[stack[-1]] < numbers[i]: 구문은 stack이 비어있지 않고, stack의 top에 있는 인덱스의 값이 현재 원소 numbers[i]보다 작은 경우에 실행된다. numbers[stack[-1]]은 stack의 top에 있는 인덱스에 해당하는 numbers 배열의 값으로 해당 조건을 만족 한다면, answer에 해당 인덱스 위치에 있는 -1을 pop하여 제거하고 현재 값을 answer의 인덱스 위치에 추가한다.

과정을 반복하여 answer을 채우고 최종 answer를 return하는 방식으로 문제를 풀이하였다.
