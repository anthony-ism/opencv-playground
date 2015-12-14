'''
This is how to track a white ball example using SimpleCV
The parameters may need to be adjusted to match the RGB color
of your object.
The demo video can be found at:
http://www.youtube.com/watch?v=jihxqg3kr-g
'''
print __doc__

import SimpleCV

display = SimpleCV.Display()
cam = SimpleCV.Camera()
normaldisplay = True

while display.isNotDone():

	if display.mouseRight:
		normaldisplay = not(normaldisplay)
		print "Display Mode:", "Normal" if normaldisplay else "Segmented"

	img = cam.getImage().flipHorizontal()
	dist = img.colorDistance(SimpleCV.Color.WHITE).dilate(2)
	segmented = dist.stretch(10,255)
	blobs = segmented.findBlobs()
	for b in blobs:
		img.drawRectangle(b._mMaxX, b._mMaxY, b._mWidth, b._mHeight);

	if normaldisplay:
		img.show()
	else:
		segmented.show()
