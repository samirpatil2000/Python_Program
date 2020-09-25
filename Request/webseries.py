import requests
THE_FLASH ="https://dl1.drbox.xyz/Series/The%20Flash/S06/The.Flash.S06E18.480p.HDTV.x264.TagName.mkv"
CHUCKS ="https://dl2.drbox.xyz/Series//Chuck/S01/Chuck%20S01E01%20480p%20TagName.mkv"
THE_BOYS="https://dl3.drbox.xyz/Series/The%20Boys%202019/S02/The.Boys.S02E05.480p.WEB.x264.TagName.mkv"


urlsGarabageList=[]
urlsList=[]

for season in range(1,7):
    for episode in range(1,24):
        if episode < 10:
            url="https://dl1.drbox.xyz/Series/The%20Flash/S0{}/The.Flash.S0{}E0{}.480p.HDTV.x264.TagName.mkv".format(season,season,episode)
            urlsGarabageList.append(url)
        else:
            url="https://dl1.drbox.xyz/Series/The%20Flash/S0{}/The.Flash.S0{}E{}.480p.HDTV.x264.TagName.mkv".format(season,season,episode)
            urlsGarabageList.append(url)
        print(url,end=" ")
        print('\n')

        
print(" All urls are printed ")
print("Now checking for valid urls")

with requests.Session() as a:
    for i in urlsGarabageList:
        r=a.get(i)
        if r.status_code==200:
            urlsList.append(i)
            print(i)
        
        
# USE MULTI-THREADING FOR THIS 
