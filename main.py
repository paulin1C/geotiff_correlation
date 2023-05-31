import numpy, sys, math
import geotiff

def cor(x,y):
    return numpy.corrcoef(x, y)[0, 1]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        imageA = geotiff.GeoTiff(sys.argv[1])
        imageB = geotiff.GeoTiff(sys.argv[2])
        if not imageA.tif_shape == imageB.tif_shape:
            raise ValueError("please provide images with similar resolution")
        dataA = imageA.read()
        dataB = imageB.read()
        valuesA = []
        valuesB = []
        a_nan = 0
        b_nan = 0
        both_nan = 0
        for x in range(imageA.tif_shape[0]):
            for y in range(imageA.tif_shape[1]):
                a_valid = not math.isnan(dataA[x,y])
                b_valid = not math.isnan(dataB[x,y])
                if a_valid and b_valid:
                    valuesA.append(dataA[x,y])
                    valuesB.append(dataB[x,y])
                elif (not a_valid) and (not b_valid):
                    both_nan += 1
                elif not a_valid:
                    a_nan += 1
                elif not b_valid:
                    b_nan += 1
        print("both_nan", both_nan)
        print("a_nan", a_nan)
        print("b_nan", b_nan)
        print("corr", cor(valuesA, valuesB))



    else:
        raise TypeError("please provide two images")
    
    
