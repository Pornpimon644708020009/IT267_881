switch_status = False #สถานะของไฟเปิดปิด

def turnon(): #ประกาศชื่อฟังก์ชั่น
    global switch_status 
    switch_status = True
    print ("ไฟเปิด")

def turnoff(): #ฟังก์ชั้นปิดไฟ
    global switch_status 
    switch_status = False
    print ("ไฟปิด")

if __name__ == "__main__":
 print(f'สถานะไฟ:{switch_status}') #สามารถเปลี่ยนเป็น If-else ได้ ให้เป็นฟังก์ชันเดียวได้
 turnon ()
 turnoff ()
