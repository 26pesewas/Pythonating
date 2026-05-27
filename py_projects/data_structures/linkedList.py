class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data, self.head)
        self.head = new_node

    def print(self):
        if self.head is  None:
            print("This Linked List is empty")
            return

        itr = self.head
        my_llist = ''

        while itr:
            my_llist += str(itr.data) + '-->'
            itr = itr.next

        my_llist += "None"
        print(my_llist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count

    def remove_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter +=1

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                # create a new node
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            counter +=1

    def insert_after_index(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        counter = 0
        itr = self.head
        while itr:
            if counter == index:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            counter +=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        # itr.next is to check if there are more elements in the linked list
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

ll = LinkedList()
ll.insert_values(["apples","strawberries","watermelons","blueberries"])
ll.insert_at_index(3,"mangoes")
ll.print()
ll.insert_after_index(3,"aluguintugui")
ll.remove_by_value("watermelons")
ll.print()