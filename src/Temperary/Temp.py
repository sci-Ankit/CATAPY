import numpy

Position = [[0.00,0.00,1.09],[0.000,0.000,2.18], [0.000,0.5000,3.045],[0.000, -0.5000, 3.045]]
array = numpy.array(Position)

print("This is the position list --> \n",Position)
print("This is the position array --> \n" ,array)

Lattice_Vector =     [[12.6399964754730050,   -0.0000000000028464,    0.0000000000000000],
   [ -6.3199982376890382,   10.9465580514719729,    0.0000000000000000],
    [0.0000000000000000,    0.0000000000000000,   26.0339990876784100]]

lattice_direction = numpy.array(Lattice_Vector)
print("This is the lattice direction --> \n" ,lattice_direction)

inverse_direction = numpy.linalg.inv(lattice_direction)
print("This is the lattice direction --> \n" ,inverse_direction)
