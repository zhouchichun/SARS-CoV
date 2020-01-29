from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
if __name__ == '__main__':

    #chrome_options = Options()
    # 设置chrome浏览器无界面模式
    #chrome_options.add_argument(
        #'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36')
    # 加载设置
    #browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()
    url = "https://3g.dxy.cn/newh5/view/pneumonia_timeline?whichFrom=peopleapp"
    # 开始请求
    browser.get(url)
    # 获取页面内容
    time.sleep(25)
    html = BeautifulSoup(browser.page_source, 'html.parser')
    # 选择有效数据
    content_lst = html.find_all('div', class_='block___wqUAz')
    print(len(content_lst))
    with open("data_raw"+"_"+now,"w",encoding="utf-8")as f:
        
        for content in content_lst:
            
            date_lst=content.find_all("span")
            date="++".join([x.text for x in date_lst])
            title=content.find_all("p",class_="topicTitle___2ovVO")[0].text
            te=content.find_all("p",class_="topicContent___1KVfy")[0].text
            whe=content.find_all("p",class_="topicFrom___3xlna")[0].text
            print(date,title)
            f.write("%s\t%s\t%s\t%s\n"%(date,title,te,whe))
            
    # 关闭浏览器
    browser.close()
    # 关闭chreomedriver进程
    browser.quit()
