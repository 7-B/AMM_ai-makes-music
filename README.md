# AI makes music

## project
 음악을 작곡 지식이 없더라도 만들어보고 싶다!

![flow](https://user-images.githubusercontent.com/52736420/64063155-97907e80-cc2b-11e9-9951-991d517f31b4.png)

## Weekly records

<details>
<summary> week1 </summary>
<div markdown='1'>
  
 - INPUT : Fruit genie 를 활용한 입력장치  
           magenta_fruit genie
           
           구성요소
           1. 라즈베리 파이 : 터치를 받아 피오노 지니 소프트웨어로 전송하고 메모를 재생하는 노드앱 실행
           2. teensy dev 보드 : 터치 감지 및 소프트웨어 전송을 처리  
           

- 시스템 구조도 : 음악 데이터를 RNN모델인 LSTM 모델을 통해 학습 시킨 후, 사용자가 음악을 입력하면 LSTM모델을 통하여 비슷한 느낌의 음악을 생성

- **진행상황**
1. 케라스 LSTM 모델로 작곡하기
   Music21 -> 20시간 학습시킨 결과 추상적인 음악. -> 훨씬 깊고 복잡한 네트워크를 만들고 학습시킬 필요성 !  
2. 마젠타 melody-rnn으로 작곡하기
   pre-trained 모델을 가지고 음악을 생성 -> 다른 장르의 음악을 가지고 커스터마이징된 모델 파라미터를 학습시키는 중  
3. 마젠타 music-VAE 모델로 작곡하기
   최대 3개의 음을 조합하여 음악을 생성. -> pre-trained 모델을 돌려보기 위해 모델 실행 중


<details>
<summary> week2 </summary>
<div markdown='2'>
 
 
 <details>
<summary> schedule planning </summary>
<div markdown='6'>
 
 
