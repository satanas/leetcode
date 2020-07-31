class MedianOfAStream:
    max_heap = []
    min_heap = []

    def insert_num(self, num):
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            self.max_heap.append(num)
        else:
            if num > self.max_heap[0]:
                if len(self.min_heap) > 0:
                    if num > self.min_heap[0]:
                        self.min_heap.append(num)
                    else:
                        self.min_heap.insert(0, num)
                else:
                    self.min_heap.append(num)
            else:
                self.max_heap.append(num)

        # Balance heaps
        diff = len(self.max_heap) - len(self.min_heap)
        if abs(diff) > 1:
            if diff > 0:
                biggest_max_heap = self.max_heap[0]
                self.max_heap = self.max_heap[1:]
                self.min_heap.insert(0, biggest_max_heap)
            else:
                smallest_min_heap = self.min_heap[0]
                self.min_heap = self.min_heap[1:]
                self.max_heap.insert(0, smallest_min_heap)

        if self.total_elements() % 2 != 0 and len(self.min_heap) > len(self.max_heap):
            smallest_min_heap = self.min_heap[0]
            self.max_heap.insert(0, smallest_min_heap)
            self.min_heap = self.min_heap[1:]
            
        return -1

    def find_median(self):
        biggest_max_heap = self.max_heap[0] if len(self.max_heap) > 0 else 0
        smallest_min_heap = self.min_heap[0] if len(self.min_heap) > 0 else 0

        if self.total_elements() % 2 == 0:
            return (biggest_max_heap + smallest_min_heap) / 2
        else:
            return biggest_max_heap

    def total_elements(self):
        return len(self.max_heap) + len(self.min_heap)


if __name__ == "__main__":
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))