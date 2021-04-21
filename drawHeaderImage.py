import random
import drawBot as db
import os

db.newDrawing()

background_images = os.listdir('img/tiles-copy/')
background_image_paths = []
for background_image in background_images:
    background_image_paths.append('img/tiles-copy/' + background_image)
# print(background_image_paths)

db.newPage(1240, 496)

tileSize = 124
images = [['i' for i in range(4)] for j in range(10)]

srcWidth, srcHeight = db.imageSize(background_image_paths[0])
dstWidth, dstHeight = tileSize, tileSize
factorWidth  = dstWidth  / srcWidth
factorHeight = dstHeight / srcHeight
for x in range(0, 1240, tileSize):
    for y in range(0, 496, tileSize):
        with db.savedState():
            stepX = int(x/tileSize)
            stepY = int(y/tileSize)
            validPath = False
            while not validPath:
                path = random.choice(background_image_paths)
                if(stepX > 0):
                    if(images[stepX-1][stepY] == path):
                        continue
                if(stepY > 0):
                    if(images[stepX][stepY-1] == path):
                        continue
                validPath = True
            db.translate(x, y)
            db.scale(factorWidth, factorHeight)
            db.image(path, (0, 0) )
            images[int(x/tileSize)][int(y/tileSize)] = path

db.saveImage('img/header.png')

# srcWidth, srcHeight = db.imageSize(background_image_path)
# dstWidth, dstHeight = canvasWidth, canvasHeight
# factorWidth  = dstWidth  / srcWidth
# factorHeight = dstHeight / srcHeight
# with db.savedState():
#     db.scale(factorWidth, factorHeight)
#     db.image(background_image_path, (0, 0))

db.endDrawing()