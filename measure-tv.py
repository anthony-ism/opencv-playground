import grabcut
import blacktowhite
import draw

output = grabcut.grabcut("/Users/anthony/opencv/orignal.jpg")
output = blacktowhite.blacktowhite()
output = draw.draw();
print "hello"
