inc_list = []
dec_list = []

def inc_ok(list, num):
    if len(list) == 0 :
        return True
    if list[len(list) - 1] < num :
        return True
    else : return False

def dec_ok(list, num):
    if len(list) == 0 :
        return True
    if list[len(list) - 1] > num :
        return True
    else : return False

max_total = 0
def func(ns, idx):
    global max_total
    total = sum(inc_list) + sum(dec_list)
    if total > max_total:
        max_total = total

    if idx == len(ns):
        return
    
    if inc_ok(inc_list, ns[idx]):
        inc_list.append(ns[idx])
        func(ns, idx + 1)
        inc_list.pop()
    
    if dec_ok(dec_list, ns[idx]):
        dec_list.append(ns[idx])
        func(ns, idx + 1)
        dec_list.pop()
    
    func(ns, idx + 1)

    return

# ns = [3, 10, 5, 2, 8, 100, 7, 4]          # 137
ns = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]  # 90

func(ns, 0)
print(max_total)