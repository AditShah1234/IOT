import socket
import time
def start_socket(file_name="",ip="10.0.0.9",port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(file_name.encode(encoding='utf-8'))
    print(file_name)
    f = open(file_name, "rb")

    datas = f.read(1024)
    time.sleep(1)
    # print(datas)
    while datas:
        s.send(datas)
        datas = f.read(1024)

    f.close()
    s.close()
    # while True:
    #     datas = s.recv(1024)
    #     while datas:
    #         f.write(datas)
    #         datas = s.recv(1024)
    #     f.close()
    #     break
    # print("Done receiving")
if __name__=="__main__":
    start_socket("asset//adit","10.0.0.9",1234)