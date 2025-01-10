import pandas
import matplotlib.pyplot as plt
import plotly.graph_objs as go
print("all packages have been installed successfully")

cities = ["austin", "dallas", "houston", "san antonio", "el paso"]
developercounts = [20000,10000,15000,8000,6000,6000]

fig, axs = plt.subplots()

axs.bar(cities, developercounts)
plt.savefig("/Users/ahmzuberiashraf/Desktop/pythonworkshop/barchart.png")
