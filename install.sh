#!/bin/bash

# Hedef dizini oluşturma
mkdir -p /etc/uygulama

# Dosyaları hedef dizine kopyalama
cp uygulama_2.py /etc/uygulama
cp index.html /etc/uygulama
cp requirements.txt /etc/uygulama
# Diğer dosyaları buraya ekleyin

#Pip Install
apt install python3-pip 

# Gerekli bağımlılıkları yükleme
pip install -r requirements.txt

cp system-monitor.service /etc/systemd/system

systemctl daemon-reload
systemctl start system-monitor.service
systemctl enable system-monitor.service


# Python uygulamasını çalıştırma
python /etc/uygulama/uygulama_2.py 

