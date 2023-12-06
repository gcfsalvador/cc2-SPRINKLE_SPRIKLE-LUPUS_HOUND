import random

class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


    # INSTANCES OF WEAPONS CLASS
Fists = Weapons(name = "Divergent Fists", damage = random.randint(15,25))
Rusted_Sword = Weapons("Rusted Sword", damage = random.randint(15, 25))
Broken_Dagger = Weapons("Broken Dagger", damage = random.randint(15, 25))
Conditioned_Blade = Weapons("Conditioned Blade", damage = random.randint(40, 65))
Skirmished_Scimitar = Weapons("Skirmished Scimitar", damage = random.randint(35, 55))
Oathkeeper = Weapons("Oathkeeper", damage = random.randint(45, 70))
Spiked_Gauntlets = Weapons("Spiked Gauntlets", damage = random.randint(15, 35))
Defiler = Weapons("Defiler", damage = random.randint(40, 90))
Cursed_Object = Weapons("Slice and Dice", damage = random.randint(30, 60))
Prowess = Weapons("Prowess' Defeat", damage = random.randint(30, 70))
LeftRight_GOODNIGHT = Weapons("These Hands.", damage = random.randint(80, 100))
Magic_GUN = Weapons("Rapier & Wand", damage = random.randint(45, 70))

    # SPELLCAST

Lava = Weapons("Spellscroll Lava", damage = random.randint(50, 75))
Water = Weapons("Spellscroll Water", damage = random.randint(35, 50))
Air = Weapons("Spellscroll Air", damage = random.randint(45, 65))
Fire = Weapons("Spellscroll Fire", damage = random.randint(50, 65))
Soul = Weapons("Spellscroll Necro", damage = random.randint(20, 65))
Blood = Weapons("Spellscroll Blood", damage = random.randint(45, 65))
Limitless = Weapons("Mobius Strip", damage = random.randint(65,85))
Cleave_Dismantle = Weapons("Assemble & Disassemble", damage = random.randint(65,90))

    # FOR ENEMIES
Mucus_Fingers = Weapons("Mucus Fingers", damage = random.randint(1, 10))
Solid_Teardrop = Weapons("Solid Teardrop", damage = random.randint(10, 20))
Membrane_Screech = Weapons("Membrane Screech", damage = random.randint(20, 50))
Black_Breath = Weapons("Black Breath", damage = random.randint(20, 50))
Cavity_Eyes = Weapons("Cavity Eyes", damage = random.randint(25, 40))
Deformed_Fetus = Weapons("Deformed Fetus", damage = random.randint(20, 50))
Splitstreak = Weapons("Splitstreaker", damage = random.randint(30, 45))
Onigiri = Weapons("Enma, Wado Ichimonji, Sandai Kitetsu", damage = random.randint(65, 90))
Eyes6 = Weapons("Six Eyes", damage = random.randint(60,95))