from vector import Vector

w = 3
h = 2
maxval = 255
red = Vector(1.,0.,0.)
green = Vector(0.,1.,0.)
blue = Vector(0.,0.,1.)
yellow = red + green
white = red + green + blue
black = red * 0.001

colors = [red, green, blue, yellow, white, black]

f = open("imgex.ppm",'w')
if f.writable():
    f.write("P3 "+str(w)+" "+str(h)+"\n")
    f.write(str(maxval)+"\n")
    for i in range(h):
        for j in range(w):
            f.write(str(round(maxval*colors[w*i+j].x))+"\t")
            f.write(str(round(maxval*colors[w*i+j].y))+"\t")
            f.write(str(round(maxval*colors[w*i+j].z))+"\t")
        f.write("\n")

f.close()
