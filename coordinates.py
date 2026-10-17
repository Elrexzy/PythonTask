points = (2,3), (-1,4), (5,-6), (0,7), (-3,-2)

def postive_points(point):
      index, count = point
      return index > 0 and count > 0
            
result = filter(postive_points, points)
print(tuple(result))

#for index, count in points:
#      print(index)
#      print(count)
#
#list_points = []      
#for index, count in points:
#      list_points.append(index,count)
