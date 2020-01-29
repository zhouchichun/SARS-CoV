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
    url = "https://3g.dxy.cn/newh5/view/pneumonia_peopleapp"
    # 开始请求
    browser.get(url)
    # 获取页面内容
    time.sleep(25)
    html = BeautifulSoup(browser.page_source, 'html.parser')
    # 选择有效数据
    content_lst = html.find_all('p', class_='subBlock1___j0DGa')
    print(len(content_lst))
    with open("city_name","w",encoding="utf-8")as f, open("pro_name","w",encoding="utf-8")as ff:
        
        for content in content_lst:
            
            try:
                pro_name=content.find_all("img",class_="close___2yTiY")[0].text
            
                if pro_name not in [""," ","   "]:
                    ff.write("%s\n"%pro_name)
            except:
                continue
            
            name=content.text
            print(name)
            f.write("%s\n"%(name))
    # 关闭浏览器
    browser.close()
    # 关闭chreomedriver进程
    browser.quit()
