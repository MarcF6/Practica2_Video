# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import os
import moviepy.editor as mp



# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    prueba = int(input("Introduce un numero de la opción que quieres ejecutar:\n"
                       "1-Tener información de un vídeo\n"
                       "2 Cambiar nombre vídeo\n"
                       "3-Cambiar calidad de vídeo\n"
                       "4-Cambiar el codec del vídeo\n"))



    if(prueba==1):
        archivo_input = input("Introduce el directorio del vídeo");
        print("Duracion en segundos: ")
        print(os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "+archivo_input+""))

        print("Rate: ")
        print(os.system("ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 " +archivo_input +""))

        print("Codec name: ")
        print(os.system("ffprobe -v error -show_entries format=codec_name -of default=noprint_wrappers=1:nokey=1 " + archivo_input))


    if(prueba==2):
        archivo_input = input("Introduce el directorio del vídeo");
        archivo_output = input("Introduce el directorio y el nuevo nombre del vídeo")
        os.rename(archivo_input,archivo_output)

    if(prueba==3):
        archivo_input = input("Introduce el directorio del vídeo");
        archivo_output = input("Introduce el directorio y el nuevo nombre del vídeo")
        clip = mp.VideoFileClip(archivo_input)
        clip_resized = clip.resize(height=360)
        clip_resized.write_videofile(archivo_output)

    if(prueba==4):
        print("Ejemplo: /home/Escritorio/input.mp4")
        archivo_input = input("Introduce el directorio del vídeo")
        print("Ejemplo: /home/Escritorio/output.avi")
        archivo_output = input("Introduce el directorio + el nombre del video + el nuevo formato")

        os.system("ffmpeg -i "+archivo_input+" "+archivo_output+"")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
