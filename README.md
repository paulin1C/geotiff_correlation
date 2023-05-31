# geotiff_correlation
simply python script to calculate the pearson correlation coefficient between two geotiff files
## dependncies
the required packages can be installed with ```pip install -r requirements.txt --user```
## usage
```python main.py layerA.tif layerB.tif```
## sample output
```
both_nan 14968278 # pixels where both layers are nan ("not a number")
a_nan 1653 # pixels where only layerA is nan
b_nan 16794688 # pixels where only layerB is nan
corr -0.012670411044346559 # pearson correlation coefficent
```
