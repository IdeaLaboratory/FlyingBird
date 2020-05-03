import os
from bird import Bird

def main():
    print("main called");
    path = os.path.dirname(__file__)
    bird = Bird(10)
    bird.flyForward()

if __name__=="__main__": 
    main()