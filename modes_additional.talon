^special powerpoint mode$:
    mode.enable("user.powerpoint") 
    mode.disable("command")
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2025-08-11_16.29.14.004482.png", 0)
    sleep(0.05)
    mouse_click(0)
    sleep(0.05)
    user.mouse_helper_position_restore()

^powerpoint mode$:
    mode.enable("user.powerpoint") 
    mode.disable("command")
    