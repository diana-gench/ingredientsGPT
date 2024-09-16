import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('test.webp', detail=0)

print("Started")
print(result)
print("finished")