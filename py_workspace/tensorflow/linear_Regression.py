import tensorflow as tf

# 키에 따른 발의 크기 예상하기
# 키: 실제값 , 발 사이즈: 예측값

height = 170
shoes = 260                                      #Ctrl + Enter : 커서 아래 행 빈줄 생성
# foot = height * a + b                         #Ctrl + Shift + K : 커서 위치 행 삭제        

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def lossFunction():  #손실함수, 손실값 리턴((실제값-예측값)의 제곱)
    expected = height * a + b
    return tf.square(260 - expected)      #(실제값 - 예측값)의 제곱으로 손실함수를 정함. 이건 내가 임의로 f지정가능

opt = tf.keras.optimizers.Adam(learning_rate=0.1)  #tf.keras.optimizers가 경사하강법을 통해 w를 업데이트 한다는 뜻.
#.Adam은 w값을 때론 작게 때론 크게 알아서 스마트하게 업데이트해주는 공식
#learning_rate은 생략해도. 기본은 0.0001인가..

for i in range(300):
    opt.minimize(lossFunction, var_list=[a,b])  # opt.minimize : 경사하강법 진행 최적의 w값, 여기선 a와 b 찾기.
    # a,b : 경사하강법으로 업데이트할 weight Variable목록
    print(a.numpy(),b.numpy())  # a,b만 써도 되지만 a.numpy()이렇게 하면 값만 출력가능

