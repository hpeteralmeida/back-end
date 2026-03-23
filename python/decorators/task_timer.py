import time

def timer(base_fn): 
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f'Task time: {end_time - start_time} seconds.')
    return enhanced_fn

def brew_coffee(): # creating a function for brewing a coffe
    print('Brewing coffee...')
    time.sleep(1)
    print('Coffee is ready!')
    # Functions must handle 1 single action each
brew_coffee()

@timer # to solve that problem, we use decorators
def brew_tea():
    print('Brewing tea...')
    time.sleep(1)
    print('Tea is ready!')

brew_tea()