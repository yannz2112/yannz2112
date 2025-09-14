import time
import random

print('SELAMAT DATANG DI NAMAKAMU AI!')
time.sleep(0.7)
print('''
NAMA KAMU AI
Dibuat : Namakamu
Versi : 1.0.0
Tanggal buat : xx/xx/xxxx
''')

question = input('BERTANYA WITH NAMAKAMU AI :')
if question == 'kamu dibuat oleh siapa':
    print('Saya dibuat oleh namakamu')
elif question == 'Hari ini hari apa':
    print('Hari ini adalah hari (hari) tanggal xx bulan xx tahun xxxx')
else:
    print('Bot sedang mencari jawaban...')
    time.sleep(5)
    print('Maaf bot sedang tidak bisa merespon jawaban kamu, cobalah nanti')
    exit()
