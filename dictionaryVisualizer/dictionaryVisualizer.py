import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib.pyplot import figure as fig
import string
import re
import scipy

good_chars = string.ascii_lowercase + " "
good_chars = set(good_chars)

regex_pattern = r"\(.*?\)"

def clean_string(s):
    s = s.lower()
    filtered_string = ''.join(filter(lambda x: x in good_chars, s))
    return filtered_string


def words(s):
    return s.split()

# before = "To relinquish all claim to; -- used when an insured person gives up to underwriters all claim to the property covered by a policy, which may remain after loss or damage by a peril insured against.\""
# after = clean_string(before)
# print(words(after))


a = open("files/realA.txt").read().strip().split("\n\n")
G = nx.Graph()
for line in tqdm(a[:30]):
    splitted = re.split(regex_pattern, line, 1)
    word = words(clean_string(splitted[0]))[0]
    definition = words(clean_string(splitted[1]))
    for w in definition:
        G.add_edge(word, w)
# nx.draw(G, with_labels=True, nodesize=2)
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx_edges(G, pos, alpha=0.3, width=1, edge_color="m")
print("edges done")
nx.draw_networkx_nodes(G, pos, node_size=20, node_color="#210070", alpha=0.2)
print("nodes done")

# get a list of nodes sorted by their outgoing edge counts
nodes_sorted = sorted(G.nodes(), key=lambda node: G.degree(node), reverse=True)

# select the top 20% of nodes with the most outgoing edges
top_nodes = nodes_sorted[:int(len(nodes_sorted) * 0.9)]
labels = {node: node for node in top_nodes}
nx.draw_networkx_labels(G, pos, font_size=8, labels=labels)
print("labels done")

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(30.5, 30.5, forward=True)

# print(G.)

# G = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
#
plt.show()
