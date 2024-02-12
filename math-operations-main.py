"""Sonlar ustida amallar bajaruvchi dastur"""
def ask_number():
    """Even or odd function"""
    while True:
        try:
            print("Istalgan son kiriting.")
            son = int(input(">>> "))
            if son % 2 == 0:
                print(f"{son} Juft son.")
            else:
                print(f"{son} Toq son.")
        except ValueError:
            print("Iltimos butun son kiriting.")
        takror = input("Davom ettirish (1)\nOrtga qaytish (0): ")
        if takror == '0':
            break

def find_largest():
    """Katta sonni aniqlaydigan funksiya"""
    while True:
        try:
            num1 = float(input("1-son: "))
            num2 = float(input("2-son: "))
            num3 = float(input("3-son: "))
            largest = max(num1, num2, num3)
            print("Eng katta qiymat:", largest)
        except ValueError:
            print("Iltimos butun son kiriting.")
        takror = input("Davom ettirish (1)\nOrtga qaytish (0): ")
        if takror == '0':
            break
    return largest
    
def son_hisobla():
    """2 ta son ustida amallar bajaruvchi funksiya"""
    while True:
        print("Istalgan ikkita son kiriting: ")
        try:
            son1 = float(input("Birinchi sonni kiriting \n>>> "))
            son2 = float(input("Ikkinchi sonni kiriting \n>>> "))
            if son1 == son2:
                print(f"{son1} = {son2}")
            elif son1 > son2:
                print(f"{son1} > {son2}")
            else:
                print(f"{son1} < {son2}")
            
            print(f"{son1} + {son2} = {son1 + son2}")
            print(f"{son1} - {son2} = {son1 - son2}")
            print(f"{son1} * {son2} = {son1 * son2}")
            print(f"{son1} / {son2} = {son1 / son2}")
        except ValueError:
            print("Iltimos butun son kiriting.")
        takror = input("Davom ettirish (1)\nOrtga qaytish (0): ")
        if takror == '0':
            break

def kv_kub():
    """Sonlar kvadrati va kubini hisoblovchi funksiya"""
    while True:
        try:
            son = float(input("Istalgan son kiriting: "))
            kv = f"{son} sonining kvadrati {son**2} ga teng"
            kub = f"{son} sonining kubi {son**3} ga teng"
            print(kv)
            print(kub)
        except ValueError:
            print("Iltimos butun son kiriting.")
        takror = input("Davom ettirish (1)\nOrtga qaytish (0): ")
        if takror == '0':
            break

def find_prime_numbers():
    """Ikki son oralig'idagi tub sonlarni aniqlovchi funksiya"""
    prime_numbers = []
    while True:
        try:
            a = int(input("Boshlanuvchi raqamni kiriting: "))
            b = int(input("Tugovchi raqamni kiriting: "))
            if a >= b:
                print("Tugovchi raqam boshlanuvchidan katta bo'lishi kerak.Qayta urining.")
            else:
                for n in range(a, b):
                    if n > 1:
                        tub = True
                        for x in range(2,int(n**0.5)+1):
                            if n % x == 0:
                                tub = False
                                break
                        if tub:
                            prime_numbers.append(n)
                print(f"{a} va {b} sonlari oralig'idagi tub sonlar: {prime_numbers}")
        except ValueError:
            print("Iltimos butun son kiriting.")
            
        takror = input("Davom ettirish (1)\nOrtga qaytish (0): ")
        if takror == '0':
            break
    return prime_numbers
    
def find_fibanacci():
    """Foydalanuvchidan raqam qabul qilib fibanacci ro'yxati chiqaruvchi funksiya"""
    fibanacci_list = [0, 1]
    while True:
        try:
            n = int(input("Fibanacci ketma ketligi uchun raqam kiriting: "))
            if n < 1:
                print("Iltimos 0 dan katta musbat son kiriting.")
            else:
                for i in range(2, n):
                    fibanacci_list.append(fibanacci_list[i-1]+fibanacci_list[i-2])
                print(fibanacci_list)
        except ValueError:
            print("Iltimos butun son kiriting.")
        
        takror = input("Davom ettirish (1)\nOrtga qaytish (0): ")
        if takror == '0':
            break
    return fibanacci_list

def main():
    while True:
        try:
            print("Amallardan birini tanlang:\n"
                  "1. Juft va Toq sonni aniqlash.\n"
                  "2. Raqamlardan eng kattasini aniqlash.\n"
                  "3. Sonlar ustida amallar bajarish.\n"
                  "4. Son kvadrati va kubini hisoblash. \n"
                  "5. Tub sonlarni aniqlash. \n"
                  "6. Fibanacci ketma-ketligi \n"
                  "0. Chiqish")
            javob = int(input(">>> "))
            if javob == 1:
                ask_number()
            elif javob == 2:
                print("Eng katta qiymat: ", find_largest())
            elif javob == 3:
                son_hisobla()
            elif javob == 4:
                kv_kub()
            elif javob == 5:
                find_prime_numbers()
            elif javob == 6:
                find_fibanacci()
            elif javob == 0:
                break
        except ValueError:
            print("Iltimos mavjud raqamlardan birini tanlang.")

main()