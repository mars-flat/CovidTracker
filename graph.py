import discord
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

async def createGraph(xCoords, yCoords, earliestDate):
  plt.plot(xCoords, yCoords)
  plt.title('Covid-19 Cases in Canada since ' + earliestDate)
  plt.xlabel('Days Since ' + earliestDate)
  plt.ylabel('Covid-19 Case Count')
  return plt
