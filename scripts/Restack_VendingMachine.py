vMachine = label(d0, "vMachine")
stacker = label(d1, "vmStacker")
sorter = label(d2, "vmSorter")
btn = label(d3, "btn")
ledD = label(d4, "display")

i = 200
no = 0
while True:
    while i <= 102:
        if vMachine.PrefabHash[i] == -12341234:
            no = no + vMachine.Quantity[i]
            ledD.Setting = no
        i = i+1
    if btn.Setting == 1:
        i = 3