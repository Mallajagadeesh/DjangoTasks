import barcode


def logic(name,b):
    ean = barcode.barcode(name)
    filename = ean.save(f'{b}.png',options={'write_text':False})
    return filename






# from barcode.pybarcode import create_barcode
#
#
# def logic(name,b):
#     ean = create_barcode(name)
#     filename = ean.save(f'{b}.png',options={'write_text':False})
#     return filename