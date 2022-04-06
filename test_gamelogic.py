from lasertank import *


def helper_print_test_functions(folder, filename, numbers):
    if isinstance(numbers, int):
        numbers = [numbers]
    print(f"# {filename}")
    filename_clean = filename.replace("-", "_").replace("'", "")
    for number in numbers:
        print(f"def test_{filename_clean}_level_{number:04}():")
        print(f'    assert run_lvl_playback("{folder}/{filename}", {number})')
        print("\n")


def run_lvl_playback(level_name, level_number, show=False):
    if isinstance(level_number, int):
        level_number = f"{level_number:04}"
    pb = load_playback(f"resources/levels/{level_name}_{level_number}.lpb")
    game = load_level(f"resources/levels/{level_name}.lvl", pb["number"])
    game.queue_new_inputs(pb["playback"])
    if show:
        graphics = Graphics()
        clock = pygame.time.Clock()
    else:
        graphics = None
        clock = None

    timeout_counter = 0
    moves_left_prev = 0
    while game.running and timeout_counter < 500:
        game.tick()

        # End early if stuck on no moves or inf loop
        moves_left = len(game.moves_buffer)
        if moves_left == 0 or moves_left == moves_left_prev:
            timeout_counter += 1
        else:
            timeout_counter = 0
        moves_left_prev = moves_left

        if show:
            graphics.draw_board(game)
            clock.tick(100)
    return game.state.reached_flag


# Tutors
def test_tutor_level_0001():
    assert run_lvl_playback("tutor/Tutor", 1)


def test_tutor_level_0002():
    assert run_lvl_playback("tutor/Tutor", 2)


def test_tutor_level_0003():
    assert run_lvl_playback("tutor/Tutor", 3)


def test_tutor_level_0004():
    assert run_lvl_playback("tutor/Tutor", 4)


def test_tutor_level_0005():
    assert run_lvl_playback("tutor/Tutor", 5)


def test_tutor_level_0006():
    assert run_lvl_playback("tutor/Tutor", 6)


def test_tutor_level_0007():
    assert run_lvl_playback("tutor/Tutor", 7)


def test_tutor_level_0008():
    assert run_lvl_playback("tutor/Tutor", 8)


def test_tutor_level_0009():
    assert run_lvl_playback("tutor/Tutor", 9)


def test_tutor_level_0010():
    assert run_lvl_playback("tutor/Tutor", 10)


def test_tutor_level_0011():
    assert run_lvl_playback("tutor/Tutor", 11)


def test_tutor_level_0012():
    assert run_lvl_playback("tutor/Tutor", 12)


def test_tutor_level_0013():
    assert run_lvl_playback("tutor/Tutor", 13)


# Tricks
def test_tricks_level_0001():
    assert run_lvl_playback("tricks/Tricks", 1)


def test_tricks_level_0002():
    assert run_lvl_playback("tricks/Tricks", 2)


def test_tricks_level_0003():
    assert run_lvl_playback("tricks/Tricks", 3)


def test_tricks_level_0004():
    assert run_lvl_playback("tricks/Tricks", 4)


def test_tricks_level_0005():
    assert run_lvl_playback("tricks/Tricks", 5)


def test_tricks_level_0006():
    assert run_lvl_playback("tricks/Tricks", 6)


def test_tricks_level_0007():
    assert run_lvl_playback("tricks/Tricks", 7)


def test_tricks_level_0008():
    assert run_lvl_playback("tricks/Tricks", 8)


def test_tricks_level_0009():
    assert run_lvl_playback("tricks/Tricks", 9)


def test_tricks_level_0010():
    assert run_lvl_playback("tricks/Tricks", 10)


def test_tricks_level_0011():
    assert run_lvl_playback("tricks/Tricks", 11)


def test_tricks_level_0012():
    assert run_lvl_playback("tricks/Tricks", 12)


def test_tricks_level_0013():
    assert run_lvl_playback("tricks/Tricks", 13)


def test_tricks_level_0014():
    assert run_lvl_playback("tricks/Tricks", 14)


def test_tricks_level_0015():
    assert run_lvl_playback("tricks/Tricks", 15)


def test_tricks_level_0016():
    assert run_lvl_playback("tricks/Tricks", 16)


def test_tricks_level_0017():
    assert run_lvl_playback("tricks/Tricks", 17)


def test_tricks_level_0018():
    assert run_lvl_playback("tricks/Tricks", 18)


def test_tricks_level_0019():
    assert run_lvl_playback("tricks/Tricks", 19)


def test_tricks_level_0020():
    assert run_lvl_playback("tricks/Tricks", 20)


def test_tricks_level_0021():
    assert run_lvl_playback("tricks/Tricks", 21)


def test_tricks_level_0022():
    assert run_lvl_playback("tricks/Tricks", 22)


def test_tricks_level_0023():
    assert run_lvl_playback("tricks/Tricks", 23)


def test_tricks_level_0024():
    assert run_lvl_playback("tricks/Tricks", 24)


def test_tricks_level_0025():
    assert run_lvl_playback("tricks/Tricks", 25)


def test_tricks_level_0026():
    assert run_lvl_playback("tricks/Tricks", 26)


# Standard Levels
def test_standard_level_0001():
    assert run_lvl_playback("standard_levels/LaserTank", 1)


def test_standard_level_0002():
    assert run_lvl_playback("standard_levels/LaserTank", 2)


def test_standard_level_0003():
    assert run_lvl_playback("standard_levels/LaserTank", 3)


def test_standard_level_0004():
    assert run_lvl_playback("standard_levels/LaserTank", 4)


def test_standard_level_0005():
    assert run_lvl_playback("standard_levels/LaserTank", 5)


def test_standard_level_0006():
    assert run_lvl_playback("standard_levels/LaserTank", 6)


def test_standard_level_0007():
    assert run_lvl_playback("standard_levels/LaserTank", 7)


def test_standard_level_0008():
    assert run_lvl_playback("standard_levels/LaserTank", 8)


def test_standard_level_0009():
    assert run_lvl_playback("standard_levels/LaserTank", 9)


def test_standard_level_0010():
    assert run_lvl_playback("standard_levels/LaserTank", 10)


def test_standard_level_0011():
    assert run_lvl_playback("standard_levels/LaserTank", 11)


def test_standard_level_0012():
    assert run_lvl_playback("standard_levels/LaserTank", 12)


# Custom Tests
def test_custom_tests_level_0001():
    assert run_lvl_playback("custom_tests/CustomTests", 1)


def test_custom_tests_level_0002():
    assert run_lvl_playback("custom_tests/CustomTests", 2)


def test_custom_tests_level_0003():
    assert run_lvl_playback("custom_tests/CustomTests", 3)


def test_custom_tests_level_0004():
    assert run_lvl_playback("custom_tests/CustomTests", 4)


def test_custom_tests_level_0005():
    assert run_lvl_playback("custom_tests/CustomTests", 5)


def test_custom_tests_level_0006():
    assert run_lvl_playback("custom_tests/CustomTests", 6)


def test_custom_tests_level_0007():
    assert run_lvl_playback("custom_tests/CustomTests", 7)


# Game-Objects-in-LT
def test_Game_Objects_in_LT_level_0001():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 1)


def test_Game_Objects_in_LT_level_0002():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 2)


def test_Game_Objects_in_LT_level_0003():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 3)


def test_Game_Objects_in_LT_level_0004():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 4)


def test_Game_Objects_in_LT_level_0005():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 5)


def test_Game_Objects_in_LT_level_0006():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 6)


def test_Game_Objects_in_LT_level_0007():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 7)


def test_Game_Objects_in_LT_level_0008():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 8)


def test_Game_Objects_in_LT_level_0009():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 9)


def test_Game_Objects_in_LT_level_0010():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 10)


def test_Game_Objects_in_LT_level_0011():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 11)


def test_Game_Objects_in_LT_level_0012():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 12)


def test_Game_Objects_in_LT_level_0013():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 13)


def test_Game_Objects_in_LT_level_0014():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 14)


def test_Game_Objects_in_LT_level_0015():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 15)


def test_Game_Objects_in_LT_level_0016():
    assert run_lvl_playback("Game-Objects-in-LT/Game-Objects-in-LT", 16)


# Pono's_trick
def test_Ponos_trick_level_0001():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 1)


def test_Ponos_trick_level_0002():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 2)


def test_Ponos_trick_level_0003():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 3)


def test_Ponos_trick_level_0004():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 4)


def test_Ponos_trick_level_0005():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 5)


def test_Ponos_trick_level_0006():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 6)


def test_Ponos_trick_level_0007():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 7)


def test_Ponos_trick_level_0008():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 8)


def test_Ponos_trick_level_0009():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 9)


def test_Ponos_trick_level_0010():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 10)


def test_Ponos_trick_level_0011():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 11)


def test_Ponos_trick_level_0012():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 12)


def test_Ponos_trick_level_0013():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 13)


def test_Ponos_trick_level_0014():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 14)


def test_Ponos_trick_level_0015():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 15)


def test_Ponos_trick_level_0016():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 16)


def test_Ponos_trick_level_0017():
    assert run_lvl_playback("Pono_trick/Pono's_trick", 17)


def test_Ponos_trick_level_0018a():
    assert run_lvl_playback("Pono_trick/Pono's_trick", "0018a")


def test_Ponos_trick_level_0018b():
    assert run_lvl_playback("Pono_trick/Pono's_trick", "0018b")


def test_Ponos_trick_level_0018c():
    assert run_lvl_playback("Pono_trick/Pono's_trick", "0018c")


# Tutor-with-Playbacks
def test_Tutor_with_Playbacks_level_0001():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 1)


def test_Tutor_with_Playbacks_level_0002():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 2)


def test_Tutor_with_Playbacks_level_0003():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 3)


def test_Tutor_with_Playbacks_level_0004():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 4)


def test_Tutor_with_Playbacks_level_0005():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 5)


def test_Tutor_with_Playbacks_level_0006():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 6)


def test_Tutor_with_Playbacks_level_0007():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 7)


def test_Tutor_with_Playbacks_level_0008():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 8)


def test_Tutor_with_Playbacks_level_0009():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 9)


def test_Tutor_with_Playbacks_level_0010():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 10)


def test_Tutor_with_Playbacks_level_0011():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 11)


def test_Tutor_with_Playbacks_level_0012():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 12)


def test_Tutor_with_Playbacks_level_0013():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 13)


def test_Tutor_with_Playbacks_level_0014():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 14)


def test_Tutor_with_Playbacks_level_0015():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 15)


def test_Tutor_with_Playbacks_level_0016():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 16)


def test_Tutor_with_Playbacks_level_0017():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 17)


def test_Tutor_with_Playbacks_level_0018():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 18)


def test_Tutor_with_Playbacks_level_0019():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 19)


def test_Tutor_with_Playbacks_level_0020():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 20)


def test_Tutor_with_Playbacks_level_0021():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 21)


def test_Tutor_with_Playbacks_level_0022():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 22)


def test_Tutor_with_Playbacks_level_0023():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 23)


def test_Tutor_with_Playbacks_level_0024():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 24)


def test_Tutor_with_Playbacks_level_0025():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 25)


def test_Tutor_with_Playbacks_level_0026():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 26)


def test_Tutor_with_Playbacks_level_0027():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 27)


def test_Tutor_with_Playbacks_level_0028():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 28)


def test_Tutor_with_Playbacks_level_0029():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 29)


def test_Tutor_with_Playbacks_level_0030():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 30)


def test_Tutor_with_Playbacks_level_0031():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 31)


def test_Tutor_with_Playbacks_level_0032():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 32)


def test_Tutor_with_Playbacks_level_0033():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 33)


def test_Tutor_with_Playbacks_level_0034():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 34)


def test_Tutor_with_Playbacks_level_0035():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 35)


def test_Tutor_with_Playbacks_level_0036():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 36)


def test_Tutor_with_Playbacks_level_0037():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 37)


def test_Tutor_with_Playbacks_level_0038():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 38)


def test_Tutor_with_Playbacks_level_0039():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 39)


def test_Tutor_with_Playbacks_level_0040():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 40)


def test_Tutor_with_Playbacks_level_0041():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 41)


def test_Tutor_with_Playbacks_level_0042():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 42)


def test_Tutor_with_Playbacks_level_0043():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 43)


def test_Tutor_with_Playbacks_level_0044():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 44)


def test_Tutor_with_Playbacks_level_0045():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 45)


def test_Tutor_with_Playbacks_level_0046():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 46)


def test_Tutor_with_Playbacks_level_0047():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 47)


def test_Tutor_with_Playbacks_level_0048():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 48)


def test_Tutor_with_Playbacks_level_0049():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 49)


def test_Tutor_with_Playbacks_level_0050():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 50)


def test_Tutor_with_Playbacks_level_0051():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 51)


def test_Tutor_with_Playbacks_level_0052():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 52)


def test_Tutor_with_Playbacks_level_0053():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 53)


def test_Tutor_with_Playbacks_level_0054():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 54)


def test_Tutor_with_Playbacks_level_0055():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 55)


def test_Tutor_with_Playbacks_level_0056():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 56)


def test_Tutor_with_Playbacks_level_0057():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 57)


def test_Tutor_with_Playbacks_level_0058():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 58)


def test_Tutor_with_Playbacks_level_0059():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 59)


def test_Tutor_with_Playbacks_level_0060():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 60)


def test_Tutor_with_Playbacks_level_0061():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 61)


def test_Tutor_with_Playbacks_level_0062():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 62)


def test_Tutor_with_Playbacks_level_0063():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 63)


def test_Tutor_with_Playbacks_level_0064():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 64)


def test_Tutor_with_Playbacks_level_0065():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 65)


def test_Tutor_with_Playbacks_level_0066():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 66)


def test_Tutor_with_Playbacks_level_0067():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 67)


def test_Tutor_with_Playbacks_level_0068():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 68)


def test_Tutor_with_Playbacks_level_0069():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 69)


def test_Tutor_with_Playbacks_level_0070():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 70)


def test_Tutor_with_Playbacks_level_0071():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 71)


def test_Tutor_with_Playbacks_level_0072():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 72)


def test_Tutor_with_Playbacks_level_0073():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 73)


def test_Tutor_with_Playbacks_level_0074():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 74)


def test_Tutor_with_Playbacks_level_0075():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 75)


def test_Tutor_with_Playbacks_level_0076():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 76)


def test_Tutor_with_Playbacks_level_0077():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 77)


def test_Tutor_with_Playbacks_level_0078():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 78)


def test_Tutor_with_Playbacks_level_0079():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 79)


def test_Tutor_with_Playbacks_level_0080():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 80)


def test_Tutor_with_Playbacks_level_0081():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 81)


def test_Tutor_with_Playbacks_level_0082():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 82)


def test_Tutor_with_Playbacks_level_0083():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 83)


def test_Tutor_with_Playbacks_level_0084():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 84)


def test_Tutor_with_Playbacks_level_0085():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 85)


def test_Tutor_with_Playbacks_level_0086():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 86)


def test_Tutor_with_Playbacks_level_0087():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 87)


def test_Tutor_with_Playbacks_level_0088():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 88)


def test_Tutor_with_Playbacks_level_0089():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 89)


def test_Tutor_with_Playbacks_level_0090():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 90)


def test_Tutor_with_Playbacks_level_0091():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 91)


def test_Tutor_with_Playbacks_level_0092():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 92)


def test_Tutor_with_Playbacks_level_0093():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 93)


def test_Tutor_with_Playbacks_level_0094():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 94)


def test_Tutor_with_Playbacks_level_0095():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 95)


def test_Tutor_with_Playbacks_level_0096():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 96)


def test_Tutor_with_Playbacks_level_0097():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 97)


def test_Tutor_with_Playbacks_level_0098():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 98)


def test_Tutor_with_Playbacks_level_0099():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 99)


def test_Tutor_with_Playbacks_level_0100():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 100)


def test_Tutor_with_Playbacks_level_0101():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 101)


def test_Tutor_with_Playbacks_level_0102():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 102)


def test_Tutor_with_Playbacks_level_0103():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 103)


def test_Tutor_with_Playbacks_level_0104():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 104)


def test_Tutor_with_Playbacks_level_0105():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 105)


def test_Tutor_with_Playbacks_level_0106():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 106)


def test_Tutor_with_Playbacks_level_0107():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 107)


def test_Tutor_with_Playbacks_level_0108():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 108)


def test_Tutor_with_Playbacks_level_0109():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 109)


def test_Tutor_with_Playbacks_level_0110():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 110)


def test_Tutor_with_Playbacks_level_0111():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 111)


def test_Tutor_with_Playbacks_level_0112():
    assert run_lvl_playback("Tutor-with-Playbacks/Tutor-with-Playbacks", 112)

# Deaths
def test_Deaths_level_0001():
    assert not run_lvl_playback("deaths/Deaths", 1)

def test_Deaths_level_0002():
    assert not run_lvl_playback("deaths/Deaths", 2)

def test_Deaths_level_0003():
    assert not run_lvl_playback("deaths/Deaths", 3)

def test_Deaths_level_0004():
    assert not run_lvl_playback("deaths/Deaths", 4)

def test_Deaths_level_0005():
    assert not run_lvl_playback("deaths/Deaths", 5)

def test_Deaths_level_0006():
    assert not run_lvl_playback("deaths/Deaths", 6)

