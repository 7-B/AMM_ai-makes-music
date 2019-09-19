# AI makes music

<br>

## project
  
 **▶ 작곡 지식이 없더라도 음악을 만들어보고 싶다!**
* 사용자가 떠올린 간단한 음을 입력하면 음에 맞춰 노래를 생성해주는 AI
* 특정 장르의 음악을 계속해서 생성해주는 AI


<br>    
    
**시스템 구조도**
  
   ![image](https://user-images.githubusercontent.com/52736420/65112311-2c5fee00-da1a-11e9-868f-7eb271b33677.png)
   
   
<br>   
   
#### PLAN  
 
 
![schedule](https://user-images.githubusercontent.com/52736420/64063336-42a23780-cc2e-11e9-97fd-9e1de9192605.png) 
 

## Weekly records

<details>
<summary> week1 </summary>
<div markdown='1'>
  
 - *INPUT*  
 Fruit genie 를 활용한 입력장치  
 (magenta_fruit genie)
           
           구성요소
           1. 라즈베리 파이 : 터치를 받아 피오노 지니 소프트웨어로 전송하고 메모를 재생하는 노드앱 실행
           2. teensy dev 보드 : 터치 감지 및 소프트웨어 전송을 처리 
           
    ![structure](https://user-images.githubusercontent.com/52736420/64146446-00f4d500-ce58-11e9-8b8d-6e14b6356dc7.png)       

- *MODELING*  
음악을 LSTM 모델을 통해 학습 시킨 후, 사용자가 음을 입력하면 LSTM모델을 통하여 비슷한 느낌의 음악을 생성  
![image](https://user-images.githubusercontent.com/52736420/64146533-53ce8c80-ce58-11e9-899b-42cd9f715e0f.png)
  
- **진행상황**
1. 케라스 LSTM 모델로 작곡하기  
  : Music21 -> 20시간 학습시킨 결과, 추상적인 음악 -> 훨씬 깊고 복잡한 네트워크를 만들고 학습시킬 필요성   
     
2. 마젠타 melody-rnn으로 작곡하기  
  : pre-trained 모델을 가지고 음악을 생성 -> 다른 장르의 음악으로 커스터마이징된 모델 파라미터를 학습시키는 중  
     
3. 마젠타 music-VAE 모델로 작곡하기  
  : 최대 3개의 음을 조합하여 음악을 생성. -> pre-trained 모델을 돌려보기 위해 모델 실행 중

</div>
</details>

---  
<details>
<summary> week2 </summary>
<div markdown="1">
  
<br>  

- **진행상황**  
1. 라즈베리 파이  
  : mpg123 : 오디오 출력 역할 부분 문제 -> 버전을 맞추거나, 따로 오디오 출력 라이브러리를 설치할 계획  
    
2. teensy dev 보드  
  : 스케치를 다운 받아 터치에 따른 반응 변화 확인 V  
  
  ![image](https://user-images.githubusercontent.com/52736420/64146977-d9067100-ce59-11e9-9e3f-5c0b23ceb1a7.png)



</div>
</details>

---  

<details>
<summary> week3 </summary>
<div markdown='1'>

<br>  
  
- **진행상황**  
 1. 라즈베리 파이   
    : 오디오 출력 부분 오류 -> 소프트웨어와 직접 연결 방식 선택 (USB, serial 통신)  
      
 2. teensy dev 보드   
    : 터치 인식 후 소리 재생 확인 V  
       
 3. melody RNN  
    : K-POP 1990년대 음악의 midi 파일 학습 
      
 4. music VAE  
    : JAZZ 생성 구축 모델, k-pop으로 학습 check point 300까지 진행 (CNN)
    
 5. score2perf  
    : 가장 음악다운 음악을 생성해주는 모델, classic 생성 구축 모델 (transformer)
 


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

<br>

### ◎ input system (fruit music) 구현 절차
  
  <br>

- **필요한 것?**  
  
ONLY teensy USB board 3.2 ! ! ! 
  
  ![image](https://user-images.githubusercontent.com/52736420/65213127-dbb2c880-dadf-11e9-9949-0b48344b8ef6.png)

- **teensy dev borad 3.2**  
![image](https://user-images.githubusercontent.com/52736420/65213379-e588fb80-dae0-11e9-96c2-f06ecaf98aff.png)  


      먼저 아두이노를 설치한다.
      
      위의 그림과 같이 해당 핀 8개가 터치인식을 담당하므로 해당 8개의 핀에 리드를 연결한다.
      리드 연결 전에 고정되게 납땜을 하면 좋다.
      연결된 리드에 과일을 연결해 놓는다.
      그 후, USB를 연결하고 fruit-genie-fw.ino 를 업로드하면 teensy 창이 뜨는데 버튼을 누르면 된다.
      그러면 업로드 완료!
      
      fruit-genie-fw.ino 는 magenta 오픈소스를 활용하였다.
      // git clone을 통해 fruit-genie-fw.ino 를 다운! //
    

- **python 을 활용한 serial data 실시간 받기/음 추출**  
             
  *1. window command 창에 pyserial 을 설치한다.*
     
      pip install pyserial  
     
  *2. jupyter notebook 을 키고 아래 라이브러리를 import한다.*  
  // git clone을 통해 fruit_music.py 를 실행시키는 것도 가능! //
     
      import serial
      import time
      import signal
      import threading
      import winsound #소리 재생
      
   *3. 코드를 실행시키고 과일을 눌러보자!*  
   
        만약 여기서 실행이 안된다면 teensy 의 baud, port 넘버를 확인해 보자.  
        
   ![image](https://user-images.githubusercontent.com/52736420/65213810-92b04380-dae2-11e9-9810-630bca19031d.png)
   
### ◎ software (magenta) 구현 절차
  <br>

- **설치 및 환경변수 설정**  
  <br>
  - **CPU 사용**
  <br>
  <br>
     최신 magenta(ver 1.1.3) 설치 시 tensorflow 1.1.15 이상 설치 하라는 오류가 나오므로 

        pip install magenta==1.1.2

     로 magenta를 설치한다
     mageta github에서 install에서 pip package에서 다음과 사진과 같이 들어간 후 magenta 파일을 다운 받는다.

     ![image](https://user-images.githubusercontent.com/52375252/65214531-47e3fb00-dae5-11e9-8e5f-8d79d7a5f505.png)



  <br>
  
    - **GPU 사용** 
  <br>
    최신 magenta gpu(ver 1.1.3) 설치 시 tensorflow 1.1.15 이상 설치 하라는 오류가 나오므로 

          pip install magenta_gpu==1.1.2

    로 magenta(ver 1.1.2)를 설치한다.
      <br>
    mageta github에서 install에서 pip package에서 다음과 사진과 같이 들어간 후 magenta 파일을 다운 받는다.

    ![image](https://user-images.githubusercontent.com/52375252/65214394-cd1ae000-dae4-11e9-9a94-665a1d429b98.png)


    gpu 사용을 위해 CUDA와 cuDNN을 다운받아 설치한다. CUDA, cuDNN 설치 후 환경변수 설정을 위해 다음과 같이 입력한다.

          export LD_LIBRARY_PATH=”$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64”
          export CUDA_HOME=/usr/local/cuda-10.0
          //cuda-(현재 자신의 cuda버전)//

    gpu가 잘 설치 되었는지 확인하기 위해 다음 코드를 사용한다.

          import sys
          import numpy as np
          import tensorflow as tf
          from datetime import datetime
          shape=(int(10000),int(10000))
          with tf.device("/gpu:0"):
              random_matrix = tf.random_uniform(shape=shape, minval=0, maxval=1)
              dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
              sum_operation = tf.reduce_sum(dot_operation)
          startTime = datetime.now()
          with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as session:
            result = session.run(sum_operation)
            print(result)
            print("\n" * 2)
            print("Time taken:", datetime.now() - startTime)
            print("\n" * 2)    
