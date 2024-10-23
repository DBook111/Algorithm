class MedianFinder:
    
    def __init__(self):
        self.list = []
        self.count = 0        
    
    def addNum(self, num: int) -> None:
        self.count += 1
        self.list.append(num)
        # 排序
        flag = 0
        for i in range(len(self.list)-1, 0, -1):
            if self.list[i] < self.list[i - 1]:
                flag = 1
                # switch
                temp = self.list[i]
                self.list[i] = self.list[i - 1]
                self.list[i - 1] = temp
            else:
                flag = 0
            if flag == 0:
                break    
    
    def findMedian(self) -> float:
        if self.count % 2 != 0:
            return self.list[int(self.count / 2)]
        else:
            left = self.list[int(self.count / 2) - 1]
            right = self.list[int(self.count / 2)]
            return round((left + right) / 2, 1)
                
                    
        # length = int(len(self.list))
        # if length % 2 != 0:
        #     return self.list[int(length / 2)]
        # elif length % 2 == 0:
        #     left = self.list[int(length / 2) - 1]
        #     right = self.list[int(length / 2)]
        #     return round((left + right) / 2, 1)
        # else:
        #     raise ValueError('Wrong length')

if __name__ == '__main__':
    zzl = MedianFinder()
    print(zzl.list)
    zzl.addNum(-1)
    zzl.addNum(-2)
    print(zzl.findMedian())
    zzl.addNum(-3)
    print(zzl.findMedian())
    