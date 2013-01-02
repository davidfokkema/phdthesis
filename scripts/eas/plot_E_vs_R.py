from artist import GraphArtist

E = [1e15, 1e16, 1e17, 1e18]
R = [20, 73, 208, 443]

graph = GraphArtist('semilogy')
graph.plot(R, E, mark=None, linestyle='smooth')
graph.set_xlabel(r"Core distance [\si{\meter}]")
graph.set_ylabel(r"Primary energy [\si{\electronvolt}]")
graph.set_xlimits(min=0)
graph.save('energy-distance')
