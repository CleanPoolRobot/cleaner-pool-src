import time
import communication as SERVICE


FOREVER = True
FRONT = 0
RIGHT = 90
BACK = 180
SIDEWAY = 90
VERTICAL = 0


def find_corner():
    # TODO: Think about the logic of how the CleanPoolRobot will find the
    #       corner of the pool.
    #
    return


def activate_water_pump():
    SERVICE.activate_pump()
    return


def deactivate_water_pump():
    SERVICE.deactive_pump()
    return


def turn_pipe(angle):
    return


def turn_wheels(angle):
    return


def read_front_distance_sensor():
    return 0


def read_back_distance_sensor():
    return 0


def read_right_distance_sensor():
    return 0


def read_left_distance_sensor():
    return 0


def deactivate_brush():
    return 0


def move_front():
    deactivate_water_pump()
    turn_pipe(FRONT)  # degree
    turn_wheels(VERTICAL)  # degree

    activate_water_pump()

    while FOREVER:
        distance = read_front_distance_sensor()  # cm

        if distance <= 5:
            deactivate_water_pump()
            deactivate_brush()
            break

    return


def move_right():
    five_seconds = 5

    deactivate_water_pump()
    turn_pipe(RIGHT)
    turn_wheels(SIDEWAY)

    activate_water_pump()
    time.sleep(five_seconds)  # second

    deactivate_water_pump

    return


def move_back():
    five_centimeters = 5

    deactivate_water_pump()
    turn_pipe(BACK)
    turn_wheels(VERTICAL)

    activate_water_pump()

    while FOREVER:
        distance = read_back_distance_sensor()  # cm

        if distance <= five_centimeters:
            deactivate_water_pump()
            deactivate_brush()
            break

    return


def state_machine(state):
    front = 1
    right = 2
    back = 3

    if state == front:
        move_front()

        previous_state = state
        state = right
    elif state == right:
        move_right()

        if previous_state == front:
            state = back
        else:
            state = front

    elif state == back:
        move_back()

        previous_state = state
        state = right

    return state


def route_course():
    activate_water_pump()

    state = 1

    while FOREVER:
        front_sensor = read_front_distance_sensor()
        back_sensor = read_back_distance_sensor()
        right_sensor = read_right_distance_sensor()
        left_sensor = read_left_distance_sensor()

        if (front_sensor > 5 and right_sensor > 5) or\
           (back_sensor > 5 and left_sensor > 5):
            break

        state = state_machine(state)

    return


def finish():
    # TODO: Think about the logic of how the CleanPoolRobot will turn back
    #       when it finish clean the pool.
    #
    return


def main():
    find_corner()
    route_course()
    finish()

    return

main()
