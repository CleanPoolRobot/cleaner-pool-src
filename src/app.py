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
