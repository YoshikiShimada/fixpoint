f = open("question3.csv","r")

sample_dic = {}
parameters = ['date','IPv4','ping']

for parameter in parameters:
    sample_dic[parameter] = []


    #1行ずつ取り出す
line = f.readline()
    #1行ごとに要素を入れていく
while line:
        #","ごとに分割
    words = line[:-1].split(',')
        #リストに全ての要素を入れる
    for i in range(len(parameters)):
        sample_dic[parameters[i]].append(words[i])
            
        
    line = f.readline()

f.close()

def question3():
    file = open("answer3.txt","w")
    m = input('直近何回の応答m>>')
    t = input('何ミリ秒超えたらt>>')
    sum = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    result = 0
    server1 = {}
    server2 = {}
    server3 = {}
    server4 = {}
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for parameter in parameters:
        server1[parameter] = []
        server2[parameter] = []
        server3[parameter] = []
        server4[parameter] = []
        #サーバごとにparameterリストを作成
    for i in range(len(sample_dic["date"])):
        if sample_dic[parameters[1]][i] =="10.20.30.1/16":
            server1[parameters[0]].append(sample_dic[parameters[0]][i])
            server1[parameters[1]].append(sample_dic[parameters[1]][i])
            server1[parameters[2]].append(sample_dic[parameters[2]][i])
            
        elif sample_dic[parameters[1]][i] == "10.20.30.2/16":
            server2[parameters[0]].append(sample_dic[parameters[0]][i])
            server2[parameters[1]].append(sample_dic[parameters[1]][i])
            server2[parameters[2]].append(sample_dic[parameters[2]][i])
           
        elif sample_dic[parameters[1]][i] != "192.168.1.1/24":
            server3[parameters[0]].append(sample_dic[parameters[0]][i])
            server3[parameters[1]].append(sample_dic[parameters[1]][i])
            server3[parameters[2]].append(sample_dic[parameters[2]][i])
            
        elif sample_dic[parameters[1]][i] != "192.168.1.2/24":
            server4[parameters[0]].append(sample_dic[parameters[0]][i])
            server4[parameters[1]].append(sample_dic[parameters[1]][i])
            server4[parameters[2]].append(sample_dic[parameters[2]][i])
            
    #サーバごとに直近m回の平均応答が過負荷状態か確認
    if len(server1[parameters[2]]) >= int(m):
        for j in range(int(m),0,-1):
             if server1[parameters[2]][-j] != '-':
                 sum += int(server1[parameters[2]][-j])
             
        result = sum/int(m)
        if result > int(t):
            print("過負荷サーバアドレス:10.20.30.1/16")
            file.write("過負荷サーバアドレス:10.20.30.1/16\n")
            for k in range(int(m),0,-1):
                list1.append(server1[parameters[0]][k-1])
        
            print("直近過負荷期間",list1[-1],"～",list1[-int(m)])
            file.write("直近過負荷期間:"+str(list1[-1])+"～"+str(list1[-int(m)])+"\n")
        else:
            print("サーバアドレス:10.20.30.1/16:直近過負荷なし")
            file.write("サーバアドレス:10.20.30.1/16:直近過負荷なし\n")
    else:
         print("サーバアドレス:10.20.30.1/16:直近過負荷なし")    
         file.write("サーバアドレス:10.20.30.1/16:直近過負荷なし\n")

    if len(server2[parameters[2]]) >= int(m):
        for j in range(int(m),0,-1):
             if server2[parameters[2]][-j] != '-':
                 sum2 += int(server2[parameters[2]][-j]) 
        result2 = sum2/int(m)
        if result2 > int(t):    
            print( "過負荷サーバアドレス:10.20.30.2/16")
            file.write("過負荷サーバアドレス:10.20.30.2/16\n")
            for k in range(int(m),0,-1):
                list2.append(server2[parameters[0]][k-1])

            print("直近過負荷期間",list2[-1],"～",list2[-int(m)])
            file.write("直近過負荷期間"+str(list2[-1])+"～"+str(list2[-int(m)])+"\n")
        else:
            print("サーバアドレス:10.20.30.2/16:直近過負荷なし")
            file.write("サーバアドレス:10.20.30.2/16:直近過負荷なし\n")
    else:
         print("サーバアドレス:10.20.30.2/16:直近過負荷なし") 
         file.write("サーバアドレス:10.20.30.2/16:直近過負荷なし\n")

    if len(server3[parameters[2]]) >= int(m):
        for j in range(int(m),0,-1):
            if server3[parameters[2]][-j] != '-':
                sum3 += int(server3[parameters[2]][-j])
        result3 = sum3/int(m)    
        if result3 > int(t):   
            print("過負荷サーバアドレス:192.168.1.1/24")
            file.write("過負荷サーバアドレス:192.168.1.1/24\n")
            for k in range(int(m),0,-1):                
                list3.append(server3[parameters[0]][k-1])
                          
            print("直近過負荷期間",list3[-1],"～",list3[-int(m)])
           
            file.write("直近過負荷期間"+str(list3[-1])+"～"+str(list3[-int(m)])+"\n")
        else:
            print("サーバアドレス:192.168.1.1/24:直近過負荷なし")
            file.write("サーバアドレス:192.168.1.1/24:直近過負荷なし\n")
    else:
         print("サーバアドレス:192.168.1.1/24:直近過負荷なし") 
         file.write("サーバアドレス:192.168.1.1/24:直近過負荷なし\n")

    if len(server4[parameters[2]]) >= int(m):
        for j in range(int(m),0,-1):
            if server4[parameters[2]][-j] != '-':
                sum4 += int(server4[parameters[2]][-j])
        result4 = sum4/int(m)
        if result4 > int(t): 
            print("過負荷サーバアドレス:192.168.1.2/24")
            file.write("過負荷サーバアドレス:192.168.1.2/24\n")
            for k in range(int(m),0,-1):
                list4.append(server4[parameters[0]][k-1])

            print("直近過負荷期間",list4[-1],"～",list4[-int(m)])
            file.write("直近過負荷期間"+str(list4[-1])+"～"+str(list4[-int(m)])+"\n")
        else:
            print("サーバアドレス:192.168.1.2/24:直近過負荷なし")
            file.write("サーバアドレス:192.168.1.2/24:直近過負荷なし\n")
    else:
         print("サーバアドレス:192.168.1.2/24:直近過負荷なし") 
         file.write("サーバアドレス:192.168.1.2/24:直近過負荷なし\n")

question3()
