#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import branca.colormap as cm
import src.parse_tcx as parse_tcx
import src.parse_gpx as parse_gpx
import folium
import pandas as pd
from src.maptiles import tiles
from typing import Dict, Optional, Any, Union, Tuple

to_knots = lambda mps: mps / 0.5144


def get_data(fname: str) -> Optional[pd.DataFrame]:
    if fname[-3:]=='tcx':
        _, data = parse_tcx.get_dataframe_from_tcx(fname)
    if fname[-3:]=='gpx':
        data = parse_gpx.get_dataframe_from_gpx(fname)
    return data

def cut(df: pd.DataFrame, start: str, stop: str) -> pd.DataFrame:
    df = df[(df['time'] > start)]
    df = df[(df['time'] < stop)]
    return df