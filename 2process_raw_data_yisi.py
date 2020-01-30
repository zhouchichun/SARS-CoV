import re
import time
now=time.strftime('%Y-%m-%d',time.localtime(time.time()))

file_name="data_raw_"+now



def get_time(time):
    if time.find("前")!=-1:
        ret=time.split("前")[-1].split(" ")[0]
        return ret
    elif time.find("日")!=-1:
        tmp=time.replace(" ","")
        tmp=time.split("日")[0]
        tmp_lst=tmp.split("月")
        ret="-".join(tmp_lst)
        ret=ret.replace(" ","")
        return ret
    else:
        return "0-0"
def get_sit(title):
    title=title.replace("确诊病例","")
    title=title.replace("确诊","")
    content_lst=title.split("新增")
    city,num=content_lst[:2]
    city=city.replace("省","")
    city=city.replace("市","")
    
    num=num.split("例")[0]
    num=num.replace("一",'1')
    num=num.replace("两",'2')
    num=num.replace("三",'3') 
    num=num.replace("四",'4')
    num=num.replace("五",'5')
    num=num.replace("六",'6')
    num=num.replace("七",'7')
    num=num.replace("八",'8')
    num=num.replace("九",'9')
    
    try:
        num=re.findall(r'\d+', num)[0]
    except Exception as e:
        print(e)
        print(title)
        print("wrong quite")
        exit()
    return city,num
with open(file_name+"_rd","w",encoding="utf-8")as f,open("wash_left_from_raw","w",encoding="utf-8")as ff:
    for line in open(file_name,"r",encoding="utf-8"):
        contents=line.strip().split("\t")
        try:
            time,title=contents[:2]
        except:
            print("分隔数量不对",contents)
            ff.write("%s\t%s\n"%("分隔数量不对",line.strip()))
            continue
        time=get_time(time)
        if title.find("新增")!=-1:
            city,num=get_sit(title)
            f.write("%s\t%s\t%s\n"%(time,city,num))
        else:
            try:
                print("不含新增",title)
                ff.write("%s\t%s\n"%("不含新增",title))
            except:
                print("===================================")
                print(line)
                
                continue
                #exit()
