from fastapi import FastAPI
import random




app = FastAPI()
#The / is the root url fpr the api, without any endpoints
@app.get('/')
# we define an async funcion that return the data form the end point
async def root():
    return [
        
        {'example': 'this is an example', 'data':123999},

        {'example1': 'this is an example', 'data':98899},

        {'example2': 'this is an example', 'data':90099}
        
    ]


# in the random endpoint we will generate a radom number and display it 
#To run the server we use the command in the terminal as
#uvicorn main:app --reload
#Here main is is the scipt file name, app is what we deifned
# --reload flag is used to async update response as we update it

@app.get('/random')

async def get_random():
    rn: int = random.randint(0,50)
    rn1: int = random.randint(51,100)
    return [

{'number0': rn, 'limit': 100},
{'number1': rn1, 'limit': " 100 Numbers Limit" }

    ] 


# Now in order to make the limit as user imputed limit

@app.get('/random/{limit}')

async def get_random(limit:int):
    rn: int = random.randint(0,limit)
    return [

{'number0': rn, 'limit': limit},

    ] 



#Now let us generate amd show a random fruit name
@app.get('/fruits')
async def generate_random_fruit():
    fruits = [
        "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", 
        "Grape", "Honeydew", "Indian Fig", "Jackfruit", "Kiwi", 
        "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", 
        "Raspberry", "Strawberry", "Tangerine", "Ugli fruit", 
        "Vanilla", "Watermelon", "Xigua", "Yellow Passion Fruit", "Zucchini"
    ]
    random_fruit = random.choice(fruits)
    return [
        {'FruitName': random_fruit, 'quatity':100}
    ]

