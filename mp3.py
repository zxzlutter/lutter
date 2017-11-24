#! /usr/bin/env python
#coding:utf-8
import re, os, time,requests
import urllib
#取得网页的html纯文本
def getHtml(url):
     return urllib.urlopen(url).read().decode('utf-8')
if __name__ == '__main__':

    print('---豆瓣音乐抓取---')
    dic = {1:'古典', 2:'轻音乐', 3:'电子', 4:'民谣',5:'爵士',6:'流行', 7:'说唱', 8:'摇滚', 9:'原声' ,10:'世界音乐'}
    for i in dic.keys():
        print('{:<15}'.format(str(i) + '--' + dic[i]))
    category = int(input('\n请输入抓取类别:'))
    pageNo1 = int(input('请输入抓取页面起始编号(1-374):'))#2017.11.23正好374页，以流行音乐为例
    pageNo2 = int(input('请输入抓取页面终止编号(1-374):'))
    for no in range(pageNo1, pageNo2+1):

        url = 'https://music.douban.com/artists/genre_page/{}/{}'.format(category,no)
        html = getHtml(url)
        reMeizi = r'https://site.douban.com/.*?/'
        pics = re.findall(reMeizi, html)
        print pics
        folder = 'D:/DBMeizi/{}/{}/'.format(dic[category], no)
        if not os.path.exists(folder):
            os.makedirs(folder)
        logfile = open(folder+'log.txt', 'wt')
        logfile.write('图片来源：'+ url +'\n图片链接：\n')
        musicname=0
        for pic in pics:
            try:
                musicpage=getHtml(pic)
                print pic
                remusic=r'http:\\/\\/mr3.doubanio.com.*?\.mp3'
                musicurls=re.findall(remusic,musicpage)

                for musicurl in musicurls:
                    print musicurl
                    remusicurl=musicurl.replace('\\','')
                    print remusicurl
                    urllib.urlretrieve(remusicurl,'%s\%s.mp3' %(folder,musicname))
                    musicname+=1
            except:
                print('error')
                logfile.write(pic +'\n')
                continue
            logfile.write(pic+'\n')
        logfile.close()
        print('下载' + dic[category] +'['+ str(no) +']结束。')
        time.sleep(1)
        print('全部任务结束。')
