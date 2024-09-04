import requests
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# pip install lxml
# pip install beautifulsoup4
# 关注---亮灯牌--进群
# url就是每一章的连接地址
# down_txts 就是下载每一章的内容！！
def down_txts(url):
    # 获取到html
    html=requests.get(url,headers=headers).text
    # soup：可以理解成一个筛子，它可以从html里面筛选出我们想要的内容
    soup = BeautifulSoup(html, 'lxml')
    # 找到class=wap_none的h1
    # class为什么要加下划线，因为这是find里面语法要求！
    title_obj=soup.find("h1",class_="wap_none")
    # 找到id=chaptercontent的div
    con_obj=soup.find("div",id="chaptercontent")
    # 两个不为空
    if title_obj and con_obj:
        #  获取到标题
        title=title_obj.get_text()
        # 获取到内容
        con=con_obj.get_text()
        # 将内容存到.txt文件里面

        # "w"----> write
        with open(f"E:/temp/斗罗大陆V重生唐三/{title}.txt","w") as f:
            f.write(con)

        print(f"{title}    下载完成。。。")

if __name__ == '__main__':

    starttime=datetime.now()
    
    # https://www.bqgai.cc/book/159995/
    url="https://www.bqgai.cc/book/3315/"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    # 获取到网页的html
    # 爬虫的原理是通过python去模拟浏览器的请求
    # 为什么要加headers？因为里面有浏览器的信息
    html=requests.get(url,headers=headers).text
    # soup：可以理解成一个筛子，它可以从html里面筛选出我们想要的内容
    soup=BeautifulSoup(html,'lxml')
    # 吧每一章的连接地址放到urls里面
    urls=[]
    # 获取class="listmain"的div下的所有的超链接
    items=soup.find("div",class_="listmain").find_all("a")
    for item in items:
        # 获取到每一章的连接地址
        url=item["href"]
        if url!="javascript:dd_show()":
            # 获取到完整的连接地址
            url="https://www.bqgai.cc"+url
            urls.append(url)

    # for url  in urls:
    #     down_txts(url)

    with ThreadPoolExecutor(max_workers=2) as exe:
        for url in urls:
            exe.submit(down_txts,url)


    endtime=datetime.now()
    print(f"总共花了{(endtime-starttime).seconds}秒！")


