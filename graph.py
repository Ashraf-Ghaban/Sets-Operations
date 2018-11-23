import matplotlib.pyplot as plt
import networkx as nx


G=nx.Graph()


def build_graph():
    while True:
        ikey = input("Enter vertices (or Enter to quit): \n")
        if not ikey:
            break
        G.add_node(ikey)
    show_graph()


def show_graph():
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='g')
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=1, alpha=0.7, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, font_size=10, font_family='sans-serif', edge_labels=labels)

    plt.axis('off')
    plt.show()


def is_graph_direct(G):
    direct = G.is_directed()
    if direct == True:  print("The Graph is Direct")
    else:   print("The Graph is not Direct")


def is_node_adjacent(v,u):
    if G.has_edge(v,u): print("Vertices " + v + " and " + u + " are  adjacent")
    else:   print("Vertices " + v + " and " + u + " are not adjacent")

def node_neighbors(v):
    print(G[v])


def add_vertex(v):
    G.add_node(v)
    show_graph()


def remove_vertex(v):
    G.remove_node(v)
    show_graph()


def add_edge(v, u):
    G.add_edge(v,u)
    show_graph()


def add_weighted_edge(v,u,w):
    G.add_edge(v,u,weight=w)
    show_graph()


def remove_edge(v,u):
    G.remove_edge(v,u)
    show_graph()


def get_edge_weight(v,u):
    print(G.get_edge_data(v,u))


def set_edge_weight(v,u,w):
    G.add_edge(v,u,weight=w)
    show_graph()


def clear_graph():
    G.clear()
    show_graph()


def number_of_vertices():
        print("The number of vertices in the graph is:  " + str(G.number_of_nodes()))


def number_of_edges():
    print("The number of edges in the graph is:  " + str(G.number_of_edges()))


def is_graph_empty():
    if number_of_vertices() == 0:  print("The graph is empty")
    else:   print("The graph is not empty")

def is_graph_complete():
   if nx.is_connected(G):   print("The graph is complete")
   else:    print("The graph is not complete")


def list_vertices():
    print(list(G.nodes))


def list_edges():
    print(list(G.edges))


def vertex_degree():
    print(G.degree[input("Please enter a vertex: \n")])


def graph_size():
    print(G.size())


def vertex_exist():
    if G.has_node(input("Please enter a vertex: \n")):  print("The vertex exist in the graph")
    else:   print("The vertex does not exist in the graph")


def print_graph():
    for (u, v, wt) in G.edges.data('weight'):
        print('(%s, %s, %d)' % (u, v, wt))
    show_graph()


while True:
    try:

        print("\n")
        print("Please select from the options below:  \n")
        print("1. Question I")
        print("2. Question II")
        print("3. Exit \n\n")

        opt_key = int(input())


        #   *** Question I ***

        if opt_key == 1:

                if G.number_of_nodes() == 0:
                    yn=int(input("Do you want to build an intitial graph (yes = 1, no = 0)"))
                    if yn == 1: build_graph()

                print("\n")
                print("Please select the graph operation:  \n")
                print("1.  Digraph Check")
                print("2.  adjacent Check")
                print("3.  Vertex Neighbors")
                print("4.  Add Vertex")
                print("5.  Remove Vertex")
                print("6.  Add Edge")
                print("7.  Remove Edge")
                print("8.  Add Weighted Edge")
                print("9.  Get Wieght")
                print("10. Set Weight")
                print("11. Empty Check")
                print("12. Complete Check")
                print("13. Vertices and Edges List")
                print("14. Vertex Degree")
                print("15. Graph Size")
                print("16. Number of Vertices")
                print("17. Number of Edges")
                print("18. Clear Graph")
                print("19. Vertex Exist Check")
                print("20. Print Graph")
                print("21. Exit")

                print("\n")

                opt_key = int(input())

                if opt_key == 1:
                    is_graph_direct(G)

                elif opt_key == 2:
                    is_node_adjacent(input("Input the first vertex: \n"), input("Input the second vertex: \n"))

                elif opt_key == 3:
                    node_neighbors(input("Please enter vertex: \n"))

                elif opt_key == 4:
                    add_vertex(input("Please enter a vertex to add: \n"))

                elif opt_key == 5:
                    remove_vertex(input("Please enter a vertex to remove: \n"))

                elif opt_key == 6:
                    add_edge(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"))

                elif opt_key == 7:
                    remove_edge(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"))

                elif opt_key == 8:
                    add_weighted_edge(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"),
                                      int(input("Please enter the edge weight: \n")))
                elif opt_key == 9:
                    get_edge_weight(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"))

                elif opt_key == 10:
                    set_edge_weight(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"),
                                      int(input("Please enter the edge weight: \n")))

                elif opt_key == 11:
                    is_graph_empty()

                elif opt_key == 12:
                    is_graph_complete()

                elif opt_key == 13:
                    list_vertices()
                    list_edges()

                elif opt_key == 14:
                    vertex_degree()

                elif opt_key == 15:
                    graph_size()

                elif opt_key == 16:
                    number_of_vertices()

                elif opt_key == 17:
                    number_of_edges()

                elif opt_key == 18:
                    clear_graph()

                elif opt_key == 19:
                    vertex_exist()

                elif opt_key == 20:
                    print_graph()

                elif opt_key == 21:
                    exit()

                else:
                    print ("Please enter a valid option")


        #            *** Question II ***

        elif opt_key == 2:

            G = nx.read_edgelist('graph.txt', nodetype=str, data=(('weight', int),))

            print("\n")
            print("Please select the graph operation:  \n")
            print("1.  Remove Vertex")
            print("2.  Complete Check")
            print("3.  Number of Edges")
            print("4.  Ckeck Link ('a' to 'f')")
            print("5.  Print Edge Weight ('b' to 'h')")
            print("6.  Print Vertex Degree (c)")
            print("7.  Number of Vertices")
            print("8.  Add Vertex (k)")
            print("9.  Add Weighted Edge ('k','a',5)")
            print("10. Add Weighted Edge ('g','k',2)")
            print("11. Set Weight('a','c',7)")
            print("12. Print Graph")
            print("\n")

            opt_key = int(input())

            if opt_key == 1:
                remove_vertex(input("Please enter a vertex to remove: \n"))

            elif opt_key == 2:
                is_graph_complete()

            elif opt_key == 3:
                number_of_edges()

            elif opt_key == 4:
                is_node_adjacent(input("Input the first vertex: \n"), input("Input the second vertex: \n"))

            elif opt_key == 5:
                get_edge_weight(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"))

            elif opt_key == 6:
                vertex_degree()

            elif opt_key == 7:
                number_of_vertices()

            elif opt_key == 8:
                add_vertex(input("Please enter a vertex 'k' or any other to add: \n"))

            elif opt_key == 9:
                add_weighted_edge(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"),
                                  int(input("Please enter the edge weight: \n")))

            elif opt_key == 10:
                add_weighted_edge(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"),
                                  int(input("Please enter the edge weight: \n")))

            elif opt_key == 11:
                set_edge_weight(input("Please enter the start vertex: \n"), input("Please enter the end vertex: \n"),
                                int(input("Please enter the edge weight: \n")))

            elif opt_key == 12:
                print_graph()


            else:
                print("Please enter a valid options")


        else:
            exit()

    except KeyboardInterrupt:
        exit()