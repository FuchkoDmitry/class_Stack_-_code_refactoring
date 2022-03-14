class Stack:
    def __init__(self, elements_list):
        self.elements_list = elements_list

    def is_empty(self):
        if not self.elements_list:
            return True
        return False

    def push(self, element):
        self.elements_list.append(element)

    def pop(self):
        return self.elements_list.pop(-1)

    def peek(self):
        return self.elements_list[-1]

    def size(self):
        return len(self.elements_list)
