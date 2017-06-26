
class Furniture:
    def __init__(self):
        self.name
        self.elements = []
        self.price

    def total_price(self):
        for i in range:
            self.prioe += self.elemets[i].price
        return self.price

"""
Calculation of total cost for Wood - Volume * Price of 1 cube of material + 0.25*(Price of paint * Number of Layers) * Square of Surface
Calculation of total cost for MDF - Square * Price of 1 square meter of material + 0.25*(Price of paint * Number of Layers) * Square of Surface
Calculation of details per template - RoundUp(TemplateWidth - DetailWidth) * RoundUp(TemplateLength - DetailLength)
Calculation of loss coefficient for MDF - MAX(TemplateSquare - DetailSquare)
Calculation of Additive price - ClearPrice * Loss coefficient
Calculation of Material price - ClearPrice + AdditivePrice/TemplateSquare
"""


class FurnitureElement:
    def __init__(self, name, width, length, depth, price, paint, material):
        self.name = name
        self.width = width
        self.length = length
        self.depth = depth
        self.price = price
        self.paint = paint
        self.material = material

    def show(self):
        print(self.name, str(self.width) + "x" + str(self.length) + "x" + str(self.depth), self.price, self.paint, self.material)


test = FurnitureElement("Box", 600, 300, 400, 15000, "White", "Oak")
test.show()
