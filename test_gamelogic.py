from lasertank import *


def run_lvl_playback(level_name, level_number, show=False):
    pb = load_playback(f"resources/levels/{level_name}_{level_number:04}.lpb")
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
            graphics.draw_board(game.board)
            clock.tick(100)
    return game.reached_flag


def test_box_through_tunnel():
    pb = load_playback("resources/levels/tunnel_test/TunnelTest_0001.lpb")
    game = load_level("resources/levels/tunnel_test/TunnelTest.lvl", pb["number"])
    game.queue_new_inputs(pb["playback"])
    while game.running:
        game.tick()
    assert game.reached_flag


# def test_tricks():
#     for i in range(1, 13):
#         assert run_lvl_playback("tricks/Tricks", i)

# def test_levels():
#     for i in range(1, 13):
#         assert run_lvl_playback("standard_levels/LaserTank", i)

# def test_tutors():
#     for i in range(1, 14):
#         assert run_lvl_playback("tutor/Tutor", i)

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
