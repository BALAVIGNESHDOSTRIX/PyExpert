def BinaryS(arr=[], st_index=None, end_index=None, srelem=None):
    #base condition
    if st_index > end_index:
        return -1

    mid = (st_index + end_index) // 2

    if arr[mid] == srelem:
        return mid

    if srelem < arr[mid]:
        return BinaryS(arr,st_index, mid-1, srelem)
    else:
        return BinaryS(arr, mid+1, end_index, srelem)



scx = [1,6,9,10,17,177]
fndelem = 177
index = BinaryS(arr=scx, st_index=0, end_index=len(scx), srelem=fndelem)
print(index)
