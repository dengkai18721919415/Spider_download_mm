import urllib.request
import os
import random

#this founction used to offer a unified http header and proxy finally return html

def url_open(url):
    req = urllib.request.Request(url):
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36')
    
    proxies = ['118.114.77.47:8080','61.135.217.7:80','110.73.40.2:8123']
    proxy = random.choice(proxies)
    
    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_supprot)
    
    response = urllib.request.urlopen(url)
    html = response.read()
    
    return html
    
    #this founction is used to get the newest page of the specific url 
def get_page(url):
    html = url_open(url).decode('utf-8')
        
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
        
    return html[a:b]
        
#this founction is used to find all the pictures those are ending with the suffix of .jpg
def find_imge(url):
    html = url_open(url).decode('utf-8)
    img_address =[]

    a = html.find('img src=')

    #if have no jpg the web server will return -1
    while a!= -1:
        b = html.find('.jpg,a,a+255)
        if b != -1:
            img_address.append(html[a+9:b+4])
        else:
            b = a+9
        a = html.find('img src=',b)
     return img_address

#this founction is used to save the found pictures
def save_imgs(folder,img_address):
    for each in img_address:
        filename = each.splite('/')[-1]
        with open (filename,'wb') as f:
            img = url_open(each)
            f.write(img)
 
#this is the main founction
def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))
    
    for i in range(pages):
        page_num -= i
        page_url = url + 'page' + str(page_num) + '#comments'
        img_address = find_image(page_url)
        save_imgs(folder,img_address)
        
 if __name__ == '__main__'
    download_mm()
            
    
