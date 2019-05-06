from omikuji.models import kannushi


def omikuji_robot():
    kannushi_robot = kannushi.Kannushi()
    kannushi_robot.hello()
    kannushi_robot.previous_result()
    kannushi_robot.omikuji()
    kannushi_robot.omikuji_result()
