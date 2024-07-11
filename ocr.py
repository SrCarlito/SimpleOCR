import pytesseract

class Char:
    def __init__(self,trama):
            self.char = trama[0]
            self.x0 = int(trama[1])
            self.y0 = int(trama[2])  
            self.x1 = int(trama[3])  
            self.y1 = int(trama[4]) 
            self.size = int(0.75 * (self.x1 - self.x0))

def ocr(image):
    bxs = pytesseract.image_to_boxes(image)
    
    result = []
    for x in bxs.split("\n"): 
        trama = x.split(" ")
                      #        x0      y0    x1      y1
        # print(trama) # ['Q', '1329', '13', '1350', '33', '0']
        if len(trama) >= 5 :
                result.append(Char(trama))

    return result
