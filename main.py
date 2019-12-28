from view.view_nilai import nyari,cetak,header,notoption
from view.input_nilai import inputan,edit,delete
header()
while True:

    c = input("\nPilih Opsi: ")

    # KELUA PROGRAM
    if c.lower() == 'k':
        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break

    # TAMPILKAN LIST DATA
    elif c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 't':
        inputan()

    # EDIT DATA
    elif c.lower() == 'u':
        edit()

    # MENCARI DATA
    elif c.lower() == 'c':
        nyari()

    # HAPUS DATA
    elif c.lower() == 'h':
        delete()

    else:
        notoption()