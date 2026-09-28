import pyray as pr
import math as mt

#init screen
screen_width = 1000
screen_height = 600
pr.init_window(screen_width, screen_height, "Fly-in")

camera = pr.Camera2D([0])
camera.zoom = 1.00

pr.set_target_fps(60)

#define default font
text = "Fly-in"
font_size = 80
font = pr.get_font_default()

#define default colors
green = pr.Color(57, 125, 39, 255)
black = pr.Color(48, 51, 51, 255)
border = 5
c_font_size = 20

#grid style
grid_grey = pr.Color(212, 212, 212, 255)
cell_size = 200


def draw_circle_bp(name, x, y, color, radius):
    x_pos = (x + 1) * 200
    y_pos = (y + 1) * 200
    c_text_width = pr.measure_text_ex(font, name, c_font_size, 1)
    x_c_text = int(x_pos - c_text_width.x / 2)
    y_c_text = int(y_pos - c_text_width.y / 2)

    pr.draw_circle_v(pr.Vector2(x_pos, y_pos), radius - border, color)
    pr.draw_ring(pr.Vector2(x_pos, y_pos), radius - border,
                 radius, 0, 360.0, 0, black)
    pr.draw_text_ex(font, name, pr.Vector2(x_c_text, y_c_text),
                    20, 1, pr.WHITE)


while not pr.window_should_close():
    wheel = pr.get_mouse_wheel_move()
    if wheel != 0:
        scale = 0.25 * wheel
        camera.zoom = pr.clamp(mt.exp(mt.log(camera.zoom)+scale), 0.125, 64.0)

    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    pr.begin_mode_2d(camera)
    for x in range(0, 20000, cell_size):
        pr.draw_line(x, 0, x, 20000, grid_grey)

    for y in range(0, 20000, cell_size):
        pr.draw_line(0, y, 20000, y, grid_grey)

    pr.draw_line_ex(pr.Vector2(200, 200), pr.Vector2(400, 200), 5.0, black)
    draw_circle_bp("start", 0, 0, green, 75)
    draw_circle_bp("waypoint1", 1, 0, pr.BLUE, 50)
    draw_circle_bp("waypoint2", 2, 0, pr.BLUE, 50)
    draw_circle_bp("goal", 3, 0, pr.RED, 75)

    text_width = pr.measure_text_ex(font, text, font_size, 1)
    x_pos = int(screen_width / 2 - text_width.x / 2)
    y_pos = int(screen_height / 2 - text_width.y / 2)
    pr.draw_text_ex(font, text, pr.Vector2(x_pos, y_pos),
                    font_size, 1, black)
    pr.end_mode_2d()

    pr.end_drawing()
pr.close_window()
