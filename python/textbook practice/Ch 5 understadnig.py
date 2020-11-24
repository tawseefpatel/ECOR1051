pH = float(input('enter the pH level: '))

if pH < 7.0 and pH > 14.0 :
    print('the pH', pH , 'is acidic')
if pH > 7.0 and pH < 0.0:
    print('the pH', pH , 'is basic')
if pH == 7.0:
    print('the pH', pH , 'is neutral')




if pH > 14.0:
    print('the pH', pH , 'does not exist')
if pH < 0.0:
    print('the pH', pH , 'does not exist')


if pH > 14.0 and pH < 0.0 :
    print('the pH', pH , 'does not exist')