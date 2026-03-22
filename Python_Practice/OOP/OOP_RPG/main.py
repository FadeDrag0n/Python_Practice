import Equipment
import Classes

if __name__ == '__main__':

    alina = Classes.Warrior('Alina')

    volodymyr = Classes.Archer('Volodymyr')
    nata = Classes.Mage('Nata')

    alina.level_ups(51)
    volodymyr.level_ups(91)
    nata.level_ups(51)

    alina.equip_bronze()
    volodymyr.equip_bronze()
    nata.armor = Equipment.Armor('Mythril Armor', 5000, 100)
    nata.fight(volodymyr)






