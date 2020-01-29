import pickle
pro_file="pro_name"
city_file="city_name_all"
t_pro2city={}
for line in open(pro_file,"r",encoding="utf-8"):
    name=line.strip()
    t_pro2city[name]=[]

tmp=[]
for line in open(city_file,"r",encoding="utf-8"):
    name=line.strip()
    if name not in t_pro2city:
        try:
            t_pro2city[this_key].append(name)
        except:
            print(name)
            exit()
    else:
        this_key=name
        
        #tmp=[]
print(t_pro2city)

with open("pro2city","wb")as f:
    pickle.dump(t_pro2city,f)