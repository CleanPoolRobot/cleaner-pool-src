import RPi.GPIO as GPIO
import time
import pinout
import communication


FOREVER = True


def find_corner():
    # TODO: Think about the logic of how the CleanPoolRobot will find the
    #       corner of the pool.
    #
    return


def activate_water_pump():
    active_pump()

    return


def deactivate_water_pump():
    return


def turn_pipe(angle):
    return


def turn_wheels(angle):
    return


def activate_front_distance_sensor():
    return


def deactivate_brush():
    return


def move_front():
    deactivate_water_pump()
    turn_pipe(0)  # degree
    turn_wheels(0)  # degree

    activate_water_pump()

    while FOREVER:
        distance = activate_front_distance_sensor()  #  cm

        if distance <= 5:
            deactivate_water_pump()
            deactivate_brush()
            break

    return


def move_right():
    deactivate_water_pump()
    turn_pipe(90)
    turn_wheels(90)

    activate_water_pump()
    time.sleep(5)  # second

    deactivate_water_pump

    return


def route_course():
    activate_water_pump()

    front = 1
    right = 2
    back = 3

    state = front
    previous_state = front

    while FOREVER:
        if state == front:
            move_front()

            previous_state = state
            state = right
        elif state == right:
            move_right()

            if previous_state == front:
                state = right
            else:
                state = back

        elif state == back:
            move_back()

            previous_state = state
            state = right

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
