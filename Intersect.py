class intersect ():
    def __init__(self,lis1, lis2):
        self.lis1 = lis1
        self.lis2 = lis2
    def unique(self):
            result = [i for i in self.lis1 if i in self.lis2]
            if len(result) > 0:
                print (*result, sep = " ")
            else:
                print("No same number")

lis1 = list(int(i) for i in input("Enter numbers in group 1: ").strip().split())
lis2 = list(int(i) for i in input("Enter numbers in group 2: ").strip().split())
s = intersect(lis1, lis2)
s.unique()