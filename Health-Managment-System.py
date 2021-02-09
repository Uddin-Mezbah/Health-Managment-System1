client_list = {1:'gqextra', 2:'max', 3:'harry'}
log_list = {1:'Exercise', 2:'diet'}



def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select the Client Name")
    for key,value in client_list.item():
        print("Press",key,"for",value,"\n",end='')
    client_name = int(input())
    print("Selected Client : ",client_list[client_name])

    print("Press 1 for Log")
    print("Press 2 for Retrive")
    op = int(input)

    if op == 1:
        for key,Value in log_list.items():
            print("Select",key,"for",Value,"\n",end='')
        log_name = int(input())
        print("Selected Job is :", log_list[log_name])
        f = open(client_list[client_name] + "-" + log_list[log_name] + ".txt","a")
        k='y'
        while k != 'n':
            print("Enter",log_list[log_name])
            mytext = input()
            f.write("["+ str(getdate()) + "]" + mytext + "")
            k = input("ADD MORE? y/n:")
            continue
        f.close()
    elif op == 2:
        for key,value in log_list.items():
            print("Select",key,"for",Value,"\n",end='')
        log_name = int(input())
        print("Slelected Job is :",log_list[log_name])
        print(client_list[client_name] +"-"+ log_list[log_name],"Report: \n", end='')
        f = open(client_list[client_name]+"-"+log_list[log_name] +".text",'r')
        contents = f.readlines()

        for data in content:
            print(data,end='')
        f.close()
    else:
        print("Invalid input")
except Exception as e:
    print("wrong input")
