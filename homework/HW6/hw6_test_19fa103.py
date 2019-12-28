# 19fa103; john k johnstone; jkj at uab dot edu; mit license

import hw6_19fa103 as hw6

# this is only a start at testing the class: add more calls to debug

sq = hw6.Pol ([(0.,0.), (1.,0.), (1.,1.), (0.,1.)]) 
print ('polygon:', sq)
print ('perimeter:', sq.perimeter())
print ('avgEdgeLength:', sq.avgEdgeLength())
print ('angle:', sq.angle(0))
print ('isSimple:', sq.isSimple())

print()
sq = hw6.Pol ([(0,0), (5,3), (5,0), (0,3), (0,0)])
print ('complex polygon:', sq)
print ('isSimple:', sq.isSimple())

print()
t = hw6.Tri ((0.,0.),
             (1.,0.),
             (.5, 1.),
             (179, 27, 27),
             (30, 107, 82),
             (244, 195,0))

print ('triangle:', t)
print ('getColour:', t.getColour(1))
print ('isEquilateral:', t.isEquilateral(1))
print ('signed area:', t.signedArea())
print ('orientation:', 'ccw' if t.isCCW() else 'cw')
print ('angles:', t.angle(0), t.angle(1), t.angle(2))
print ('perimeter:', t.perimeter())
print ('avgEdgeLength:', t.avgEdgeLength())
print ('centroid:', t.centroid())
print ('circumCenter:', t.circumCenter())
