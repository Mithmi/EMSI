
class Furniture:
    def __init__(self):
        self.name
        self.elemets = []
        self.price

    def total_price(self):
        for i in range:
            self.prioe += self.elemets[i].price
        return self.price

class FurnitureElement:
    def __init__(self, name, width, length, depth, price, paint):
        self.name = name
        self.width = width
        self.lenght = length
        self.depth = depth
        self.price = price
        self.paint = paint

    def show(self):
        print(self.name, str(self.width) + "x" + str(self.lenght) + "x" + str(self.depth), self.price, self.paint)


test = FurnitureElement("Box", 600, 300, 400, 15000, "White")
test.show()