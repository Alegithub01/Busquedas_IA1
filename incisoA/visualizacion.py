import matplotlib.pyplot as plt
import networkx as nx

def visualizar_mapa(G, colores, coloreo):
    pos = nx.spring_layout(G)

    # Dibujar el mapa inicial
    node_colors = [G.nodes[node]['color'] for node in G.nodes]
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Mapa Inicial')
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=12, font_weight='bold')

    # Dibujar el mapa final
    plt.subplot(1, 2, 2)
    plt.title('Mapa Final')
    node_colors_final = [coloreo[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors_final, node_size=800, font_size=12, font_weight='bold')

    plt.tight_layout()
    plt.show()
