class area():
    def __init__(self, n):
        self.n = n

    def convert(self):
        n = self.n
        lis = []
        for i in range(0, n):
            d = {}
            d["types"] = str(input("Enter type of area {}: ".format(i + 1)))
            d["area"] = float(input("Enter the area {}: ".format(i + 1)))
            lis.append(d)
            i += 1
        for i in lis:
            print("{index} - {types} with area size {area}".format(index=lis.index(i) + 1, types=i["types"],
                                                                       area=i["area"]))


i = int(input("Enter the type of areas you want to input: "))
a = area(i)
a.convert()