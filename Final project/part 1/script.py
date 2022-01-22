import enum
import random

class Colors(enum.Enum):
   BLUE = "B"
   RED = "R"
   GREEN = "G"
   ORANGE = "O"
   PERPUL = "P"
   WHITE = "W"

class Cube:
    def __init__(self, wight,sides = [],buttomIndex=5):
        self.wight = wight
        if len(sides) == 0:
            self.sides = self.__randomColorSides()
        else:
            self.sides = sides
        self.buttomIndex = buttomIndex

    def __lt__(self, other):
        return (self.wight < other.wight)

    def __str__(self):
        return "--"+self.sides[-(self.buttomIndex+1)].value+"--   "+ str(list(map(lambda tss : tss.value ,self.sides))) +"\n"+\
               "|   |" + " : "+ str(self.wight) +"\n"+\
               "--" +self.sides[self.buttomIndex].value+"--\n"

    def __randomColorSides(self):
        listt = list((Colors.PERPUL, Colors.RED, Colors.ORANGE, Colors.BLUE , Colors.GREEN, Colors.WHITE))
        random.shuffle(listt)
        return tuple(listt)

    def GetButtomSideColer(self):
        return self.sides[self.buttomIndex]

    def GetTopSideColer(self):
        return self.sides[-(self.buttomIndex+1)]

    def putColorAtBottom(self,color):
        self.buttomIndex = self.sides.index(color)

    def putButtomIndex(self,index):
        self.buttomIndex = index



class Tower:
    def __init__(self, cubes):
        self.totalcubes = sorted(cubes)
        self.resCubes = []


    def printTower(self):
        for index in range(len(self.resCubes)-1,-1,-1):
            print(self.resCubes[index])

    def __isValidPosition(self, newcube , cubes):
        if len(cubes) == 0:
            return True
        if cubes[-1].wight > newcube.wight and newcube.GetButtomSideColer() == cubes[-1].GetTopSideColer() :
            return True
        return False

    def __copyCubeList(self,listToCopy):
        copyCubes = [Cube(0) for _ in range(len(listToCopy))]
        for index in range(len(listToCopy)):
            copyCubes[index] = Cube(listToCopy[index].wight , listToCopy[index].sides,listToCopy[index].buttomIndex)
        return copyCubes
    
    def FindOptimalSolution(self, tempCubes):
        if len(tempCubes) > len(self.resCubes):
            self.resCubes = self.__copyCubeList(tempCubes)
        if len(self.resCubes) == len(self.totalcubes):
            return
        
        for cube in self.totalcubes:
            firstIndex = cube.buttomIndex
            for buttomIndex in range(6):
                cube.putButtomIndex(buttomIndex)
                if self.__isValidPosition(cube,tempCubes):
                    #cube.putColorAtBottom(topCube.GetTopSideColer())
                    self.FindOptimalSolution(tempCubes+[cube])
                else:
                    cube.putButtomIndex(firstIndex)
            

heavyCube1 = Cube(100,sides=list((Colors.PERPUL, Colors.PERPUL, Colors.PERPUL, Colors.PERPUL , Colors.PERPUL, Colors.PERPUL)))
heavyCube2 = Cube(90,sides=list((Colors.BLUE, Colors.BLUE, Colors.BLUE, Colors.BLUE , Colors.BLUE, Colors.BLUE)))
cubes = [Cube(10),Cube(2),Cube(8),Cube(1),heavyCube1,heavyCube2,Cube(80),Cube(40),Cube(20)]
tower = Tower(cubes=cubes)
tower.FindOptimalSolution([])
tower.printTower()
print(len(tower.resCubes))