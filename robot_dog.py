from time import sleep
import utime
from ROBOT_ACTIONS import *

# ---- Initialize current servo positions ---- #
servo_angles = [90, 90, 120, 75, 120, 60, 110, 65]

def move_servos_smooth(target_angles, step=3, delay=0.01):
    """Move all servos smoothly in parallel toward target_angles"""
    global servo_angles
    done = False
    while not done:
        done = True
        for i in range(len(servo_angles)):
            if abs(target_angles[i] - servo_angles[i]) > step:
                done = False
                if target_angles[i] > servo_angles[i]:
                    servo_angles[i] += step
                else:
                    servo_angles[i] -= step
                move_servo(i, servo_angles[i])
        sleep(delay)

# ---- Define poses ---- #
stand_pose   = [90, 90, 120, 75, 120, 60, 110, 65]
sit_pose     = [180, 0, 120, 75, 120, 60, 110, 65]
sleep_pose   = [180, 0, 180, 0, 90, 90, 90, 80]
work_pose    = [90, 90, 120, 75, 120, 60, 110, 65]

# ---- MAIN LOOP ---- #
while True:
    # ---- 1. Handshake sequence ---- #
    print("Starting handshake...")
    move_servos_smooth(sit_pose)
    sleep(1)

    # Handshake motion for 5 seconds
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:
        # Hand up
        handshake_up = [180, 0, 180, 75, 110, 70, 150, 65]
        move_servos_smooth(handshake_up, step=5, delay=0.01)
        sleep(0.3)

        # Hand down
        handshake_down = [180, 0, 140, 75, 110, 70, 150, 65]
        move_servos_smooth(handshake_down, step=5, delay=0.01)
        sleep(0.3)
    sleep(1)

    # ---- 2. Pose sequence ---- #
    print("Performing pose sequence...")
    move_servos_smooth(stand_pose)
    sleep(3)
    move_servos_smooth(sit_pose)
    sleep(3)
    move_servos_smooth(sleep_pose)
    sleep(3)
    move_servos_smooth(work_pose)
    sleep(3)

    # ---- 3. Walking loop (20 seconds only) ---- #
    print("Walking for 20 seconds...")
    walk_start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), walk_start) < 20000:
        # Left forward
        left_forward = [90, 110, 120, 50, 120, 60, 90, 85]
        move_servos_smooth(left_forward, step=4, delay=0.01)
        sleep(0.5)

        # Right forward
        right_forward = [70, 90, 140, 75, 120, 60, 90, 85]
        move_servos_smooth(right_forward, step=4, delay=0.01)
        sleep(0.5)

    print("Restarting sequence...\n")
    sleep(2)
