def box_code(symbol, width, height):
    print(symbol*width)
    for i in range(height-2):
        print(symbol + (' '*(width-2))+symbol)
        
    print(symbol*width)
    
    
    
width = 15
height = 5
box_code('*', width, height)
    
    
    
    
