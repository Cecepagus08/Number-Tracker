
Phone Number Tracker adalah script Python sederhana yang digunakan untuk melacak informasi dasar dari nomor telepon yang dimasukkan pengguna, seperti lokasi, operator, validitas, dan zona waktu.



## Ikutin cara ini
## Buka termux dam masukkan perintah
## Tulis perintahnya satu satu
```sh
pkg update && pkg upgrade -y
pkg install python
pkg install git
git clone https://github.com/Cecepagus08/Number-Tracker.git
pip install phonenumbers
cd phone-number-tracker
python TrackNumber.py
```



### Contoh Hasil

tampilan hasil informasi nya begini

```plaintext
--- Phone Number Information ---
Location          : Indonesia
Region Code       : ID
Operator          : Telkomsel
Valid Number      : True
Formatted Number  : +62 812-3456-7890
Time Zones        : Asia/Jakarta
```


