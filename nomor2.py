import socket
from binascii import hexlify

def konversiIP(s):  
  
    # Inisialisasi variable count
    count = 0  
  
    # Mengecek jumlah oktet pada IP Address  
    for i in range(0, len(s)):  
        if(s[i] == '.'):  
            count = count+1  
    if(count != 3):  
        return 0  
  
    # Mengecek periode IP yaitu range 0-255  
    set_val= set()  
    for i in range(0, 256):  
        set_val.add(str(i))  
    count = 0  
    temp = ""  
    for i in range(0, len(s)):  
        if(s[i] != '.'):  
            temp = temp+s[i]  
        else:  
            if(temp in set_val):  
                count = count+1  
            temp = ""  
    if(temp in set_val):  
        count = count+1  
  
    # Verifikasi semua kondisi  
    if(count == 4):  
        for alamatIP in [ip_addr]:
            packed_ip_addr = socket.inet_aton(alamatIP)
            unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
            return ("IP Address : {} => Packed: {}, Unpacked: {}".format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)) 
    else:  
        return 'IP tidak valid'  

if __name__ == '__main__':
    ip_addr = input('Masukan IP Address: ')  
    print(konversiIP(ip_addr))  