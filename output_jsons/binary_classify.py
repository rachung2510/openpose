import json
from math import pi, sqrt, acos, degrees, atan
import numpy as np
import matplotlib.pyplot as plt

# find angle between two points (-pi to pi rads)
def angle(ref, point):
    x = point[0] - ref[0]
    y = point[1] - ref[1]

    if not x:
        return pi/2 if y>0 else -pi/2
        
    angle = atan(y/x)
    if x<0 and y>0: # 2nd quadrant
        angle += pi
    elif x<0 and y<0: # 3rd quadrant
        angle -= pi
    return angle

##--------------------MAIN-----------------------##
# load data
f = open(filename, 'r')
content = f.read()
a = json.loads(content)
f.close()
data = a['people'][0]['pose_keypoints_2d']

# normalize
coords = np.array([[data[i*3],-data[i*3+1]] for i in range(25)]) # (0,0) is at top left
coords -= coords[0] # center around point 0
coords /= max(abs(coords[:,1])) # normalize

# classify
thetaL = degrees(angle(coords[9], coords[10]))
thetaR = degrees(angle(coords[12], coords[13]))
print(thetaL, thetaR)
if (thetaL>=-85 or thetaL<=-95) (thetaR>=-85 or thetaR<=-95):
    print("Pose: sitting")
else:
    print("Pose: standing")

# plot
plt.scatter(coords[:,0], coords[:,1],marker='.')
for i in range(25):
    plt.annotate(str(i), (coords[i][0],coords[i][1]))
plt.xlim(-0.5,0.5)
plt.show()


