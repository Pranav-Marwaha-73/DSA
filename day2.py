class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def user_logic(linked_list):
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    values = list(map(int, data[1:]))
    ll = LinkedList()
    for value in values:
        ll.push(value)
    result = user_logic(ll)
    print(result)

if __name__ == "__main__":
    main()