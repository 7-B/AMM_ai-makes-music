import serial # serial 통신
import time #시간 기능
import signal #signal 처리
import threading #thread 실행
import winsound #sound 출력

line = []
piano = {'do': 261, 're':293, 'mi':329, 'pa':349, 'sol':391, 'ra':440, 'si':493, 'doo':530}

mel1 = ['do']
dur1 = [3]
music1 = zip(mel1,dur1)

mel2 = ['re']
dur2 = [3]
music2 = zip(mel2,dur2)

mel3 = ['mi']
dur3 = [3]
music3 = zip(mel3,dur3)

mel4 = ['pa']
dur4 = [3]
music4 = zip(mel4,dur4)

mel5 = ['sol']
dur5 = [3]
music5 = zip(mel5,dur5)

mel6 = ['ra']
dur6 = [3]
music6 = zip(mel6,dur6)

mel7 = ['si']
dur7 = [3]
music7 = zip(mel7, dur7)

mel8 = ['do']
dur8 = [3]
music8 = zip(mel8, dur8)

port = 'COM3'
baud = 9600

for melody, duration in music1:
    duration = duration #duration 은 3으로 동일하기 때문에 music1에서 추출한 것만 사용해도 무방
    
exitThread = False
tmpli1 = []
tmpli2 = []
tmpli3 = []
tmpli4 = []
tmpli5 = []
tmpli6 = []
tmpli7 = []
tmpli8 = []
out_sound = [] #결과 리스트

def handler(signum, frame): #DB 관련 정리 후 프로그램 종료
     exitThread = True

def parsing_data(data): #소리출력 함수
    global tmp
    global duration
    tmp = data
        
    if (tmp==['2', '\r', '\n']):
        del tmpli2[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli7[:]
        del tmpli8[:]
        tmpli1.append(tmp)
        if (tmpli1==[['2', '\r', '\n']]):
            winsound.Beep(piano['do'], 1000//duration)
            out_sound.append(0)


    elif (tmp==['1', '\r', '\n']):
        del tmpli1[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli7[:]
        del tmpli8[:]
        tmpli2.append(tmp)
        if (tmpli2 ==[['1','\r','\n']]):
            winsound.Beep(piano['re'], 1000//duration)
            out_sound.append(2)
            
    elif (tmp==['1', '2', '8', '\r', '\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli7[:]
        del tmpli8[:]
        tmpli3.append(tmp)
        if (tmpli3 ==[['1', '2', '8', '\r', '\n']]):
            winsound.Beep(piano['mi'], 1000//duration)
            out_sound.append(4)
       
    elif (tmp==['4', '\r', '\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli3[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli7[:]
        del tmpli8[:]
        tmpli4.append(tmp)
        if (tmpli4==[['4', '\r', '\n']]):
            winsound.Beep(piano['pa'], 1000//duration)
            out_sound.append(5)
            
    elif (tmp==['8', '\r', '\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli6[:]
        del tmpli7[:]
        del tmpli8[:]
        tmpli5.append(tmp)
        if (tmpli5==[['8', '\r', '\n']]):
            winsound.Beep(piano['sol'], 1000//duration)
            out_sound.append(7)
            
    elif (tmp==['1','6', '\r', '\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli7[:]
        del tmpli8[:]
        tmpli6.append(tmp)
        if (tmpli6==[['1','6', '\r', '\n']]):
            winsound.Beep(piano['ra'], 1000//duration)
            out_sound.append(9)
            
    elif (tmp==['3','2', '\r', '\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli8[:]
        tmpli7.append(tmp)
        if (tmpli7==[['3','2', '\r', '\n']]):
            winsound.Beep(piano['si'], 1000//duration)
            out_sound.append(11)
            
    elif (tmp==['6','4', '\r', '\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli7[:]       
        tmpli8.append(tmp)
        if (tmpli8==[['6','4', '\r', '\n']]):
            winsound.Beep(piano['doo'], 1000//duration)
            out_sound.append(12)
    elif (tmp==['0', '\r','\n']):
        del tmpli1[:]
        del tmpli2[:]
        del tmpli3[:]
        del tmpli4[:]
        del tmpli5[:]
        del tmpli6[:]
        del tmpli7[:]
        del tmpli8[:]

def readThread(ser):
    global line
    global exitThread
    while not exitThread: #종료가 나오기 전까지 반복
        for c in ser.read(): 
            line.append(chr(c))
            if c == 10: #라인의 끝 (48,13,11 이 한 라인)
                parsing_data(line) #소리함수 출력
                del line[:]


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler) #DB정리 코드 등록
    ser = serial.Serial(port, baud, timeout=0) #지정된 port,baudrate 를 열기
    thread = threading.Thread(target=readThread, args=(ser,)) #ser 을 전달해 readThread 실행 
    thread.start()