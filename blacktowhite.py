from PIL import Image

def blacktowhite():
    # Separate RGB arrays
    im = Image.open(file("grabcut_output.png", 'rb'))
    R, G, B = im.convert('RGB').split()
    r = R.load()
    g = G.load()
    b = B.load()
    w, h = im.size

    # Convert non-black pixels to white
    for i in range(w):
        for j in range(h):
            if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
                r[i, j] = 255 # Just change R channel

    # Merge just the R channel as all channels
    im = Image.merge('RGB', (R, R, R))
    im.save("line-input.jpg")
    return im;
