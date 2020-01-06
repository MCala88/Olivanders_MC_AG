class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def get_items(self, name, sell_in, quality):
        items = [
        ['Aged Brie', 2, 0],
        ['Elixir of the Mongoose', 5, 7],
        ['Sulfuras, Hand of Ragnaros', 0, 80],
        ['Backstage passes to a TAFKAL80ETC concert', 15, 20],
        ['Conjured Mana Cake', 3, 6]
        ]
        return items
        
    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)    

    def set_SellIn(self): #no baja de cero
        if self.sell_in:
            self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in <= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-1)
        self.set_SellIn()

class AgedBrie(NormalItem):
    sell_in = 2
    quality = 0
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 0:
            self.quality += 1
        else:
            self.quality += 2

class Sulfuras(NormalItem):
    sell_in = 0
    quality = 80
    #def __init__(self, name, sell_in, quality):
    #    Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        assert self.quality == 80
        
    def set_SellIn(self):
        assert self.sell_in == self.sell_in

class Backstagepass(NormalItem):
    sell_in = 15
    quality = 20
    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality += 1
        elif self.sell_in > 5:
            self.setQuality += 2
        elif self.sell_in > 0:
            self.setQuality += 3
        else:
            self.quality = 0
        #self.set_SellIn()
        
class Conjured(NormalItem):
    sell_in = 3
    quality = 6
    def update_quality(self):
        if self.sell_in <= 0:
            self.setQuality(-4)
        else:
            self.setQuality(-2)

if __name__ == '__main__':

    item = NormalItem("Pene de fierro", 2, 3)
    print(item)

    for dia in range(1, 10):
        item.update_quality()
        print(item)
    

