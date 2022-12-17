class Node:
    def __init__(self,d):
        self.kiri = None
        self.kanan = None
        self.data = d
    def isi(self,d):
        if self.data:
            if d < self.data:
                if self.kiri is None:
                    self.kiri = Node(d)
                else:
                    self.kiri.isi(d)
            elif d > self.data:
                if self.kanan is None:
                    self.kanan = Node(d)
                else:
                    self.kanan.isi(d)
        else:
            self.data = d
    def printTree(self,posisi="root",n=1):
        if self.kiri:
            self.kiri.printTree(posisi+" kiri",n+1)
        print(f"posisi: {posisi} sub({n}): >>> {self.data}")
        if self.kanan:
            self.kanan.printTree(posisi+" kanan",n+1)
    

bst = Node(8)
bst.isi(3)
bst.isi(10)
bst.isi(1)
bst.isi(6)
bst.isi(14)
bst.isi(4)
bst.isi(7)
bst.isi(13)
bst.printTree()