import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._all_Retailer = DAO.getAllRetailer()
        self._grafo = nx.Graph()
        self._idMap = {}
        for ret in self._all_Retailer:
            self._idMap[ret.Retailer_code] = ret

    def creaGrafo(self,nazione,anno):
        nodi = DAO.getAllNodes(nazione)
        self._grafo.add_nodes_from(nodi)
        for r1 in self._grafo.nodes:
            for r2 in self._grafo.nodes:
                if r1 != r2:
                    peso = DAO.getAllEdges(anno,r1,r2)[0]
                    if peso > 0:
                        self._grafo.add_edge(r1,r2,weight=peso)
        print(self._grafo)



    def get_IdMap(self):
        return self._idMap
