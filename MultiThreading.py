import threading
import thread
import time
class check_threding():
    def __init__(self):
        pass

    def add_nos(self,a,b,c):
        add = a + b + c
        print("#####")
        time.sleep(2)
        print add

    def main(self):
        arr = ["t1","t2","t3","t4"]
        # self.add_nos(1,2,3)
        for i in range(len(arr)):
            arr[i] = threading.Thread(target=self.add_nos, args=(1,2,3))
            arr[i].start()
            # self.add_nos(1, 2, 3)

if __name__ == "__main__":
    obj = check_threding()
    obj.main()



