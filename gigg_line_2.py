from microbit import *
import gigglebot

def main():

    check = True
    threshold = 100
    while check:
            # Obtiene la lectura de los sensores de línea
            # El segundo parámetro puede ser LEFT, RIGHT o BOTH
            # Si se lee un sólo sensor, devuelve un entero
            # Si se leen los dos sensores, se devuelve una tupla de 2 enteros (izquierdo, derecho)
            # Los valores devueltos están entre 0 y 1024, cuanto mayor, más clara es la superficie
            # sobre la que se encuentra el robot.
        try:
            values = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
        except OSError:
            if button_a.is_pressed():
                check = False
        else:
            if values[0] < threshold and values[1] < threshold:
                gigglebot.drive(gigglebot.FORWARD,10)
            elif values[0] < threshold and values[1] > threshold:
               gigglebot.turn(gigglebot.RIGHT,10)
            elif values[0] > threshold and values[1] < threshold:
                gigglebot.turn(gigglebot.LEFT,10)


if __name__ == "__main__":
    main()
