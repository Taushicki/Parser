from parser.rbc_parser import parse
import asyncio 

async def main():
    await parse()
    
if __name__ == '__main__':
    asyncio.run(main())