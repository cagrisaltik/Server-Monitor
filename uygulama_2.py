import psutil 
import speedtest
from flask import Flask, render_template 

app = Flask(__name__, template_folder='/etc/uygulama') 

@app.route("/")
    
   

# Byte to MB 

  
  #INT Hızı Ölçme



def home():

    #CPU Kullanım Yüzdesi 

    cpu_percent = psutil.cpu_percent()
   

      # Bellek Kullanımı 

    memory = psutil.virtual_memory()

    memory_percent = memory.percent

        #Disk Kullanımı 

    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    used = round(disk.used/1024.0//1024.0/1024.0,1)
    disk_used = used
    free = round(disk.free/1024.0//1024.0/1024.0,1)
    disk_free = free 



    # Network I / O 
    network = psutil.net_io_counters(nowrap=True)
    network_input = network.bytes_recv
    network_giris = network_input
    giris_kb = round(network_giris/1024.0//1024.0/1024.0,1)
    giris = giris_kb
    network_output = network.bytes_sent
    network_cikis = network_output
    cikis_kb = round(network_cikis/1024.0//1024.0/1024.0,1)
    cikis = cikis_kb


    
    
    #Verileri Flaksa Aktarma
    return render_template('index.html',cpu_percent=cpu_percent,memory_percent=memory_percent,disk_percent=disk_percent,disk_used=disk_used,disk_free=disk_free,giris=giris,cikis=cikis)
    
if __name__ == '__main__':
           app.run(host="0.0.0.0",port=80)
