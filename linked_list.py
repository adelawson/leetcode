class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class lnk_lst:
    def __init__(self):
        self.head= None
    def insert_at_beginning(self,data):
        n = node(data,self.head)
        self.head= n

    def print(self):
        if self.head == None :
            print("the linked list is empty")
            return
    
        lst=[]
        cur_val= self.head
        while True:
            lst.append(cur_val)
            cur_val = cur_val.next
        print(lst)
    
