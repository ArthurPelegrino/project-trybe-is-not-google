from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()
        # self.len = 0

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
        # self.len += 1

    def dequeue(self):
        # if len(self.queue) == 0:
        #     return None
        # self.len -= 1
        return self.queue.pop(0)

    def search(self, index):
        if index >= len(self.queue) or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]


# teste = Queue()
# teste.
