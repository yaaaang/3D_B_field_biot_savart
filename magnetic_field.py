"""
This is a code to generate and visualize the 3-D magnetic field generated by either circular coils, straight coils or
any combinations of the two types of coils, with constant current flowing inside.

Note the volume of the coils is neglected.

Here we need numpy, mayavi.

The basic theory is based on Biot-Savart's Law.
Author: Y. Zhang
2018 - 05 -14
"""

from coil import circle_coil, straight_line, np
from biot_savart import biot_savart
from draw_coil import draw_coil, mlab

c01 = [0, 1, 0]                         # center of the 1st circle
c02 = [0, -1, 0]                        # center of the 2ed circle
end_points = [[0, -5, 0], [0, 5, 0]]    # end points of the straight wire
nr = [0, 1, 0]                          # the normal vector of the c1,c2 coil and the line coil
Rc = 1                                  # the radius of the c1,c2 coil
nc = 200                                # division num. of the coils
Ic = 1000                               # current flowing inside of the coil

# space grid
ls = 2
nrs = 50
x, y, z = np.mgrid[-2:2:10j, -2:2:10j, -2:2:10j]
r = np.c_[np.ravel(x), np.ravel(y), np.ravel(z)]

rc1, dl1 = circle_coil(c01, nr, Rc, nc)
rc2, dl2 = circle_coil(c02, nr, Rc, nc)
rc3, dl3 = straight_line(end_points, nr, 10)
Bx1, By1, Bz1 = biot_savart(r, rc1, Ic, dl1)
Bx2, By2, Bz2 = biot_savart(r, rc2, Ic, dl2)
Bx3, By3, Bz3 = biot_savart(r, rc3, Ic, dl3)

Bx = Bx1 + Bx2 + Bx3
By = By1 + By2 + By3
Bz = Bz1 + Bz2 + Bz3

# Visualisation
coil_color = (0, 0, 0)
mlab.figure(bgcolor=(1., 1., 1.), fgcolor=(1., 1., 1.), size=(640, 480))
# draw the coils
draw_coil(rc1, coil_color)
draw_coil(rc2, coil_color)
draw_coil(rc3, coil_color)
# draw the vector field
mlab.quiver3d(x, y, z, Bx, By, Bz, line_width=3)
# field lines
mlab.flow(x, y, z, Bx, By, Bz)
mlab.show()