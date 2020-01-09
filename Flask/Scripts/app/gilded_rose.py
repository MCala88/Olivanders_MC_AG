class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def get_items(self, name, sell_in, quality):
        Brie = AgedBrie("Aged Brie", 2, 0)
        Elixir = NormalItem("Elixir of the Mongoose", 5, 7)
        Ragnaros = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
        Tafkal = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 22)
        ManaCake = Conjured("Conjured Mana Cake", 3, 6)

        Inventory = [Brie, Elixir, Ragnaros, Tafkal, ManaCake]
        
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
    def set_SellIn(self):
        if self.sell_in >= 0:
            self.sell_in -= 1
        else:
            self.sell_in -= 1

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
    def setQuality(self):
        self.quality()

    def update_quality(self):
        if self.quality >= 50:
            self.quality = 50
        elif self.sell_in <= 0:
            if self.quality == 49:
                self.quality = 50
            else:
                self.quality += 2
        else:
            self.quality += 1
        self.set_SellIn()

class Sulfuras(NormalItem):
    def update_quality(self):
        assert self.quality == 80      

class Backstagepass(NormalItem):
    def update_quality(self):
        if self.sell_in <= 0:
            self.quality = 0
        if self.quality >= 50:
            self.quality = 50
        elif self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5:
            if self.quality == 49:
                self.quality = 50
            else:
                self.quality += 2
        elif self.sell_in > 0:
            if self.quality >= 48:
                self.quality = 50
            else:
                self.quality += 3
        self.set_SellIn()
        
class Conjured(NormalItem):
    def update_quality(self):
        if self.sell_in <= 0:
            self.quality -= 4
        else:
            self.quality -= 2
        self.set_SellIn()

if __name__ == '__main__':

    item = AgedBrie("Aged Brie", 2, 0)
    
    for dia in range(1, 30):
        item.update_quality()
        print(item)
    
    print ('---------------------------------')

    item = NormalItem("Elixir of the Mongoose", 5, 7)
    print(item)

    for dia in range(1, 30):
        item.update_quality()
        print(item)

    print ('---------------------------------')

    item = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 22)
    print(item)

    for dia in range(1, 30):
        item.update_quality()
        print(item)

    print ('---------------------------------')

    item = AgedBrie("Aged Brie", 2, 1)
    print(item)

    for dia in range(1, 30):
        item.update_quality()
        print(item)

    print ('---------------------------------')

    item = Conjured("Conjured Mana Cake", 3, 6)
    print(item)

    for dia in range(1, 30):
        item.update_quality()
        print(item)
