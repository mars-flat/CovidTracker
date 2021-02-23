import discord
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

async def createGraph(xCoords, yCoords, earliestDate):
  plt.plot(xCoords, yCoords)
  return plt
