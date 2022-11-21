#!/usr/bin/env python3
london_co = {
     "r1": {
         "location": "21 New Globe Walk",
         "vendor": "Cisco",
         "model": "4451",
         "ios": "15.4",
         "ip": "10.255.0.1"
     },
     "r2": {
         "location": "21 New Globe Walk",
         "vendor": "Cisco",
         "model": "4451",
         "ios": "15.4",
         "ip": "10.255.0.2"
     },
     "sw1": {
          "location": "21 New Globe Walk",
          "vendor": "Cisco",
          "model": "3850",
          "ios": "3.6.XE",
          "ip": "10.255.0.101",
          "vlans": "10,20,30",
          "routing": True
     }
}

ans = input("Введите имя устройства: ")
ans_param = input(f"Введите имя параметра {list(london_co[ans].keys())}: ")
if ans_param in list(london_co[ans].keys()):
        print(london_co[ans][ans_param])
else:
        print("Нет такого параметра!")



