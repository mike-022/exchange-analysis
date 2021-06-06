
<h1>Exchange Analysis</h1>
<div>
Scripts and Jupyter Notebooks for analysis of exchange data from Coinbase, can be extendable to any applicable exchange. <br> <br>This repo contains:<br>

1. Scripts to query current tickers of product offerings from coinbase.
2. Scripts to pull data from coinbase's public api for a range of data points for any of the available tickers.
3. Ability to load these data points into a OHLCV dataframe to plot candlestick charts.
4. CSV Export.
5. Techincal analysis using the talib library. Including candlestick pattern recogition and momentum indicators, etc.
</div>

<h3>Installation</h3>

<h4>1. Download Miniconda or Anaconda. We need conda for running the TA-Lib library which will be unable to compile without it.</h4>
<h4>2. Install TA-Lib dependencies.</h4>

  
<h4>3. Create the environment and install dependencies</h4>

```
conda create --name marketanalysis
conda activate marketanalysis
```

These dependencies need the conda forge channel to be installed

```
conda install -c conda-forge ipykernel
conda install -c conda-forge TA-Lib
```

```
After TA-Lib is installed to your conda environment through -> conda install -c conda-forge TA-Lib
Install: https://mrjbq7.github.io/ta-lib/install.html
Guide: https://blog.quantinsti.com/install-ta-lib-python/

Steps outlined in the guide:
Dependencies
To use TA-Lib for python, you need to have the TA-Lib already installed:

Mac OS X
$ brew install ta-lib

Windows
Download ta-lib-0.4.0-msvc.zip and unzip to C:\ta-lib

Linux
Download ta-lib-0.4.0-src.tar.gz and:

$ untar and cd
$ ./configure --prefix=/usr
$ make
$ sudo make install
```

<br>

Installing all other dependencies
```
pip install -r requirements.txt
```
  
This command will add our conda environment to the ipykernel if you are running through jupyter notebook

```
python -m ipykernel install --user --name=marketanalysis
```
  
<h4>4. <i>Run in terminal:</i> ```jupyter notebook```</h4>



<h3>Without jupyter notebook:</h3><br>
<i>For TA: </i> ```python run_techincal_analysis.python```

<i>For Chart generation and export: </i>```python generate_candlestick_and_export.py```
  

Resources: TA-Lib: Python library for analysis of metrics

https://mrjbq7.github.io/ta-lib/doc_index.html