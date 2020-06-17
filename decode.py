from pyzbar import pyzbar

def decode(img):
    barcodes = pyzbar.decode(img)

    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        barcodeType = barcode.type

    return data