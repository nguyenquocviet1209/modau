def nhap_tu_dien():
    n = int(input("Nhập n items: "))
    kho_hang = {}
    for i in range(n):
        ma_hang = input("Nhập mã hàng thứ {}: ".format(i+1))
        so_luong = int(input(f"Nhập số lượng của mã hàng {ma_hang}: "))
        kho_hang[ma_hang] = so_luong
    return kho_hang


def nhap_nha_cung_cap():
    m = int(input("Nhập m items: "))
    nha_cung_cap = {}
    for i in range(m):
        ma_ncc = input(f"Nhập mã nhà cung cấp thứ {i+1}: ")
        ten_ncc = str(input(f"Nhập tên nhà cung cấp của {ma_ncc}: "))
        nha_cung_cap[ma_ncc] = ten_ncc
    return nha_cung_cap

def in_nha_cung_cap(nha_cung_cap):
    print("\nDanh sách nhà cung cấp:")
    print(nha_cung_cap)

def check(kho_hang, ma_hang):
    return ma_hang in kho_hang

def sua_so_luong(kho_hang, ma_hang):
    kho_hang[ma_hang] = 200

def bo_sung(kho_hang, ma_hang):
    so_luong_moi = input("Nhập số lượng mới cho ma hàng {}: ".format(ma_hang))
    kho_hang[ma_hang] = so_luong_moi

def xoa_mat_hang(kho_hang):
    for ma_hang, so_luong in list(kho_hang.items()):
        if so_luong == 0:
            del kho_hang[ma_hang]

def chuyen_sang_list(kho_hang):
    ma_hang_list = list(kho_hang.keys())
    so_luong_list = list(kho_hang.values())
    return ma_hang_list, so_luong_list

def in_man_hinh(list1, list2):
    print("3 phần tử đầu tiên của danh sách mã hàng:")
    for i in range(3):
        if i < len(list1):
            print(f"{i + 1}. {list1[i]}")
        else:
            break
    print("\n3 phần tử cuối cùng của danh sách số lượng:")
    for i in range(len(list2) - 3, len(list2)):
        print(f"{i + 1}. {list2[i]}")


# a:nhap tu dien thu 1

tudien1 = nhap_tu_dien()

# b:khoi tao va in tu diem thu 2

tudien2 = nhap_nha_cung_cap()
in_nha_cung_cap(tudien2)

# c:check ma hang o tu dien 1(neu ko sua lai or bo sung

if(check(tudien1,'H001')):
    sua_so_luong(tudien1,'200')
else:
    bo_sung(tudien1,'H001')

# d:xoa cac mat hang sl 0

xoa_mat_hang(tudien1)

# e: chuyen tu dien 1 sang 2 list

ma_hang_list,so_luong_list = chuyen_sang_list(tudien1)

in_man_hinh(ma_hang_list,so_luong_list)

