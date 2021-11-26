def print1(arr_new):
    for text in arr_new:
        print(f"Объект {text}-напечатался")
def pechat(arr_models,arr_new):
    while arr_models:   
        title1 = arr_models.pop(0)
        arr_new.append(title1)
        print(arr_new)
