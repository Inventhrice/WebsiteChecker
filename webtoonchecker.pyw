import requests
import time
from plyer import notification

def sendNotif(num):
    if(num==1):
        notification.notify(title='Dark Magician', message = 'Dark Magician has updated!', app_name = 'Webcomic has updated',app_icon = 'dmimg.ico')
    if(num==2):
        notification.notify(title='Return of Mount Hua Sect', message = 'Return of Mount Hua Sect has updated!', app_name = 'Webcomic has updated',app_icon = 'mhimg.ico')
    if(num==3):
        notification.notify(title='Villain To Kill', message = 'Villain To Kill has updated!', app_name = 'Webcomic has updated',app_icon = 'vtkimg.ico')
    if(num==4):
        notification.notify(title='Player Who Can\'t Level Up', message = 'Player Who Can\'t Level Up has updated!', app_name = 'Webcomic has updated',app_icon = 'pcluimg.ico')
        

url = "https://www.asurascans.com/"

obj = open("number.txt","r+")
dmep = int(obj.read(2)) #dark magician ep num
mhep = int(obj.read(2)) #mount hua ep num
vtkep = int(obj.read(2)) #villain to kill ep num
pcluep = int(obj.read(2)) #player who cant level up ep num
obj.close()
i = 1
while(i == 1):
    dmurl = url + "the-dark-magician-transmigrates-after-66666-years-chapter-" + str(dmep) + "/"
    mhurl = url + "return-of-the-mount-hua-sect-chapter-" + str(mhep) + "/"
    vtkurl = url + "villain-to-kill-chapter-" + str(vtkep) + "/"
    pclurl = url + "player-who-cant-level-up-chapter-" + str(pcluep) + "/"

    if(requests.get(dmurl).status_code == 200):
        sendNotif(1)
        dmep += 1
    if(requests.get(mhurl).status_code == 200):
        sendNotif(2)
        mhep += 1
    if(requests.get(vtkurl).status_code == 200):
        sendNotif(3)
        vtkep += 1
    if(requests.get(pclurl).status_code == 200):
        sendNotif(4)
        pcluep += 1

    obj = open("number.txt","w")
    obj.write(str(dmep))
    obj.write(str(mhep))
    obj.write(str(vtkep))
    obj.write(str(pcluep))
    obj.close()

    time.sleep(86400)
    


