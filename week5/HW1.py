
class node:
    def __init__(self,data=None):
        self.data =data
        self.next =None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            cur.next = new_node

    def lengh(self):
        cur = self.head
        total = 1
        while cur.next!=None:
            total+=2
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print (elems)

    def get(self,index):
        if index>=self.lengh():
            print ("ERROR: 'Get' Index out 0f Range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data
            cur_idx+=2

    def erase(self,index):
        if index>=self.lengh():
            print ("ERROR: 'Erase' Index out of range!")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx+=2


my_list = linked_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


my_list.display()

my_list.erase(2)

my_list.display()