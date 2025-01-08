from datetime import *
from re import X
feedbackdict={
    "ร้านนี้บริการดีมากค่ะ":5,
    "ปรุงสดใหม่ทุกชาม":4,
    "เส้นเหนียวนุ่ม น้ำซุปเข้มข้น":4,
    "ปริมาณเหมาะสมต่อราคา":3,
    "ภายในร้านสะอาด บรรยากาศดี":5,
    "ร้านข้างๆอร่อยมากค่ะ":5
}
Noodle = {
    'เล็กน้ำใส' : 50,
    'เล็กน้ำตก' : 50,
    'เล็กต้มยำ' : 50,
    'ใหญ่น้ำใส' : 50,
    'ใหญ่น้ำตก' : 50,
    'ใหญ่ต้มยำ' : 50,
    'บะหมี่น้ำใส' : 50,
    'บะหมี่น้ำตก' : 50,
    'บะหมี่ต้มยำ' : 50,
    'วุ้นเส้นน้ำตก' : 50,
    'วุ้นเส้นต้มยำ' : 50,
    'วุ้นเส้นน้ำใส' : 50,
    'ตับหวาน' : 55,
    'ยำมาม่า' : 40,
    
}

drink = {
    'โค๊ก' : 20,
    'สไปร์ท' : 20,
    'น้ำแดง' : 20,
    'น้ำเปล่า' : 10,
    'น้ำส้ม' : 15,
    'น้ำกระเจี๊ยบ' : 15,
    'น้ำเก๊กฮวย' : 15,
    'โอเลี้ยง' : 20
}

desert = {
    'แคปหมู' : 15,
    'หนังไก่' : 15,
    'ขนมถ้วย' : 20,
    'เฟรนซ์ฟรายส์' : 49,
    'เกี๊ยวทอด' : 49,
    'ลวกจิ้ม' : 49,
    'ไอศกรีมกะทิ' : 20,
    'น้ำแข็งไส' : 20
}

def mainmenu(cost):
    print("\t")
    thistime=datetime.now().hour
    print("===หัวข้อหลัก===")
    print("--------------")
    print("1.อาหาร")
    print("2.เครื่องดื่ม")
    print("3.ของว่าง")
    print("4.เติมเงิน")
    print("5.ความคิดเห็น")
    print("0.จบโปรแกรม")
    print(f" ยอดเงินคงเหลือ {cost} บาท ")
    print("------------------")


#list
listnoodle = list(Noodle)
listdrink = list(drink)
listdesert = list(desert)

def Drink(x) :
    print("------------------")
    if x==0:
        dri = input("ต้องการดื่มน้ำไหม (Y/N) : ").lower()
        print("------------------")
        if dri == 'y' :
            pass
        elif dri == 'n' :
            return 0
        else:
            return 0
    else :
        pass
    
    while True :
        a = 0
        print("0.ไม่เลือกรายการใดๆ")
        for i,o in drink.items() :
            a += 1
            print(f"{a}.{i} ราคา {o} บาท")
        print("------------------")
        work = int(input("เลือก : "))-1
        if work < 0 :
            return 0 
        print("------------------")
        m_input = listdrink[work]
        pricedrink = drink.get(m_input)
        return pricedrink

def Desert(x):
    print("------------------")
    if x==0:
        deserth = input("ต้องการของว่างไหม (Y/N) : ").lower()
        print("------------------")
        if deserth== 'y' :
                pass
        elif deserth == 'n' :
                return 0
        else:
                return 0
    else :
        pass
    while True :
        a = 0
        print("0.ไม่เลือกรายการใดๆ")
        for i,o in desert.items() :
            a += 1
            print(f"{a}.{i} ราคา {o} บาท")
        print("------------------")
        work = int(input("เลือก : "))-1
        if work < 0 :
            return 0 
        print("------------------")
        d_input = listdesert[work]
        pricedesert = desert.get(d_input)
        return pricedesert




def Noodlefunc(x) :
    print("------------------")
    if x==0:
        dri = input("ต้องการก๋วยเตี๋ยวไหม (Y/N) : ").lower  ()
        print("------------------")
        if dri == 'y' :
            pass
        elif dri == 'n' :
            return 0
        else:
            return 0
    else :
        pass
    a = 0
    print("รายการอาหาร")
    print("0.ไม่เลือกรายการใดๆ")
    for i,o in Noodle.items() :
        a += 1
        print(f"{a}.{i} ราคา {o} บาท")
    print("------------------")
    work = int(input("เลือก : "))-1
    if work < 0 :
            return 0 
    n_input = listnoodle[work]
    pricenood = Noodle.get(n_input)
    print("------------------")
    return pricenood
           


def greet (name) :
    thistime=datetime.now().hour
    today=datetime.today()
    print(today.strftime("%d/%m/%Y %H:%M "),"น.")
    if(thistime<=12) :
        thegreet="ตอนเช้า"
    elif(thistime>12 and thistime<18):
        thegreet="ตอนบ่าย"
    else:
        thegreet="ตอนค่ำ"
    print (f"สวัสดี{thegreet} คุณ {name}\n")


def farewell(name) :
    print(f"\nลาก่อนคุณ {name}")
    print("ขอบคุณที่ใช้บริการ")
    print("--------------")

def termmoney():
    money = int(input("เติมเงิน : "))
    return money

def verifyfeed():
    z=True
    while z:
        ver=input("คุณยืนยันที่จะเพิ่มความคิดเห็น (Y/N) : ").lower()
        if ver=='y':
            return ver
        elif ver=='n':
            feedbackdict.popitem()
            return ver
        else:
            print("-------------------")
            print("***คุณกรอกตัวเลือกผิด กรุณากรอกใหม่***")
            print("-------------------")

def feedback():
    z=True
    while z:
        try:
            print("-------------------")
            print("===แสดงความคิดเห็น===")
            print("-------------------")
            star=int(input("ให้คะแนนร้านนี้กี่ดาว 1-5 ดาว : "))
            if star>=5:
                star=5
            elif star<=0:
                star=1
            else:
                star=star
            print("-------------------")
            print(f"คุณให้จำนวน {star} ดาว")
            print("-------------------")
            commen=input("คุณมีความคิดเห็นหรือมีข้อปับปรุงอย่างไร : ")
            feedbackdict[commen]=star
            a=0
            for k,v in feedbackdict.items():
                a+=1
                print(f"{a}.{k} {v} ดาว")
            x=True
            while x:
                ask=verifyfeed()
                if ask=='y':
                    x=False
                    z=False
                elif ask=='n':
                    x=False
                    z=False
                else:
                    print("-------------------")
        except ValueError:
            print("------------------")
            print("กรุณากรอกให้ถูกต้อง")
            print("------------------")
        except ZeroDivisionError:
            print("------------------")
            print("เกิดข้อผิดพลาดกรุณาลองใหม่อีกครั้ง")
            print("------------------")
        except IndexError:
            print("------------------")
            print("ไม่พบข้อมูลในระบบ")
            print("------------------")
#readfeedback
def readfeed():
    x=True
    while x:
        try:
            serch=int(input("ค้นหาดาวที่ต้องการอ่าน : "))
            z=0
            if serch > 5 :
                print("กรุณาใส่ 1-5 ดาว")
                continue
            for view,star in feedbackdict.items():

                if star==serch:
                    z+=1
                    print(f"{z}. {view} {star} ดาว")
                
            feed=input("ต้องการแสดงความคิดเห็นหรือไม่? (Y/N): ").lower()
            if feed=='y':
                feedback()
                return
            else:
                return
        except ValueError:
            print("------------------")
            print("กรุณากรอกให้ถูกต้อง")
            print("------------------")
        except ZeroDivisionError:
            print("------------------")
            print("เกิดข้อผิดพลาดกรุณาลองใหม่อีกครั้ง")
            print("------------------")
        except IndexError:
            print("------------------")
            print("ไม่พบข้อมูลใน")
            print("------------------")
def readfeedback():
    while True:
        print("-------------------")
        print("1.อ่านความคิดเห็นทั้งหมด")
        print("2.ต้องการอ่านความคิดเห็นโดยตัวกรองดาว")
        feed=int(input("ต้องการอ่านในหัวข้อใด : "))
        print("-------------------")
        if feed <= 2 and feed > 0 :
            return feed
        else :
            print("\nไม่มีหัวข้อที่ท่านต้องการ")
            pass
def mainfeed():
    print("-------------------")
    print("===หัวข้อความคิดเห็น==")
    print("-------------------")
    print("1.อ่านความคิดเห็น")
    print("2.แสดงความคิดเห็น")

def readfeed_defult():
    a=0
    for k,v in feedbackdict.items():
        a+=1
        print(f"{a}.{k} {v} ดาว")
    feed=input("ต้องการแสดงความคิดเห็นหรือไม่? (Y/N): ").lower()
    if feed=='y':
        feedback()
    else:
        return    

# main program
print("      ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ")
print("\t♥ ♥ Welcome to Plaplern Noodle ♥ ♥")
print("      ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ")
myname= input("ชื่อ:")
greet(myname)

x=True
while x :
    try:
        cost = int(input("เติมเงิน : "))
        if cost==0 :
            print("กรุณาใส่ตัวเลขมากกว่า 0")
            x=True
        else :
            x=False
    except ValueError :
        print("กรุณาใส่ตัวเลข")


while True :
    try:
        mainmenu(cost) 
        work=int(input("เลือกหัวข้อเพื่อทำงาน : "))
        if work == 0 :
            farewell(myname)
            break
        elif work==1:
            pricenood = Noodlefunc(1)
            cost = cost - pricenood
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricenood
                continue
            print(f"เงินเหลือ {cost}")
            pricedrink = Drink(0)
            cost = cost - pricedrink
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricedrink
                continue
            print(f"เงินเหลือ {cost}")
            pricedes=Desert(0)
            cost = cost - pricedes
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricedes
                continue
            print(f"เงินเหลือ {cost}")
        elif work == 2:
            pricedrink = Drink(1)
            cost = cost - pricedrink
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricedrink
                continue
            print(f"เงินเหลือ {cost}")
            pricedes=Desert(0)
            cost = cost - pricedes
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricedes
                continue
            print(f"เงินเหลือ {cost}")
            pricenood = Noodlefunc(0)
            cost = cost - pricenood
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricenood
                continue
            print(f"เงินเหลือ {cost}")
        elif work == 3:
            pricedes=Desert(1)
            cost = cost - pricedes
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricedes
                continue

            print(f"เงินเหลือ {cost}")
            pricedrink = Drink(0)
            cost = cost - pricedrink
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricedrink
                continue
            print(f"เงินเหลือ {cost}")
            pricenood = Noodlefunc(0)
            cost = cost - pricenood
            if cost<0:
                print("เงินไม่พอ  *กรุณาเติมเงิน*")
                cost+=pricenood
                continue
            print(f"เงินเหลือ {cost}")
        elif work==4:
            money=termmoney()
            cost+=money
        elif work==5:
            mainfeed()
            feed_input=int(input("เลือกหัวข้อที่ต้องการ : "))
            if feed_input==1:
                feed_num=readfeedback()
                if feed_num==1:
                    readfeed_defult()
                elif feed_num==2:
                    readfeed()
            elif feed_input==2:
                feedback()
            else :
                print("\nไม่มีหัวข้อที่ท่านต้องการ")
        else :
            print("\nไม่มีหัวข้อที่ท่านต้องการ")
    except ValueError :
        print("\nกรุณาใส่ตัวเลข")
    except ZeroDivisionError:
        print("0")
    except IndexError:
        print("\nไม่พบรายการที่ท่านเลือก")