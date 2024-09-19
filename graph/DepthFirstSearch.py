from node import Node
from icecream import ic
from graph import Graph
from vertics import Vertics
from BaseStack import BaseStack

# ic.enable()


class Dfs(Graph):
    def __init__(self, numOfVertics) -> None:
        super().__init__(numOfVertics)
        self.visitInfo = dict()
        for v in Vertics:
            if v.value >= numOfVertics:
                break

            self.visitInfo[v] = False

    def print(self):
        super().print()
        print(self.visitInfo)

    def visitVertex(self, visitV):
        if self.visitInfo[visitV] is False:
            self.visitInfo[visitV] = True
            print(f"visit: {visitV}")
            return True

        return False

    def showVertex(self, startV):
        visitV = startV
        stack = BaseStack()

        self.visitVertex(visitV)
        stack.push(visitV)

        nextV = Node()
        vertics = self.dict[visitV]

        while vertics.first(nextV) is True:
            visitflag = False

            if self.visitVertex(nextV.data) is True:
                stack.push(nextV.data)
                visitV = nextV.data
                visitflag = True
            else:
                while vertics.next(nextV) is True:
                    if self.visitVertex(nextV.data) is True:
                        stack.push(nextV.data)
                        visitV = nextV.data
                        visitflag = True
                        break

            if visitflag == False:
                if stack.isEmpty() == True:
                    break
                else:
                    visitV = stack.pop()

        for k in self.visitInfo.keys():
            self.visitInfo[k] = False


if __name__ == "__main__":
    dfs = Dfs(4)
    dfs.addEdge(Vertics.A, Vertics.B)
    dfs.addEdge(Vertics.A, Vertics.D)
    dfs.addEdge(Vertics.B, Vertics.C)
    dfs.addEdge(Vertics.C, Vertics.D)
    dfs.showVertex(Vertics.A)
