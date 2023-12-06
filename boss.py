import curses
import random
import sys
from entities import Hero
from weapon import LeftRight_GOODNIGHT

Dialogue1 = ['CATCH THESE HANDS!', 'Black Flash!', 'Left Right, GOODNIGHT!', 'You are my Special~', 'I AM BETTER', 'I WILL AVENGE THEM', 'DIE', 'BEGONE DEMON', 'LIGHTNIGN STRIKE', 'ZOLTRAKK', 'You did not sugarcoat it', 'CRITICALLL', 'CRITICAL']

player = Hero("YOU", 300, 5, 3)
player.equip(LeftRight_GOODNIGHT)

class Boss:
    def __init__(self, health=950):
        self.health = health

    def attack(self, player):
        damage_dealt = random.randint(20, 50)
        player.health -= damage_dealt
        return damage_dealt

def draw_boss(stdscr):
    boss_ascii = """

     ,/|    y               /|    /(_)\    |\               y    ||
   ,/  \   ,OGmm          /' `\   \`,'/   /' `\          mm3O,   / `|
  /     \_//            /' / | `\_/\~/\_/' | \ `\            \\_/    `|
 /    |   ||           O  |   \/'   V   `\/   |  O           ||   |    |
|  |  |  /||          O   |,-,|   ,_;_,   |,-,|   O          ||\  |  |  |
|  |   \ | \\        oO    \  \\ '\ I /` //  /    Oo        // | /   |  |
|  \   /\|  M        oO     \ \`\  \ /  /'/ /     Oo        M  |/\   /  |
|   \ |  ` //         O    /~\ \,\  |  /,/ /~\    O         \\ '  | /   |
|  /'\|    M      _____O  /__/ /__| I |__\ \__\  O____       M    |/`\  |
 \ |  `    \\     |     \|  '''  ''' ```  ```  |/     |     //    '  | /
  \|    |   M     |             AZERANTH              |     M   |    |/
   \    \\_//     |                                   |     \\_//    /
    `    `~'      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      `~'    '
    """
    stdscr.addstr(0, 0, boss_ascii)
def draw_stats(stdscr, player, boss):
    stdscr.addstr(7, 49, f" PLAYER STATS ",curses.A_REVERSE)
    stdscr.addstr(8, 45, f"  Vigor: {player.health}", curses.A_BOLD)
    stdscr.addstr(9, 45, f"  Constitution: {player.constitution}", curses.A_BOLD)
    stdscr.addstr(10, 45, f"  WEAPON: {player.weapon.name}", curses.A_BOLD)
    stdscr.addstr(11, 45, f"  Flasks: {player.pots}", curses.A_BOLD)

    stdscr.addstr(13, 0, f"Boss Health: {boss.health}")

def boss_fight(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    boss = Boss()

    while True:
        stdscr.clear()

        draw_boss(stdscr)
        draw_stats(stdscr, player, boss)

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('1'):
            player_damage = player.attack(boss)
            boss_damage = boss.attack(player)

            stdscr.addstr(15, 0, f"You have dealt {player_damage} to the Absolute.")
            stdscr.addstr(16, 0, f"The Absolute dealt {boss_damage} damage to you.")

            if player.health <= 0:
                stdscr.addstr(18, 0, "You are but another Legend.")
                sys.exit()

            if boss.health <= 0:
                stdscr.addstr(18, 0, "You have brought Victory to Humanity.")
                sys.exit()

        stdscr.refresh()
