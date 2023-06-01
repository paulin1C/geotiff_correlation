import sys, math
import geotiff

class Correlation:
    def __init__(self):
        self.n = 0
        self.sum_xy = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_xsq = 0
        self.sum_ysq = 0

    def add_values(self, x,y):
        self.n += 1
        self.sum_xy += x + y
        self.sum_x += x
        self.sum_y += y
        self.sum_xsq += x**2
        self.sum_ysq += y**2

    def calculate(self):
        sd_x = self.n * self.sum_xsq - self.sum_x**2
        sd_y = self.n * self.sum_ysq - self.sum_y**2
        return (self.n * self.sum_xy - self.sum_x * self.sum_y) / math.sqrt(sd_x * sd_y)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        imageA = geotiff.GeoTiff(sys.argv[1])
        imageB = geotiff.GeoTiff(sys.argv[2])

        if not imageA.tif_shape == imageB.tif_shape:
            raise ValueError("please provide images with similar resolution")

        dataA = imageA.read()
        dataB = imageB.read()

        c = Correlation()

        a_nan = 0
        b_nan = 0
        both_nan = 0

        for x in range(imageA.tif_shape[0])[1000:1500]:
            for y in range(imageA.tif_shape[1])[1000:1500]:
                a_valid = not math.isnan(dataA[x,y])
                b_valid = not math.isnan(dataB[x,y])
                if a_valid and b_valid:
                    c.add_values(dataA[x,y], dataB[x,y])
                elif (not a_valid) and (not b_valid):
                    both_nan += 1
                elif not a_valid:
                    a_nan += 1
                elif not b_valid:
                    b_nan += 1

        print("both_nan", both_nan)
        print("a_nan", a_nan)
        print("b_nan", b_nan)
        print("corr", c.calculate())

    else:
        raise TypeError("please provide two images")
    
    
