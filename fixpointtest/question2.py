f = open("question2.csv","r")

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

def question2():
    file = open("answer2.txt","w")
    n = input('何回連続timeoutした場合？N>>')
    n = int(n)
    flug = 0
    flug2 = 0
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
           # print(server1)
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

    for i in range(len(server1[parameters[0]])):
        if flug == 0 and server1[parameters[2]][i] == '-':
            flug = 1
            flug2 += 1
            list1.append(server1[parameters[0]][i])
        elif flug == 1 and server1[parameters[2]][i] == '-':
            list1.append(server1[parameters[0]][i])
            flug2 += 1
        elif flug == 1 and flug2 < n and server1[parameters[2]][i] != '-':
            flug = 0
            flug2 = 0
        elif flug == 1 and flug2 > n and server1[parameters[2]][i] != '-':
            list1.append(server1[parameters[0]][i])
            print("故障サーバアドレス:",server1[parameters[1]][i])
            print("故障期間:",list1[0],"～",list1[-1])
            file.write("故障サーバアドレス:"+str(server1[parameters[1]][i]))
            file.write("故障期間:"+str(list1[0])+"～"+str(list1[-1])+"\n")
            flug = 0
            flug2 = 0

    if flug == 0 and flug2 == 0:
        print("サーバアドレス:",server1[parameters[1]][i])
        print("故障なし")
        file.write("サーバアドレス:"+ str(server1[parameters[1]][i]))
        file.write("故障なし"+"\n")
    if flug != 0 and flug2 != 0:
        print("故障サーバアドレス:",server1[parameters[1]][i])
        print("故障中:",list1[0],"～",list1[-1])
        file.write("故障サーバアドレス:"+ str(server1[parameters[1]][i]))
        file.write("故障中:"+str(list1[0])+"～"+str(list1[-1])+"\n")
        flug = 0
        flug2 = 0

    for i in range(len(server2[parameters[0]])):
        if flug == 0 and server2[parameters[2]][i] == '-':
            flug = 1
            flug2 += 1
            list2.append(server2[parameters[0]][i])
        elif flug == 1 and server2[parameters[2]][i] == '-':
            list2.append(server2[parameters[0]][i])
            flug2 += 1
        elif flug == 1 and flug2 < n and server2[parameters[2]][i] != '-':
            flug = 0
            flug2 = 0
        elif flug == 1 and flug2 > n and server2[parameters[2]][i] != '-':
            list2.append(server2[parameters[0]][i])
            print("故障サーバアドレス:",server2[parameters[1]][i])
            print("故障期間:",list2[0],"～",list2[-1])
            file.write("故障サーバアドレス:"+str(server2[parameters[1]][i]))
            file.write("故障期間:"+str(list2[0])+"～"+str(list2[-1])+"\n")
            flug = 0
            flug2 = 0

    if flug == 0 and flug2 == 0:
        print("サーバアドレス:",server2[parameters[1]][i])
        print("故障なし")
        file.write("サーバアドレス:"+ str(server2[parameters[1]][i]))
        file.write("故障なし"+"\n")
    if flug != 0 and flug2 != 0:
        print("故障サーバアドレス:",server2[parameters[1]][i])
        print("故障中:",list2[0],"～",list2[-1])
        file.write("故障サーバアドレス:"+ str(server2[parameters[1]][i]))
        file.write("故障中:"+str(list2[0])+"～"+str(list2[-1])+"\n")
        flug = 0
        flug2 = 0

    for i in range(len(server3[parameters[0]])):
        if flug == 0 and server3[parameters[2]][i] == '-':
            flug = 1
            flug2 += 1
            list3.append(server3[parameters[0]][i])
        elif flug == 1 and server3[parameters[2]][i] == '-':
            list3.append(server3[parameters[0]][i])
            flug2 += 1
        elif flug == 1 and flug2 < n and server3[parameters[2]][i] != '-':
            flug = 0
            flug2 = 0
        elif flug == 1 and flug2 > n and server3[parameters[2]][i] != '-':
            list3.append(server3[parameters[0]][i])
            print("故障サーバアドレス:",server3[parameters[1]][i])
            print("故障期間:",list3[0],"～",list3[-1])
            file.write("故障サーバアドレス:"+str(server3[parameters[1]][i]))
            file.write("故障期間:"+str(list3[0])+"～"+str(list3[-1])+"\n")
            flug = 0
            flug2 = 0

    if flug == 0 and flug2 == 0:
        print("サーバアドレス:",server3[parameters[1]][i])
        print("故障なし")
        file.write("サーバアドレス:"+ str(server3[parameters[1]][i]))
        file.write("故障なし"+"\n")
    if flug != 0 and flug2 != 0:
        print("故障サーバアドレス:",server3[parameters[1]][i])
        print("故障中:",list3[0],"～",list3[-1])
        file.write("故障サーバアドレス:"+ str(server3[parameters[1]][i]))
        file.write("故障中:"+str(list3[0])+"～"+str(list3[-1])+"\n")
        flug = 0
        flug2 = 0


    for i in range(len(server4[parameters[0]])):
        if flug == 0 and server4[parameters[2]][i] == '-':
            flug = 1
            flug2 += 1
            list4.append(server4[parameters[0]][i])
        elif flug == 1 and server4[parameters[2]][i] == '-':
            list4.append(server4[parameters[0]][i])
            flug2 += 1
        elif flug == 1 and flug2 < n and server4[parameters[2]][i] != '-':
            flug = 0
            flug2 = 0
        elif flug == 1 and flug2 > n and server4[parameters[2]][i] != '-':
            list4.append(server4[parameters[0]][i])
            print("故障サーバアドレス:",server4[parameters[1]][i])
            print("故障期間:",list4[0],"～",list4[-1])
            file.write("故障サーバアドレス:"+str(server4[parameters[1]][i]))
            file.write("故障期間:"+str(list4[0])+"～"+str(list4[-1])+"\n")
            flug = 0
            flug2 = 0

    if flug == 0 and flug2 == 0:
        print("サーバアドレス:",server4[parameters[1]][i])
        print("故障なし")
        file.write("サーバアドレス:"+ str(server4[parameters[1]][i]))
        file.write("故障なし"+"\n")
    if flug != 0 and flug2 != 0:
        print("故障サーバアドレス:",server4[parameters[1]][i])
        print("故障中:",list4[0],"～",list4[-1])
        file.write("故障サーバアドレス:"+ str(server4[parameters[1]][i]))
        file.write("故障中:"+str(list4[0])+"～"+str(list4[-1])+"\n")
        flug = 0
        flug2 = 0


question2()
