import colorgram
colors = colorgram.extract('hirst.jpg', 30)
color_list=[]
for i in range(30):
    first_color = colors[i]
    rgb = first_color.rgb
    r = rgb.r
    g=rgb.g
    b=rgb.b
    rgb_tuple=(r, g, b)
    color_list.append(rgb_tuple)
print(color_list)
