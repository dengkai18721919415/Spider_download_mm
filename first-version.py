import urllib.request
import random
import shutil
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    
    #proxies = ['115.150.229.171:9000','180.118.86.197:9000','117.135.164.170:8080','27.159.124.78:8118','111.155.116.195:8123','110.73.5.63:8123']
    #proxies = ['210.38.1.144:8080','111.13.7.118','112.216.16.250:3128']
    #proxies = ['101.230.198.106:80']
    #proxy = random.choice(proxies)
    #print(proxy)
    
    #proxy_support = urllib.request.ProxyHandler({'http':proxy})
    #opener = urllib.request.build_opener(proxy_support)
    #urllib.request.install_opener(opener)
    
    response = urllib.request.urlopen(url)
    html = response.read()
    
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    
    a = html.find('img src=')
    
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=',b)
    #for each in img_addrs:
        #print(each)
    return img_addrs


def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            
def download_mm(folder='mm',pages=20):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    else:   
        os.mkdir(folder)
        os.chdir(folder)
    
        url = 'http://jandan.net/ooxx/'
        page_num = int(get_page(url))
        print(page_num)
        for i in range(pages):
            page_num -= 1
            page_url = url + 'page-' + str(page_num) + '#comments'
            print(page_url)
            img_addrs = map(lambda x: 'http:'+x,find_imgs(page_url))
            #print(type(img_addrs))
            save_imgs(folder, img_addrs)
        

if __name__ == '__main__':
    download_mm()
