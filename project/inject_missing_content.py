import os
from bs4 import BeautifulSoup

file_path = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

sec1_2_2 = soup.find(id='sec1-2-2')
if sec1_2_2:
    # First, append the transition paragraph
    transition = soup.new_tag('p')
    transition['class'] = 'text-slate-700 font-bold mt-4 mb-3 border-l-4 border-brand-500 pl-3'
    transition.string = '该指南在工程建设中，重点涵盖以下资源的构建与接口对接：'
    sec1_2_2.append(transition)

    # Then append the container for the 2 items
    container = soup.new_tag('div')
    container['class'] = 'space-y-2 text-base'

    # Item 1: Data Resource Catalog (sec1-5)
    item1 = soup.new_tag('div')
    item1['class'] = 'mt-3 space-y-1'
    item1['id'] = 'sec1-5'
    
    title1 = soup.new_tag('strong')
    title1['class'] = 'text-slate-800 block mb-1 font-bold'
    title1.string = '1. 数据资源目录'
    item1.append(title1)
    
    p1 = soup.new_tag('p')
    p1['class'] = 'text-slate-600'
    p1.string = '编制完善《湖北省公路事业发展中心数据资源目录》，联动更新机制，在应用、数据变化时对数据资源目录进行更新，打造公路中心数据资源“一本帐”。'
    item1.append(p1)
    
    container.append(item1)

    # Item 2: Data Interface Construction (sec1-6)
    item2 = soup.new_tag('div')
    item2['class'] = 'mt-3 space-y-1'
    item2['id'] = 'sec1-6'

    title2 = soup.new_tag('strong')
    title2['class'] = 'text-slate-800 block mb-1 font-bold'
    title2.string = '2. 数据接口建设'
    item2.append(title2)

    p2 = soup.new_tag('p')
    p2['class'] = 'text-slate-600'
    p2.string = '本工程按需开发各类数据接口，主要建设内容如下：'
    item2.append(p2)

    ul = soup.new_tag('ul')
    ul['class'] = 'list-disc pl-5 text-slate-600 space-y-1 mt-1'
    
    items = [
        ('政府侧数据底座对接：', '按需开发相应接口，实现与政府侧数据底座数据的接入与共享；'),
        ('高速视频联网平台对接：', '按需开发相应接口，实现与高速视频联网平台视频数据的接入；'),
        ('省公路中心数转专项业务对接：', '按需开发相应接口，将公路中心各数转任务业务数据共享至政府侧底座；'),
        ('地市及非交投高速对接：', '按需开发相应接口，实现各地市州、非交投路段数转任务数据的接入与共享。')
    ]
    
    for bold_text, normal_text in items:
        li = soup.new_tag('li')
        strong = soup.new_tag('strong')
        strong.string = bold_text
        li.append(strong)
        li.append(normal_text)
        ul.append(li)
        
    item2.append(ul)
    container.append(item2)
    sec1_2_2.append(container)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Content successfully injected.")
else:
    print("Could not find sec1-2-2")
