f = open("question4.csv","r")

sample_dic = {}
parameters = ['date','IPv4','ping']
N = input('何回連続timeoutした場合？(サブネット)N>>')
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

def question4():
    file = open("answer4.txt","w")
    subnet1 = {}
    subnet2 = {}
    list1 = []
    list2 = []
    timeout = 0
    for parameter in parameters:
        subnet1[parameter] = []
        subnet2[parameter] = []
      
        #サブネットごとにparameterリストを作成
    for i in range(len(sample_dic["date"])):
        if sample_dic[parameters[1]][i] =="10.20.30.1/16":
            subnet1[parameters[0]].append(sample_dic[parameters[0]][i])
            subnet1[parameters[1]].append(sample_dic[parameters[1]][i])
            subnet1[parameters[2]].append(sample_dic[parameters[2]][i])
        elif sample_dic[parameters[1]][i] == "10.20.30.2/16":
            subnet1[parameters[0]].append(sample_dic[parameters[0]][i])
            subnet1[parameters[1]].append(sample_dic[parameters[1]][i])
            subnet1[parameters[2]].append(sample_dic[parameters[2]][i])
       
        elif sample_dic[parameters[1]][i] != "192.168.1.1/24":
            subnet2[parameters[0]].append(sample_dic[parameters[0]][i])
            subnet2[parameters[1]].append(sample_dic[parameters[1]][i])
            subnet2[parameters[2]].append(sample_dic[parameters[2]][i])
            
        elif sample_dic[parameters[1]][i] != "192.168.1.2/24":
            subnet2[parameters[0]].append(sample_dic[parameters[0]][i])
            subnet2[parameters[1]].append(sample_dic[parameters[1]][i])
            subnet2[parameters[2]].append(sample_dic[parameters[2]][i])
   
    #サブネット内のサーバのpingがN回以上"-"だった場合故障とみなす
    if len(subnet1[parameters[2]]) >= int(N):
        for j in range(len(subnet1[parameters[2]])):
             if subnet1[parameters[2]][j] == '-':
                 timeout += 1
                 list1.append(subnet1[parameters[0]][j])
             #pingがN回以上タイムアウトかつ"-"から回復した場合
             elif subnet1[parameters[2]][j] != '-':
                 if timeout >= int(N):
                     list1.append(subnet1[parameters[0]][j])
                     print("故障サブネット10.20")
                     print("故障開始",list1[0],"故障終了",list1[-1],"故障時間",format(int(list1[-1])-int(list1[0]),"014"))
                     print("サブネット10.20:",list1[-1],"故障回復")

                     file.write("故障サブネット10.20\n")
                     file.write("故障開始:"+str(list1[0])+"\t"+"故障終了:"+str(list1[-1])+"\t"+"故障時間"+str(format(int(list1[-1])-int(list1[0]),"014"))+"\n")
                     file.write("サブネット10.20:"+str(list1[-1])+"故障回復\n")

                     timeout = 0
                     
        #pingがN回以上タイムアウトかつ回復していない場合
        if timeout >= int(N):
           print("故障サブネット10.20")
           print("故障開始",list1[0],"故障中",list1[-1],"故障時間",format(int(list1[-1])-int(list1[0]),"014"))
           file.write("故障サブネット10.20\n")
           file.write("故障開始:"+str(list1[0])+"\t"+"故障中:"+str(list1[-1])+"\t"+"故障時間:"+str(format(int(list1[-1])-int(list1[0]),"014"))+"\n")
        else:
            
            print("サブネット10.20:",list1[-1],"故障無し")
            file.write("サブネット10.20:"+str(list1[-1])+"故障無し\n")
        timeout = 0
    
    #サブネット内のサーバのpingがN回以上"-"だった場合故障とみなす
    if len(subnet2[parameters[2]]) >= int(N):
        for j in range(len(subnet2[parameters[2]])):
            if subnet2[parameters[2]][j] == '-':
                timeout += 1
                list2.append(subnet2[parameters[0]][j])
                
            #pingがN回以上タイムアウトかつ"-"から回復した場合
            elif subnet2[parameters[2]][j] != '-':
                if timeout >= int(N):
                    list2.append(subnet2[parameters[0]][j])
                    print("故障サブネット192.168.1")
                    print("故障開始",list2[0],"故障終了",list2[-1],"故障時間",format(int(list2[-1])-int(list2[0]),"014"))
                    print("サブネット192.168.1:",list2[-1],"故障回復")
                   
                    file.write("故障サブネット192.168.1\n")
                    file.write("故障開始:"+str(list2[0])+"\t"+"故障終了:"+str(list2[-1])+"\t"+"故障時間"+str(format(int(list2[-1])-int(list2[0]),"014"))+"\n")
                    file.write("サブネット192.168.1:"+str(list2[-1])+"故障回復\n")

                    timeout = 0
                    
        #pingがN回以上タイムアウトかつ回復していない場合        
        if timeout >= int(N):
            print("故障サブネット192.168.1")
            print("故障開始",list2[0],"故障中",list2[-1],"故障時間",format(int(list2[-1])-int(list2[0]),"014"))
            
            file.write("故障サブネット192.168.1\n")
            file.write("故障開始:"+str(list2[0])+"\t"+"故障中:"+str(list2[-1])+"\t"+"故障時間:"+str(format(int(list2[-1])-int(list2[0]),"014"))+"\n")
        else:
            
            print("サブネット192.168.1:",list2[-1],"故障無し")
            file.write("サブネット192.168.1:"+str(list2[-1])+"故障無し\n")
        timeout = 0

question4()