from node import Node


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.head.prev = self.tail
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.size += 1

    def pos_g(self):
        return int(self.size - 1)

    def print_list(self):
        if not self.head:
            return

        current = self.head
        cont = self.size - 1
        while current:
            print(current.data, end=f'x {cont} ')
            current = current.next
            cont -= 1
            if current == self.head:
                break
        print()

    def delete(self, data):
        if not self.head:
            return

        current = self.head
        while current.data != data:
            current = current.next
            if current == self.head:
                return

        if current == self.head:
            self.head = current.next
            self.tail.next = self.head
            self.head = current.next
            self.tail.next = self.head
            self.head.prev = self.tail
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def refractor(self, old_data, new_data):
        if not self.head:
            return

        current = self.head
        while current.data != old_data:
            current = current.next
            if current == self.head:
                return

        current.data = new_data

    def search(self, data):
        if not self.head:
            return None

        current = self.head
        while current.data != data:
            current = current.next
            if current == self.head:
                return None

        return current.data

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index < 0:
            print('El inidice esta fuera de rango')
            return
        if index == 0:
            self.insert_at_index(index, data)
            return

        cont = 0
        current = self.head
        while cont < index - 1:
            current = current.next
            cont += 1
            if current == self.head:
                print('El inidice esta fuera de rango')
                return

        next_node = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = next_node
        next_node.prev = new_node
