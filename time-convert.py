def TimeConvert(num): 

    num = int(num)
    hours = num // 60
    minutes = num % 60
    return f'{hours}:{minutes}'
    
# keep this function call here  
print(TimeConvert(num=74))