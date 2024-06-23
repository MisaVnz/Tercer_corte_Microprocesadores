import utime
from machine import Pin

print(f'hola soy el Rasperry Pi Pico')

def app():
    
    # Salidas Digitales GPIO Raspberry Pi Pico
    led_amarillo  = Pin(2, Pin.OUT)
    led_azul      = Pin(3, Pin.OUT)
    led_rojo      = Pin(4, Pin.OUT)
    led_4         = Pin(5, Pin.OUT)
    led_5         = Pin(6, Pin.OUT)
    led_c         = Pin(25, Pin.OUT)

    # Entradas Digitales GPIO Raspberry Pi Pico
    boton_izquierda = Pin(17, Pin.IN, Pin.PULL_UP)
    boton_derecha   = Pin(16, Pin.IN)
    print(f'{boton_izquierda}')
    led_c.value(1)   
    # Almaceno los leds en una lista
    leds = [led_amarillo, led_azul, led_rojo, led_4, led_5]
    
    #variables de desplazamiento
    izquierda = True
    derecha   = False
    
    for i in range(5):
        leds[i].off()

    #Ciclo infinito
    while True:
        print('app runnning')
        #Si presiona el botón de la izquierda
        if boton_izquierda.value() == 0:
            izquierda = True
            derecha   = False
            print('Se presiono el boton izquierdo')
            
        #Si presiona el botón de la derecha
        if boton_derecha.value() == 1:
            izquierda = False
            derecha   = True
            print('Se presiono el boton derecho')
            
        #Si presiona ambos botones
        if boton_izquierda.value() == 0 and boton_derecha.value() == 1 :
            izquierda = True
            derecha   = True
            print('Se presiono los dos botones')
        
        #Rotación de leds a la izquierda
        if izquierda and not derecha:
            for i in range(5):
                leds[i].on()
                utime.sleep_ms(100)
                leds[i].off()
                utime.sleep_ms(100)
                
        #Rotación de leds a la derecha
        if not izquierda and derecha:
            for i in range(4,-1,-1):
                leds[i].on()
                utime.sleep_ms(100)
                leds[i].off()
                utime.sleep_ms(100)
                
        if  izquierda and derecha:
            for i in range(5):
                leds[i].on()
                
if __name__ == '__main__':
    app()