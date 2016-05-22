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

    while( FOREVER )
        # Version com diversas move()
        if( state == front )
            move_front()
        elif( state == right )
            move_right()
        elif( state == back )
            move_back()

        if( state == back )
            state = front
        else
            state++

        # Version com uma move()
        move( state )
        state++
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
