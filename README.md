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

