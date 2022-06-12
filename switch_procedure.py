switch_status = False # ไฟปิดอยู่

def turn_on(): #ฟังชั่นเปิดไฟ
    global switch_status
    switch_status = True
    print("ไฟเปิด")

def turn_off(): #ฟังชั่นปิดไฟ
    global switch_status
    switch_status = False
    print("ไฟปิด")

if __name__ == "__main__":
    print(f'สถานะไฟ: {switch_status}')
    turn_on()
    #turn_off()