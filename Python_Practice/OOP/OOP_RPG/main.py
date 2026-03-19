import Equipment
import Classes

if __name__ == '__main__':

    #mythril_armor = Equipment.Armor('Mythril Armor', 5000, 50) Example of creating new armor

    alina = Classes.Warrior('Alina')
    volodymyr = Classes.Archer('Volodymyr')
    nata = Classes.Mage('Nata')

    alina.level_ups(51)
    volodymyr.level_ups(51)
    nata.level_ups(51)

    alina.equip_bronze()
    volodymyr.equip_bronze()
    nata.equip_bronze()

    alina.fight(nata)