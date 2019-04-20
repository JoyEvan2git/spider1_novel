# -*- coding:utf-8 -*-
import requests
import re
url = "http://www.quanshuwang.com/book/9/9055"

response = requests.get(url)
response.encoding = 'GBK'
#目标小说源码
html = response.text
#print(html)
#获取每一章的信息（章节，url）
#re,findall返回一个数组  把数组的索引为0的赋给dl
title = re.findall(r'<title>(.*?)</title>',html,re.S)[0]
dl = re.findall(r'<DIV class="clearfix dirconone">.*?</DIV>',html,re.S)[0]
chapter_info_list = re.findall(r'<li><a href="(.*?)" title="(.*?)">(.*?)</a></li>',dl,re.S)
fb = open('%s.txt' % title,'w',encoding='utf-8')

for chapter_info in chapter_info_list:
    #chapter_title = chapter_info[1]
    #chapter_url = chapter_info[0]
    #print(chapter_info)
    chapter_url, chapter_title1,chapter_title2 = chapter_info
    #print(chapter_url, chapter_title1,chapter_title2)
    #下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'GBK'
    chapter_html = chapter_response.text
    chapter_content = re.findall(r'<div class="mainContenr"   id="content">(.*?)</div>',chapter_html,re.S)[0]

    chapter_content = chapter_content.replace('<script type="text/javascript">style5();</script>','')
    chapter_content = chapter_content.replace('&nbsp;', '')
    chapter_content = chapter_content.replace('<br />', '')
    chapter_content = chapter_content.replace('<script type="text/javascript">style6();</script>', '')

    fb.write(chapter_title1)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)




