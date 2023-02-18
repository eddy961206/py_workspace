import numpy as np
import tensorflow as tf
import pandas as pd

data = pd.read_csv('gpascore.csv') # pandas로 csv파일 불러서 읽기. 
# print(data)  # pandas로 연 데이터(여기선 data)를 dataframe(열과 행)이라고 함.

# print(data.isnull().sum())   #빈칸 있는 것의 갯수 출력
data = data.dropna()  # NaN/빈칸있는 행을 제거해줌
# data = data.fillna(100) # 비어있는 행에 100을 집어넣어줌
# print(data.isnull().sum())   
# print(data['gpa'].min())   # data['gpa'].min(), .max(), .count()..

yData = data['admit'].values  # .values로 결괏값들을 리스트[] 에 담기. [0 1 1 0 1 0.....] 콤마 없음
# print(yData)
xData = []

for i, rows in data.iterrows():  # data.iterrow() -> data라는 dataframe을 가로 한 줄씩(한개씩 따로) 출력해라   
    xData.append([ rows['gre'], rows['gpa'], rows['rank'] ])
    # print(xData)                                                     

# exit()
#########################   위에는 pandas (파일 전처리과정)    ################

#  1. 딥러닝 모델 만들기(keras.Sequential통해 레이어들 만들기)
model = tf.keras.models.Sequential([   
    tf.keras.layers.Dense(64, activation='tanh'),   # (히든)레이어 하나에 노드 64개 만들기
    tf.keras.layers.Dense(128, activation='tanh'),  # 레이어나 노드의 갯수는 임의. 결과 잘 나올때까지 실험으로 파악해야.
    tf.keras.layers.Dense(1, activation='sigmoid') # 마지막 레이어의 노드 : 확률을 한 개만 예측 할거면 노드가 하나여야.
    # 마지막 레이어의 활성함수는 sigmoid로. 그래야 확률을 0과 1 사이로 압축시켜서 알려줌. 물론 다른 많은 활성함수들도 있음.
    # 첫번째와 두번째 히든 레이어로 들어간 활성함수인 tanh는 값을 -1 ~ 1 로 압축시켜줌. 
])

#  2. 모델 컴파일
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])  
    # optimizer='adam' 이게 범용적으로 자주 쓰여. optimizer가 learning rate관련된 것. w를 균등하지 않게 업데이트 할 수있게 해줌.
    # 로스함수는 지금같은 경우 확률 0~1사이의 분류 문제면 binary_corssentropy쓰는게 좋아.
    # 로스함수는 어떤 문제를 풀려고 하느냐에 따라 적절한 함수들이 다름.

#  3. 모델 학습(fit) 시키기
model.fit(np.array(xData), np.array(yData), epochs=1000)   
# model.fit(학습데이터, 실제정답, epochs=10)  10번 학습시키기. 즉 최적의 w값 찾는 코드.
# 데이터와 실제정답은 [] 형식으로 넣어줘야함.
# 데이터들을 리스트 그대로 넣으면 안됨. numpy array로 변환해서 넣어야.


# 4. 예측
predict_val = model.predict( [ [750, 3.70, 3], [400, 2.2, 1] ] )    
# model.predict(예측원하는 값) 여기선 두명의 성적 입력함.
print(predict_val)


