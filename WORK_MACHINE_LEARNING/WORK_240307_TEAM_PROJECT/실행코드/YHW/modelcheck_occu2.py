from joblib import load
import pandas as pd


model_file = './occupation2.pkl'

occupation_model = load(model_file)

super_data= input('나이, 심박수, 수면시간, 스트레스 정도(1~10)사이, 1일 걸음 수, '
                  '특이사항(정상:0, 수면무호흡증:1, 불면증:2) 을 입력하세요 : ').split(',')
disorder_list = ['normal', 'Sleep Apnea', 'Insomnia']
try:
    if len(super_data) == 6:
        super_data = list(map(int, super_data))
        data = pd.DataFrame(data=[super_data], columns=['Age','Heart Rate','Sleep Duration','Stress Level','Daily Steps','Sleep Disorder'])
        # make_predict([super_data])
        print(f'나이: {super_data[0]},\t 심박수:{super_data[1]},\t 수면시간:{super_data[2]},\n스트레스 정도(1~10):{super_data[3]},\t 1일 걸음 수:{super_data[4]}, 특이사항:{disorder_list[super_data[5]]}')

        def make_predict(feature_data):
            occupation = occupation_model.predict(feature_data)
            # print(occupation)
            occupationList = ['Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant', 'Lawyer', 'Salesperson']
            predictproba = occupation_model.predict_proba(feature_data)
            occu_dict=dict(zip(occupationList, predictproba[0]))

            print(f' 직업이 {occupationList[occupation[0]]}일 확률: {predictproba[0][occupation[0]]*100}%')
            print('-'*30)
            for key, value in occu_dict.items():
                print(f'{key} 확률 : {round(value*100,2)}%')

        make_predict(data)
    else:
        print('잘못된 데이터입니다.')
except Exception as e:
    print('잘못된 데이터입니다.')
    print(e)