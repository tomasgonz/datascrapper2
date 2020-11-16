import sys
sys.path.append("../")
import streamlit as st
import numpy as np
import pandas as pd

from sources import worldbank
from geo import *

import plotly.express as px
import plotly.graph_objects as go

st.title('Gender in the LDCs')

