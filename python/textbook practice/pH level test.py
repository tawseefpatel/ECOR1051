def pH(pH_level):
    """return if the pH level is acidic or basic
    pH_level(6.0)
    is acidic
    """
    pH = 0.0
    
    if pH < 7.0 and pH >= 0:
        print ("The ph", pH, "is acidic")
    if pH > 7.0 and pH <= 14.0:
        print ("The pH", pH, "is basic")
    if pH == 7.0:
        print ("The pH", pH, "is neutral") 
        
    if pH < 0.0:
        print ("The pH", pH, "does not exist")
    if pH > 14.0:
        print ("The pH", pH, "does not exist")
        
    return (pH_level)

print (pH(''))