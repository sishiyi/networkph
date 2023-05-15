import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 读取化合物、靶蛋白和药物-靶蛋白相互作用数据
compounds = pd.read_csv('/path/to/compounds.csv')
proteins = pd.read_csv('/path/to/proteins.csv')
interactions = pd.read_csv('/path/to/interactions.csv')

# 创建化合物-靶蛋白关系网络
G = nx.Graph()

# 添加化合物节点
for compound in compounds.itertuples(index=False):
    G.add_node(compound.compound_id, **{'name': compound.compound_name, 'type': 'compound'})

# 添加靶蛋白节点
for protein in proteins.itertuples(index=False):
    G.add_node(protein.protein_id, **{'name': protein.protein_name, 'type': 'protein'})

# 添加药物-靶蛋白相互作用边
for interaction in interactions.itertuples(index=False):
    G.add_edge(interaction.compound_id, interaction.protein_id, **{'type': 'interaction', 'strength': interaction.strength})

# 绘制网络图
nx.draw(G, with_labels=True)
plt.show()
