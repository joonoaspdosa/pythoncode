import random # 리스트 셔플을 위해 
import time # 시간 측정을 위해
import os # 화면 지우고 대기하기 위해 사용


# 출제 문장 리스트
WORD_LIST = [
    "남박사의 파이썬 100% 실전 프로그래밍 강좌",
    "파이썬에서 ord() 함수는 문자의 유니코드 값을 알아오는 함수로 10진수 값을 리턴 합니다.",
    "chr(x)은 x에 유니코드 10진수 값을 입력하면 해당하는 문자를 리턴합니다.",
    "UTF-8은 유니코드를 8비트 기반으로 저장하는 인코딩 방식입니다.",
    "CP949는 윈도우에서 사용하기 위해 EUC-KR을 확장해서 만든 문자셋 입니다.",
    "파이썬은 코드가 짧고 유연하여 가독성과 생산성이 좋은 프로그래밍 언어 입니다.",
    "독도는 우리땅"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1

    tot_len = len(q)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f} 정확도: {:0.2f} 오타율: {:0.2f}".format(speed, c, e))
    os.system("pause")
