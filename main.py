import pickle
import matplotlib.pyplot as plt
import time
now=time.strftime('%Y-%m-%d',time.localtime(time.time()))

raw_file="data_raw_%s_rd"%now
pro2num="pro2num"
pickle_file="pro2city"
t_pro2citys={}
with open(pickle_file,"rb")as f:
    t_pro2city=pickle.load(f)
    
    
city_file="city_name_all"
t_city2seq={}
for line in open(raw_file,"r",encoding="utf-8"):
    time,name,num=line.strip().split("\t")
    if name not in t_city2seq:
        t_city2seq[name]=[[int(time.replace("-","")),int(num)]]
    else:
        t_city2seq[name].append([int(time.replace("-","")),int(num)])

t_pro2num={}
for line in open("pro2num","r",encoding="utf-8"):
    name,num=line.strip().split(" ")
    num=int(float(num))
    t_pro2num[name]=num


t_new={}
for city,seq in t_city2seq.items():
    print(city)
    if city not in t_pro2num: continue
    num=t_pro2num[city]
    seq.sort()
    
    date=[x[0] for x in seq]
    new_seq=[]
    for se in seq:
        if len(new_seq)==0:
            new_seq.append(se)
        elif se[0]==new_seq[-1][0]:
            new_seq[-1][1]+=se[1]
        else:
            new_seq.append(se)
   
    new_new_seq=[]
    av_all=[]
    av_wuhan=[]
    av_no_wuhan=[]
    date_range=[i for i in range(117,131)]  # 需要手动配置
    for i in date_range:
        #tmp=[i,0]
        av_all.append([i,0])
        av_wuhan.append([i,0])
        av_no_wuhan.append([i,0])
        if i not in date:
            new_new_seq.append([i,0])
        else:
            for se in new_seq:
                if se[0]==i:
                    se[1]=float(se[1])/num
                    new_new_seq.append(se)
    t_new[city]=new_new_seq

num_city=len(t_new)
for city,sq in t_new.items():
    print(city)
    if city=="湖北":
        for ii, ss in enumerate(sq):
            av_wuhan[ii][1] +=ss[1]
    else:
        for ii, ss in enumerate(sq):
            av_no_wuhan[ii][1] +=ss[1]/(num_city-1)
    print(sq)
    for ii, ss in enumerate(sq):
        av_all[ii][1] +=ss[1]/num_city

print(av_all)
print(av_wuhan)
print(av_no_wuhan)
rate_all=[x[1]for x in av_all]
rate_wuhan=[x[1]for x in av_wuhan]
rate_no_wuhan=[x[1]for x in av_no_wuhan]

#plt.plot(acc)
x=[i for i in range(14)]  #需要手动配置
all=plt.scatter(x,rate_all,c="b",marker='*')
wuhan=plt.scatter(x,rate_wuhan,c="y",marker='o')
no_wuhan=plt.scatter(x,rate_no_wuhan,c="r",marker=',')
plt.ylabel('days',fontsize=14)
plt.legend(handles = [all,wuhan,no_wuhan], labels = ['all',"Hubei only",'without Hubei'], loc = 'best')
plt.legend
plt.title("The ave infection rate per 10,000 people. 1-17 1-30")
plt.ylabel('Infected population per 10000 people',fontsize=14)

plt.savefig("all_%s.png"%now)

plt.show()

all=plt.scatter(x,rate_all,c="b",marker='*')
#wuhan=plt.scatter([0,1,2,3,4,5,6,7,8,9,10],rate_wuhan,c="y",marker='o')
no_wuhan=plt.scatter(x,rate_no_wuhan,c="r",marker=',')
plt.ylabel('days',fontsize=14)
plt.legend(handles = [all,no_wuhan], labels = ['all','without Hubei'], loc = 'best')
plt.legend
plt.title("The ave infection rate per 10,000 people. 1-17 1-30")
plt.ylabel('Infected population per 10000 people',fontsize=14)

plt.savefig("no_hubei%s.png"%now)

plt.show()