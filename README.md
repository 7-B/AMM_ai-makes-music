# AI makes music

## project
  
 **작곡 지식이 없더라도 음악을 만들어보고 싶다!**
* 사용자가 떠올린 간단한 음을 입력하면 음에 맞춰 노래를 생성해주는 AI
* 특정 장르의 음악을 계속해서 생성해주는 AI


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
           
    ![structure](https://user-images.githubusercontent.com/52736420/64146446-00f4d500-ce58-11e9-8b8d-6e14b6356dc7.png)       

- 시스템 구조도 : 음악 데이터를 RNN모델인 LSTM 모델을 통해 학습 시킨 후, 사용자가 음악을 입력하면 LSTM모델을 통하여 비슷한 느낌의 음악을 생성  
![image](https://user-images.githubusercontent.com/52736420/64146533-53ce8c80-ce58-11e9-899b-42cd9f715e0f.png)
  
- **진행상황**
1. 케라스 LSTM 모델로 작곡하기
   Music21 -> 20시간 학습시킨 결과 추상적인 음악. -> 훨씬 깊고 복잡한 네트워크를 만들고 학습시킬 필요성   
     
2. 마젠타 melody-rnn으로 작곡하기
   pre-trained 모델을 가지고 음악을 생성 -> 다른 장르의 음악을 가지고 커스터마이징된 모델 파라미터를 학습시키는 중  
     
3. 마젠타 music-VAE 모델로 작곡하기
   최대 3개의 음을 조합하여 음악을 생성. -> pre-trained 모델을 돌려보기 위해 모델 실행 중

</div>
</details>

---  
<details>
<summary> week2 </summary>
<div markdown="1">
  

- **진행상황**
 <INPUT> : Fruit genie 를 활용한 입력장치  
   
1. 라즈베리 파이 : node app.js 실행 문제 (mpg123 : 오디오 출력 역할 문제)
2. teensy dev 보드 : 스케치를 다운 받아 터치에 따른 반응 변화 확인 
  
 ![image](https://user-images.githubusercontent.com/52736420/64146977-d9067100-ce59-11e9-9e3f-5c0b23ceb1a7.png)



</div>
</details>

---  

<details>
<summary> week3 </summary>
<div markdown='1'>

  
- **진행상황**
 <INPUT> : Fruit genie 를 활용한 입력장치
 
 1. 라즈베리 파이 : 오디오 출력 부분 오류 → 소프트웨어와 직접 연결 방식 선택
 2. teensy dev 보드 : 터치 인식 후 소리 재생 확인
 
- **python 을 활용한 serial data 실시간 받기**  
             
      [window cmd] pip install pyserial  
      
      [python]
      import serial
      import time
      import signal
      import threading
      import winsound #소리 재생
      
 <INPUT> : music vae 를 이용한 학습
 
 1. 재즈로 학습
 2. k-pop으로 학습 check point 300까지 진행





</div>
</details>

---  

<details>
<summary> week4 </summary>
<div markdown='1'>

- **역할 분담**  

      유원호 : audio generation  
      최영철 : imrovement melody-rnn & music VAE  
      이슬기 : servere  
      주선정 : fruit touch, input data  
      정성원 : magenta gpu  




</div>
</details>

--- 

<details>
<summary> week5 </summary>
<div markdown='1'>

- input system 변경  
  
  
![image](https://user-images.githubusercontent.com/52736420/65112119-83b18e80-da19-11e9-91fb-54f618348903.png)






</div>
</details>

---  


### PLAN  
 
 
![schedule](https://user-images.githubusercontent.com/52736420/64063336-42a23780-cc2e-11e9-97fd-9e1de9192605.png) 
 
