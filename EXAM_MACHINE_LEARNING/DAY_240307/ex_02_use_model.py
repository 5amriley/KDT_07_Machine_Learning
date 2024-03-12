## -------------------------------------------------
## 모델을 활용한 서비스 제공
## -------------------------------------------------
# 모듈 로딩
from joblib import *
import pandas as pd

# 전역 변수
model_file = '../model/iris_best_model.pkl'

# 모델 로딩
model = load(model_file)

# 로딩된 모델 확인
print(model.classes_)
print(list(model.feature_names_in_))

# 붓꽃 정보 입력 => 4개 피쳐
while True:
    input_data = input('붓꽃 정보 입력 (예: 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비) : ')
    if len(input_data):
        if len(input_data.split(',')) == 4:
            data_list = list(map(float, input_data.split(',')))
            break
        else:
            print('입력한 형식이 잘못되었거나 데이터의 개수가 부족합니다.')
    else:
        print('입력된 정보가 없습니다.')

# pd.DataFrame([data_list], columns=list(model.feature_names_in_))

print('사용한 모델 유형:', type(model))

# 입력된 정보에 해당하는 품종 알려주기
pred_iris = model.predict(pd.DataFrame([data_list], columns=list(model.feature_names_in_)))
print(f'해당 꽃은 {pred_iris}입니다.')
