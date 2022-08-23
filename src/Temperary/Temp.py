import numpy

Position = [[0.00,0.00,0],[0.000,0.000,1.09], [0.000,0.5000,1.955],[0.000, -0.5000, 1.955]]
array = numpy.array(Position)

print("This is the position list --> \n",Position)
print("This is the position array --> \n" ,array)

Lattice_Vector =     [[ 12.6484979403553499,   -0.0000000000026369 ,   0.0000000000000000],
   [ -6.3242489701299966,   10.9539205360290524,   -0.0000000000000000],
    [ 0.0000000000000000 ,   0.0000000000000000,   25.9990142618964022]]
       
    
    

lattice_direction = numpy.array(Lattice_Vector)
print("This is the lattice direction --> \n" ,lattice_direction)

inverse_direction = numpy.linalg.inv(lattice_direction)
print("This is the inverse direction --> \n" ,inverse_direction)

height_in_c = 1.09
unit_offset = [ 0.58333,   0.41667,   0.39304]
transform_offset= numpy.dot(unit_offset,lattice_direction)
transform_offset[2] += height_in_c

for i in range(len(array)):
    #print(i)
    #print(array[i])
    array[i] += transform_offset
    #print(array[i])

array=numpy.dot(array,inverse_direction)

for i in range(len(array)):
    print(f"{array[i][0]}   {array[i][1]}    {array[i][2]}")    

