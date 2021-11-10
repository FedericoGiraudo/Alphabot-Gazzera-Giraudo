import socket as sck
import time
import RPi.GPIO as GPIO
import sqlite3


class AlphaBot(object):
    
    def __init__(self, in1=13, in2=12, ena=6, in3=21, in4=20, enb=26):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb
        self.PA  = 25
        self.PB  = 25
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        self.PWMA = GPIO.PWM(self.ENA,500)
        self.PWMB = GPIO.PWM(self.ENB,500)
        self.PWMA.start(self.PA)
        self.PWMB.start(self.PB)
        self.stop()
        
    def stop(self):
            self.PWMA.ChangeDutyCycle(0)
            self.PWMB.ChangeDutyCycle(0)
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.LOW)
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.LOW)
            
    def left(self, t):
        self.PWMA.ChangeDutyCycle(self.PA)
        self.PWMB.ChangeDutyCycle(self.PB)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(t/1000)
        Ab.stop()
        

    def right(self,t):
        self.PWMA.ChangeDutyCycle(self.PA)
        self.PWMB.ChangeDutyCycle(self.PB)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        time.sleep(t/1000)
        Ab.stop()

    def forward(self,t, speed =30):
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(t/1000)
        Ab.stop()
    
    def forward_2(self, speed=15):
        while speed<=100 :
            self.PWMA.ChangeDutyCycle(speed)
            self.PWMB.ChangeDutyCycle(speed)
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            time.sleep(0.2)
            speed+=2
            print(speed)
            
        

    def backward(self,t, speed =30):
        self.PWMA.ChangeDutyCycle(speed)
        self.PWMB.ChangeDutyCycle(speed)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        time.sleep(t/1000)
        Ab.stop()
        
    def set_pwm_a(self, value):
        self.PA = value
        self.PWMA.ChangeDutyCycle(self.PA)

    def set_pwm_b(self, value):
        self.PB = value
        self.PWMB.ChangeDutyCycle(self.PB)    
        
    def set_motor(self, left, right):
        if (right >= 0) and (right <= 100):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif (right < 0) and (right >= -100):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(0 - right)
        if (left >= 0) and (left <= 100):
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif (left < 0) and (left >= -100):
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)

if __name__ == '__main__':
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    s.bind(('0.0.0.0', 5000)) #(indirizzo ip della macchina server (0.0.0.0 = il mio ip), porta
    s.listen() #alloca i dati
    conn, addr = s.accept() #dati ricevuti(data), addr Ã¨ una tupla con indirizzo ip del client e porta del client
    Ab = AlphaBot()      
    while True:
        data= conn.recv(4096).decode() 
        conn1 = sqlite3.connect('./comandi.db')
        cur = conn1.cursor()
        query = f"SELECT funzione FROM movimenti WHERE movimento = '{data}'"
        print(query)
        cur.execute (query)
        rows = cur.fetchall()
        for row in rows:
            print(row[0])
        
        if "," in row[0]:
            comandi = row[0].split(",")
            for comando in comandi:
                c = comando.split(" ")  
                if(c[0]=='r'):
                    Ab.right(float(c[1]))
                if(c[0]=='l'):
                    Ab.left(float(c[1]))
                if(c[0]=='s'):
                    Ab.stop()
                if(c[0]=='i'):
                    Ab.backward(float(c[1]))
                if(c[0]=='a'):
                    Ab.forward(float(c[1]))
                if(c[0]=='aa'):
                    Ab.forward_2(float(c[1]))               
        else: 
            comando = row[0].split(" ")  
            if(comando[0]=='r'):
                Ab.right(float(comando[1]))
            if(comando[0]=='l'):
                Ab.left(float(comando[1]))
            if(comando[0]=='s'):
                Ab.stop()
            if(comando[0]=='i'):
                Ab.backward(float(comando[1]))
            if(comando[0]=='a'):
                Ab.forward(float(comando[1]))
            if(comando[0]=='aa'):
                Ab.forward_2(float(comando[1]))
        
sck.close() 
            




