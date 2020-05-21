from coordinates import Coordinate
import math
from shapely.geometry import Point, LineString
from pyproj import Geod, CRS, transform


g = Geod(ellps='WGS84')
wgs84=CRS("EPSG:4326")
UTM=CRS("EPSG:32721") # UTM 21S
Coordinate.default_order = 'yx'

def to_utm(c):
	xx,yy=transform(wgs84, UTM, c.y, c.x)
	return Coordinate(xx,yy)
def to_wgs84(c):
	xx,yy=transform(UTM, wgs84, c.x, c.y)
	return Coordinate(xx,yy)

def degree(x):
	pi=math.pi
	degree=(x*180)/pi
	return degree

def radians(x):
	pi=math.pi
	rad=(x*pi)/180
	return rad

def offset(point,angle,d):
	xx = point.x + ( d * math.cos(radians(90-angle)) )
	yy = point.y + ( d * math.sin(radians(90-angle)) )
	return Coordinate(x=xx, y=yy)

def vector(angle):
	return  math.cos(radians(90-angle)),  math.sin(radians(90-angle))

def bearing(b,a):
	dx = a.x-b.x
	dy = a.y-b.y
	bearing=90-degree(math.atan2(dy,dx))
	if bearing<0:
		bearing+=360
	return bearing

def extend(a,b):
	m = (a.y-b.y)/(a.x-b.x)
	_b= (a.x*b.y - b.x*a.y)/(a.x-b.x)
	#y=mx+b
	def ye(x):
		return m*x+_b
	return Point(a.x-10000, ye(a.x-10000)), Point(b.x+10000, ye(b.x+10000))

def toCoord(point):
	return Coordinate(x=point[0],y=point[1])
	
