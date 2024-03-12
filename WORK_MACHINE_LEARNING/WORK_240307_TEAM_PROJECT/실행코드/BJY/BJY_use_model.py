## -------------------------------------------------
## 모델을 활용한 서비스 제공
## -------------------------------------------------
# 모듈 로딩
from joblib import *
import pandas as pd

# 전역 변수
model_file = 'sd_and_qs_rf.pkl'

# 모델 로딩
model = load(model_file)

# 로딩된 모델 확인
print(model.estimators_)
print(list(model.feature_names_in_), end='\n\n')

# 수면시간 예측 정보 입력 => 4개 피쳐
while True:
    input_data = input('데이터 입력 (형식: (만)나이, 스트레스 레벨(1~10), 수면 심박수(bpm), 일일 신체활동 시간(분) ) : ')
    if len(input_data):
        if len(input_data.split(',')) == 4:
            data_list = list(map(float, input_data.split(',')))
            break
        else:
            print('입력한 형식이 잘못되었거나 데이터의 개수가 부족합니다.')
    else:
        print('입력된 정보가 없습니다.')

# pd.DataFrame([data_list], columns=list(model.feature_names_in_))

# print('사용한 모델 유형:', type(model))

# 입력된 정보에 해당하는 품종 알려주기
pred_sd_qs = model.predict(pd.DataFrame([data_list], columns=list(model.feature_names_in_)))
pred_sd, pred_qs = pred_sd_qs[0]

decimal_part = pred_sd % 1  # 소수점 부분 저장

# print(f'소수점 부분 : {decimal_part}')
print(f'[예측치] 수면시간 : {int(pred_sd)}시간 {int(60 * decimal_part)}분, 수면의 질 : {pred_qs}')
