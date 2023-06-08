import sys, math
import geotiff
import matplotlib.pyplot as plt

class ImageHandler:
    def __init__(self, pathA, pathB):
        self.imageA = geotiff.GeoTiff(pathA)
        self.imageB = geotiff.GeoTiff(pathB)

        if not self.imageA.tif_shape == self.imageB.tif_shape:
            raise ValueError("please provide images with similar resolution")

        self.dataA = self.imageA.read()
        self.dataB = self.imageB.read()

    def map(self, func):
        self.a_nan = 0
        self.b_nan = 0
        self.both_nan = 0

        for x in range(self.imageA.tif_shape[0]):
            for y in range(self.imageA.tif_shape[1]):
                a_valid = not math.isnan(self.dataA[x,y])
                b_valid = not math.isnan(self.dataB[x,y])
                if a_valid and b_valid:
                    func(self.dataA[x,y], self.dataB[x,y])
                elif (not a_valid) and (not b_valid):
                    self.both_nan += 1
                elif not a_valid:
                    self.a_nan += 1
                elif not b_valid:
                    self.b_nan += 1

    def load_values(self):
        self.valuesA = []
        self.valuesB = []

        def save(x,y):
            self.valuesA.append(x)
            self.valuesB.append(y)

        self.map(save)


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
        self.sum_xy += x * y
        self.sum_x += x
        self.sum_y += y
        self.sum_xsq += x**2
        self.sum_ysq += y**2

    def calculate(self):
        sd_x = self.n * self.sum_xsq - self.sum_x**2
        sd_y = self.n * self.sum_ysq - self.sum_y**2
        return (self.n * self.sum_xy - self.sum_x * self.sum_y) / math.sqrt(sd_x * sd_y)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        handler = ImageHandler(sys.argv[2], sys.argv[3])
        if sys.argv[1] == "corr":
            c = Correlation()
            handler.map(c.add_values)
            print("corr:", c.calculate())

        elif sys.argv[1] == "plot":
            handler.load_values()
            plt.scatter(handler.valuesA, handler.valuesB, s=0.3)
            plt.show()
        else:
            raise ValueError("command must be corr or plot")

    else:
        raise ValueError("please provide a command (corr or plot) and two images\nfor example: python main.py corr a.tiff b.tiff")
    
    
