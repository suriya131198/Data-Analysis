class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        print("--- Appended Value {} ---" .format(value))

    def pop_last(self):
        if self.length == 0:
            print("--- No Node found ---")
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        print("--- Pop completed Successfully ---")
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        print("--- Prepend Added {} ---" .format(value))
        return True

    def pop_first(self):        
        if self.length == 1:
            return None            
        elif self.length == 0:
            self.head = None
            self.tail = None
            return True
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        print("--- Pop First Completed ---")
        return True

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        print("--- Received the Value {} ---" .format(temp.value))
        return temp
    
    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            print("--- Value Setted in the Index ---")
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        print('--- Value Inserted ---')

    def remove(self, index):
        print("Length")
        print(self.length-1)
        if index < 0 or index >= self.length:
            print("Out Of Index")
            return None
        if index == 0:
            print('Removing the 1st value')
            self.length -= 1
            return self.pop_first()
        if index == (self.length-1):
            print('Removing the Last Value')
            self.length -= 1
            return self.pop_last()
        prev = self.get_value(index-1)
        temp = prev.next
        prev.next = temp.next
        print("Removed the index {}".format(index))
        self.length -= 1
        return temp.value

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        print('--- Reversed the LinkedList ---')
        return True

my_linked_list = LinkedList(0)

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

# my_linked_list.pop_last()

# my_linked_list.prepend(4)

# my_linked_list.pop_first()

# my_linked_list.set_value(1, 4)

# my_linked_list.insert(3, 8)

# my_linked_list.remove(5)

# my_linked_list.print_list()

# my_linked_list.reverse()

# my_linked_list.print_list()
