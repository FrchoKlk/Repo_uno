#06-05-2025
#Fermin Martinez
import asyncio
async def tarea (nombre):
    print (f"{nombre}")
    await asyncio.sleep(2)
    print(f"{nombre} termino")
async def main(
        tarea("tarea1")
        tarea("tarea2")
):
    asyncio.run(main())