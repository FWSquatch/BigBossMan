#!/usr/bin/env python3

import requests, json, csv, random

#uname = 'fwsquatch'
#pw = 'oyeah1234!'

#template = ''

def list_memes():
    meme_list = []
    f = open('memes.csv','r')
    reader = csv.reader(f)
    csvdata = list(reader)
    for element in csvdata:
        meme_list.append(element[2])
    return meme_list

def random_temp():
    f = open('memes.csv','r')
    reader = csv.reader(f)
    csvdata = list(reader)
    meme = random.choice(csvdata)
    #print(meme[2])
    return(meme)

def make_meme(uname, pw, meme_template,text0, text1):
    url = 'https://api.imgflip.com/caption_image?username=' + uname + '&password=' + pw
    url = url + '&template_id=' + meme_template + '&text0=' + text0 + '&text1=' + text1
    r = requests.post(url)
    jdata = json.loads(r.text)

    return jdata["data"]["url"]