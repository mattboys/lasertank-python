GAMEBOARD_SIZE = 16

Empty = "Empty"
Grass = "Grass"
Flag = "Flag"
Water = "Water"
Conveyor_N = "Conveyor_N"
Conveyor_S = "Conveyor_S"
Conveyor_E = "Conveyor_E"
Conveyor_W = "Conveyor_W"
Ice = "Ice"
ThinIce = "ThinIce"
Bridge = "Bridge"
Tunnel_0 = "Tunnel_0"
Tunnel_1 = "Tunnel_1"
Tunnel_2 = "Tunnel_2"
Tunnel_3 = "Tunnel_3"
Tunnel_4 = "Tunnel_4"
Tunnel_5 = "Tunnel_5"
Tunnel_6 = "Tunnel_6"
Tunnel_7 = "Tunnel_7"
Tunnel_8 = "Tunnel_8"
Tunnel_9 = "Tunnel_9"

Tank_N = "Tank_N"
Tank_S = "Tank_S"
Tank_E = "Tank_E"
Tank_W = "Tank_W"
Solid = "Solid"
Block = "Block"
Wall = "Wall"
Antitank_N = "Antitank_N"
Antitank_S = "Antitank_S"
Antitank_E = "Antitank_E"
Antitank_W = "Antitank_W"
DeadAntitank_N = "DeadAntitank_N"
DeadAntitank_S = "DeadAntitank_S"
DeadAntitank_E = "DeadAntitank_E"
DeadAntitank_W = "DeadAntitank_W"
Mirror_NW = "Mirror_NW"
Mirror_NE = "Mirror_NE"
Mirror_SE = "Mirror_SE"
Mirror_SW = "Mirror_SW"
Glass = "Glass"
RotMirror_NW = "RotMirror_NW"
RotMirror_NE = "RotMirror_NE"
RotMirror_SE = "RotMirror_SE"
RotMirror_SW = "RotMirror_SW"

#
#
# DIRECTIONS = ["N", "S", "E", "W"]
#
# ANGLES = ["NW", "NE", "SE", "SW"]
#
# TERRAIN_NAMES = {
#     "Grass": {},
#     "Flag": {},
#     "Water": {},
#     "Conveyor": {"direction": DIRECTIONS},
#     "Ice": {},
#     "ThinIce": {},
#     "Bridge": {},
#     "Tunnel": {"tunnel_id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
# }
#
# ITEM_NAMES = {
#     "Tank": {"direction": DIRECTIONS},
#     "Solid": {},
#     "Block": {},
#     "Wall": {},
#     "Antitank": {"direction": DIRECTIONS},
#     "DeadAntitank": {"direction": DIRECTIONS},
#     "Mirror": {"angle": ANGLES},
#     "Glass": {},
#     "RotMirror": {"angle": ANGLES},
# }
#
# if __name__ == "__main__":
#     for t, v in ITEM_NAMES.items():
#         if v:
#             for name, p in v.items():
#                 for pa in p:
#                     print(f"{t}_{pa}")
#         else:
#             print(f"{t}")


    # print("TERRAIN:")
    # for s in TERRAIN_NAMES:
    #     print(s[:2])
    #
    # for s in ITEM_NAMES:
    #     print(s[:2])
    #
    # all_s = {
    #     "Gr",
    #     "Fl",
    #     "Wa",
    #     "Co",
    #     "Ic",
    #     "Th",
    #     "Br",
    #     "Tu",
    #     "Ta",
    #     "So",
    #     "Bl",
    #     "Wa",
    #     "An",
    #     "De",
    #     "Mi",
    #     "Gl",
    #     "Ro",
    #        }




# print("Printing all sprites with their parameters")
    # i = 0
    #
    # def iprint(str):
    #     global i
    #     print(f"{i}{str}")
    #     i+=1
    #
    # print("TERRAIN:")
    # for terrain, parameters in TERRAIN_NAMES.items():
    #     if parameters:
    #         print(f"        {terrain}")
    #         for para_name, options in parameters.items():
    #             for opt in options:
    #                 iprint(f"          {para_name} : {opt}")
    #     else:
    #         iprint(f"       {terrain}")
    #
    # print()
    # print("ITEMS:")
    # for item, parameters in ITEM_NAMES.items():
    #     if parameters:
    #         print(f"         {item}")
    #         for para_name, options in parameters.items():
    #             for opt in options:
    #                 iprint(f"           {para_name} : {opt}")
    #     else:
    #         iprint(f"       {item}")
