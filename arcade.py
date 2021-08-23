import arcade

screen_width = 200
screen_hight = 200

arcade.open_window(SCREEN_WIDHT, SCREEN_HIGHT, "Drawing example")

arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, aracde.color.YELLOW)

x = 370
y = 350
radius = 20

aracde.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

sh_render()

arcade.run()
