# geotiff_correlation
simply python script to calculate the pearson correlation coefficient between two geotiff files
## dependencies
the required packages can be installed with ```pip install -r requirements.txt --user```
## usage
get perason correlation between two images
```python main.py corr layerA.tif layerB.tif```
plot values
```python main.py plot layerA.tif layerB.tif```
## sample output
```
corr -0.012670411044346559 # pearson correlation coefficent
```
