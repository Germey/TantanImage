# coding=utf-8
import os
import random
import requests

PATH = 'images/'


def get_random_location():
    jl = 108
    jr = 120
    wb = 23
    wt = 40
    w = random.randint(wb, wt)
    j = random.randint(jl, jr)
    w = w + round(random.random(), 6)
    j = j + round(random.random(), 6)
    return str(w) + ',' + str(j)


def get_images_urls(location):
    urls = []
    headers = {
        'User-Agent': 'Putong/2.1.3 Android/17 samsung/GT-P5210',
        'Accept-Language': 'zh-CN',
        'Geolocation': 'geo:' + location + ';u=246',
        'Authorization': 'cd8e5607bed783a78d5345ad505fe2f47359fa84787daf17c337b9305fde87b1',
        'Host': 'core.tantanapp.com'
    }

    url = 'https://core.tantanapp.com/v1/users?with=questions,contacts&search=suggested&limit=100'

    response = requests.get(url, headers=headers)
    print u'正在获取列头像列表'
    result = response.json()
    users = result['data']['users']
    for user in users:
        pictures = user['pictures']
        for picture in pictures:
            urls.append(picture['url'])
    return urls


def save_file(path, name, data):
    print u'正在保存图片', name
    file = open(path + name, 'wb')
    file.write(data)
    file.close()
    print u'成功保存图片', name


def get_image(url):
    try:
        print u'正在获取一张新头像, 请稍后...'
        response = requests.get(url)
        return response.content
    except Exception:
        print u'获取头像失败'
        return False


def get_file_name():
    count = len(os.listdir(PATH))
    return str(count + 1) + '.jpeg'


def parse_list(urls):
    for url in urls:
        data = get_image(url)
        if data:
            save_file(PATH, get_file_name(), data)


location = get_random_location()
urls = get_images_urls(location)
parse_list(urls)
