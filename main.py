from llm_service.ingredientsGPT import chain
from OCR_service import reader


# print(chain.invoke({"query": "Sodium Lauryl Sulfate"}))
def check_ingredient(ingredient):
    # not inmplemented yet
    ...

def ingredient_check(image_path):
    result = reader.readtext(image_path, detail=0)
    ingredients = []
    for res in result:
        is_ingredient = check_ingredient(res)
        if is_ingredient:
            ingredients.append(res)
    ingredients_text = " ,".join(ingredients)
    return chain.invoke({"query": ingredients_text})
