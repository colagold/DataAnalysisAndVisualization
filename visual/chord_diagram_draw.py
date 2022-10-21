import pandas as pd
import holoviews as hv
from holoviews import opts, dim
from bokeh.sampledata.les_mis import data

hv.extension('bokeh')
hv.output(size=200)
links = pd.DataFrame(data['links'])
print(links.head(3))
hv.Chord(links)
nodes = hv.Dataset(pd.DataFrame(data['nodes']), 'index')
nodes.data.head()
chord = hv.Chord((links, nodes)).select(value=(5, None))
chord.opts(
    opts.Chord(cmap='Category20', edge_cmap='Category20', edge_color=dim('source').str(),
               labels='name', node_color=dim('index').str()))
hv.save(chord,r'output.html') # 将结果保存到网页，不知道为啥网页出不来
