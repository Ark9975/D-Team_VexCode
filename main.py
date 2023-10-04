#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_36_1, True)
left_motor_b = Motor(Ports.PORT1, GearSetting.RATIO_36_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_36_1, False)
right_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_36_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 0.6111111111111112)
intake_motor_a = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
intake_motor_b = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
intake = MotorGroup(intake_motor_a, intake_motor_b)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")



# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3 + axis1
            # right = axis3 - axis1
            drivetrain_left_side_speed = controller_1.axis3.position() + controller_1.axis1.position()
            drivetrain_right_side_speed = controller_1.axis3.position() - controller_1.axis1.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project: Ali's Test 1
#	Author: Ali Khan
#	Created: 10/2/23
#	Configuration:
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

def pre_autonomous():
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def Intake(): # intake control
    intake.set_velocity(69, PERCENT)
    if controller_1.buttonR2.pressing():
        intake.spin(FORWARD)
    elif controller_1.buttonR1.pressing():
        intake.spin(REVERSE)
    else:
        intake.stop()

def motion(): # drivetrain movement
    drivetrain.set_drive_velocity(75, PERCENT)

    if controller_1.axis3.position() > 0:
        drivetrain.drive(FORWARD)
    elif controller_1.axis3.position() < 0:
        drivetrain.drive(REVERSE)
    else:
        drivetrain.stop()

def turning():
    if controller_1.axis1.position() > 0:
        drivetrain.turn(LEFT)
    elif controller_1.axis1.position() < 0:
        drivetrain.turn(RIGHT)
    else:
        drivetrain.stop()

def speed(): # Setting drivetrain speed
    if controller_1.buttonA.pressed:
        drivetrain.set_drive_velocity(70, PERCENT)
        controller_1.screen.print("70% Speed")
    elif controller_1.buttonB.pressed:
        drivetrain.set_drive_velocity(50, PERCENT)
        controller_1.screen.print("50% Speed")
    elif controller_1.buttonY.pressed:
        drivetrain.set_drive_velocity(30, PERCENT)
        controller_1.screen.print("30% Speed")
    elif controller_1.buttonX.pressed:
        drivetrain.set_drive_velocity(10, PERCENT)
        controller_1.screen.print("10% Speed")
    else:
        drivetrain.set_drive_velocity(100, PERCENT)
        controller_1.screen.print("100% Speed")

def user_control():
    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:
        wait(20, MSEC)
        on = True
        
        while on:
            Intake()
            #motion()
            #turning()
            #speed()

        

# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()
