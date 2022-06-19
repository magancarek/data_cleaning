import pandas as pd
import numpy as np
from scipy import stats
from scipy.spatial.distance import squareform, pdist

def importData(path = ''):
    df = pd.read_csv(path, sep=',')
    df = df.fillna(df.median())

    df = df.select_dtypes(include=np.number)

    return df

def getMatrixOdDistance(data):
    data = data[:40]

    matrixOfDistance = round(pd.DataFrame(squareform(pdist(data.iloc[:, 0:]))), 2)

    return matrixOfDistance


def standarizeData(data):
    outputData = data.copy(deep=True)

    for col in outputData.columns:
        outputData[col] = stats.zscore(outputData[col])

    return outputData

def normalizeData(data):
    return data / data.max()

def getMatrixOfDistanceWithMax(data):
    matrixOfDistance = round(pd.DataFrame(squareform(pdist(normalizeData(data).iloc[:, 0:]))), 2)

    return matrixOfDistance
