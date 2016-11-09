import subprocess

inputx = input(" who's turn? :")
whence = subprocess.check_output("ps -ef|grep {0}|grep -v 'grep'|awk {1}".format(inputx,"'{print $2}'"),shell=True)

while whence != b'':   #shell返回的结果不为空
    lista = list()
    for x in str(whence,encoding = "utf-8").split('\n'):
        if x:
            lista.append(int(x))
    lista.sort()
    #subprocess.call('kill '+str(lista[0]),shell=True)
    subprocess.call('kill -9 '+str(lista[0]),shell=True)
    #subprocess.call('kill -TERM '+str(lista[0]),shell=True)
    break
else:
    print('进程已结束或没有该进程')
