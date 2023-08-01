import asyncio

async def divide(a, b):

    await asyncio.sleep(1)

    try:
        results = a/b
        return results
    
    except ZeroDivisionError:
        print('Cannot divide by zero')

async def main():

    a = int(input('Enter the first Number: '))
    b = int(input('Enter the second Number: '))

    results = await divide(a, b)
    if results != None:
            print(results)

asyncio.run(main())
        

