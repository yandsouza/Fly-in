import pyray as pr

screen_width = 750
screen_height = 500
pr.init_window(screen_width, screen_height, "Fly-in")

text = "Fly-in"
font_size = 80
font = pr.get_font_default()

green = pr.Color(57, 125, 39, 255)
black = pr.Color(48, 51, 51, 255)
border = 3.75
c_text_start = "start"
c_font_size = 20

grid_grey = pr.Color(212, 212, 212, 255)
cell_size = 50

text_width = pr.measure_text_ex(font, text, font_size, 1)
x_pos = int(screen_width / 2 - text_width.x / 2)
y_pos = int(screen_height / 2 - text_width.y / 2)

c_text_width = pr.measure_text_ex(font, c_text_start, c_font_size, 1)
x_c_text = int(100 / 2 - c_text_width.x / 2)
y_c_text = int(100 / 2 - c_text_width.y / 2)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    for x in range(0, screen_width, cell_size):
        pr.draw_line(x, 0, x, screen_height, grid_grey)

    for y in range(0, screen_height, cell_size):
        pr.draw_line(0, y, screen_width, y, grid_grey)

    pr.draw_circle_v(pr.Vector2(50, 50), 50 - border, green)
    pr.draw_ring(pr.Vector2(50, 50), 50 - border, 50, 0, 360.0, 0, black)
    pr.draw_text_ex(font, "start", pr.Vector2(x_c_text, y_c_text),
                    20, 1, pr.WHITE)

    pr.draw_text_ex(font, text, pr.Vector2(x_pos, y_pos),
                    font_size, 1, pr.BLUE)

    pr.end_drawing()
pr.close_window()
