import cv2 
import time
import pyautogui
import webbrowser
import os 


def send_whatsapp_message():
    phone_number="asdasdad"
    timestamp=time.strftime('%d %H %M')
    message=f"hareket tespit edildi tarih saat:{timestamp}"
    web_url=f"https://web.whatsapp.com/send?phone{phone_number}&tetx{message}"

    try:
        print(f"[INFO] whatsapp uzeridnen mesaj gonderiuliyor:{message}")
        webbrowser.Opera(web_url)
        time.sleep(20)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl','w')
        time.sleep(2)
        print("[INFO] whatsapp mesaji gonderildi")
    except Exception as e:
        print("[ERROR] whatsapp mesaji gonderilemedi")
        return False;

def main():
    pyautogui.PAUSE=1.5
    #kamerayi olaray dahil et
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Kamera Acilamadi")
        return
    #mog2 algoritmasi
    backsub=cv2.createBackgroundSubtractorMOG2(

        history=500,
        varThreshold=25,
        detectShadows=True
    )

    last_motion=0
    cooldown=10

    while True:
        ret,frame=cap.read()
        if not ret:
            print("[EROR] kamera goruntusu alunamadi")
            break
        #hareket algilama
        fgMask=backsub.apply(frame)
        _,thres=cv2.threshold(fgMask,127,255,cv2.THRESH_BINARY)
        thres=cv2.erode(thres,None,iteration=2)
        thres=cv2.dilate(thres,None,iterations=2)

        #hareket eden bolgelerin sinirlari
        contours,_=cv2.findContours(thres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        motion_detected=False

        for countour in contours:
            if cv2.contourArea(countour)>1500:
                continue
            motion_detected=True
            break

        current_time=time.time()

        if motion_detected and (current_time-last_motion>cooldown):
            print("[INFO] hareket algilandi")
            #whatsapp mesaji gonde\
            if send_whatsapp_message():
                last_motion_time=current_time
                cv2.putText(frame,"Hareket algilandi",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,266),2)
            else:
                print("[WARNING] mesajin gitmedi")    
        else:
             cv2.putText(frame,"Hareket yok",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,266),2)

        cv2.imshow("Kamera",frame)     
        cv2.imshow("Kamera maskesi",thres)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break     
    cap.release()
    cv2.destroyAllWindows()

if __name__ =='__name__':
 main()