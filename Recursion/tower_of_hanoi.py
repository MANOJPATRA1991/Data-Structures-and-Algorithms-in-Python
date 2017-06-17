def TowerOfHanoi(n, fro, to, aux):
    if n==1:
        print(("Move disk 1 from {0} to {1}").format(fro, to))
        return
    TowerOfHanoi(n-1, fro, aux, to)
    print(("Move disk {0} from {1} to {2}").format(n, fro, to))
    TowerOfHanoi(n-1, aux, to, fro)

TowerOfHanoi(3, "A", "B", "C")
