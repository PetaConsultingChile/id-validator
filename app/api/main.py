from services.validated_foreign import ocr

def execute():
    print("inicio")
    result= ocr("prueba/carnet.jpg")
    print(result)
execute()