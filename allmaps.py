#Allmaps
import minqlx

class allmaps(minqlx.Plugin):
    def __init__(self):
        self.add_command(("allmaps", "listmaps"), self.cmd_allmaps)

    def cmd_allmaps(self, player, msg, channel):
        player.tell(
                "^5oxodm102_b1      ^3Campgrounds Redux\n"
                "^5karist           ^3mid teamsize CA\n"
                "^56ex              ^3Campgrounds After\n"
                "^5prodcmap7        ^3Fortress 2089 (Hidden Fortress remake)\n"
                "^5ts_dm5/ts_dm5tmp ^3Full Moon - Ufreeze Map tmp is bigger\n"
                "^5nodm10           ^3The Edge 2004 CPM Remix\n"
                "^5szq2dm1ish       ^3Q2DM1-ISH: The Edge Remix\n"
                "^5p1rate_overek    ^3Pirate Overkill Cut em' Hard\n"
                "^56plus            ^36+ (Q3: 6++)\n"
                "^5q1dm6t           ^3The Dark Zone 2020\n"
                "^5oxodm2a          ^3Aero Run (Second Edition)\n"
                "^5shovq2dm1_cpm    ^3The Edge, Revisited!\n"
                "^5nalq1dm6         ^3The Sinister Zone (q1dm6)\n"
                "^5proverek         ^3Pro Overkill / Projectile Vomiting\n"
                "^5dm6remix         ^3Q3DM6 In a hat\n"
                "^5ql_dust          ^3ql_dust2 CS maps\n"
                "^5Opium            ^3Opium\n"
                "^5heroscerated     ^3Heroscerated\n"
                "^5ts_ca1           ^3Fly on Rocket\n"
                "^5heffdm17         ^3DM17 Egyptian Redux\n"
                "^5dAdeX            ^3dAde_X\n"
                "^5e1m7ish3         ^3remake of Quake's E1M7\n"
                "^5ci               ^3Citadel Insatiable\n"
                "^5Arena66          ^3Arena66\n"
                "^5dubneoc          ^3Neorganic Epiphany Sock and Nunuks Geometric Challenge 2\n"
                "^52sweet           ^32!Sweet large map good for 6vs6\n"
                "^5hyperblast       ^3Hyperblast\n"
                "^5ct3dm4           ^3Paranoid  3vs3\n"
                "^5lsjgcoop         ^3MaXimus 4-8 players\n"
                "^5q3dm4remix       ^3Eviscerated remix\n"
                "^5q3dm13remix      ^3Lost World remix\n"
                "^5q3dm1+           ^3The Arena Gate II\n"
                "^5damn_q3dm1       ^3Arena Gate (damn edition)\n"
                "^56ex              ^3Campgrounds After (q3dm6 upgraded)\n"
                "^5prodcmap7        ^3Fortress 2089 (Hidden Fortress remake)\n"
                "^5heroscerated     ^3Heroscerated\n"
                "^5inversekill      ^3Inversekill\n"
                "^513matrix         ^3Campgrounds - Matrix Edition\n"
                "^5gd_tourney1a     ^3Thrill Kill\n"
                "^5Ra3map11pp       ^3Overkill PP\n"
                "^5Ra3map2pp        ^3ShakenNotStirredPP The ProPack Version\n"
                "^5ra3map1          ^3Theatre of Pain by Firestarter\n"
                "^5ra3map1a         ^3Evolution by Firestarter\n"
                "^5ra3map1b         ^3Thunderstruck by Firestarter\n"
                "^5ra3map1c         ^3Canned Heat by Firestarter\n"
                "^5ospca1           ^3American Can-CO\n"
                "^5ospctf1          ^3White Noise\n"
                "^5ospctf2          ^3Crossed Paths\n"
                "^5ospdm1           ^3The New Edge\n"
                "^5ospdm3           ^3Scrap Metal II\n"
                "^5ospdm4           ^3Bitter Embrace\n"
                "^5ospdm2           ^3Batcula\n"
                "^5ospdm5           ^3Deep Inside\n"
                "^5ospdm6           ^3Suicide\n"
                "^5ospdm7           ^3The Dancehall\n"
                "^5ospdm8           ^3The Chastity Belt\n"
                "^5ospdm9           ^3Anticipating Oblivion\n"
                "^5ospdm10          ^3Apologie\n"
                "^5ospdm12          ^3Deschutes\n"
                "^5ospdm11          ^3The Olden Domain\n"
                "^5ospdm13          ^3Bullet Ride\n"
                "^5ospdm14          ^3Epilogue\n"
                "^5ospdm15          ^3Deeper Blue\n"
                "\n"
                "")
        return minqlx.RET_STOP_ALL
        
'''
560545593
623436886
632421088
632254333
575312620
563105825
560535691
560533896
560531568
560523904
557591894
550566693
547252823
540986862
539421982
539421606
607909342
560547573
560548198
560550879
560610357
560647562
572015381
586817666
605561819
606599547
597920398
638619897
638619355
638618725
638618287
638617899
638616850
638531198
638500202
637351306
637350852
632422741
632422465
632422201
632421804
632421451
632421088
632254333
623436886
606599547
600299201
691078677
668999226
728480172
'''

