import asyncio
import sys
from merge_media import main as merge_main, update_loading_bar, out, bar_finished

# Configuración de la salida estándar para caracteres UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Función principal con barra de carga
async def main():
    global bar_finished

    # Pedir al usuario el nombre del anime
    title = input("Name of the anime: ")

    print("Searching for animes with a similar name...")

    # Primera búsqueda
    import aiohttp
    async with aiohttp.ClientSession() as session:
        url = f"https://animeflv.ahmedrangel.com/api/search?query={title}&page=1"
        async with session.get(url) as response:
            searchs = await response.json()

    # Crear tarea para la barra de carga
    task = asyncio.create_task(update_loading_bar())

    # Ejecutar la recopilación principal (asincrónica)
    await merge_main(searchs, title)

    # Finalizar la barra de carga
    bar_finished = True
    await task  # Esperar que la barra termine correctamente

    # Mostrar resultados al final
    print("\nAnime found:")
    for i, x in enumerate(out):
        print(f"[{i}] {x['title']}")
    
    # get what anime the user wants to see:
    index = input("")
    print(index)

if __name__ == "__main__":
    asyncio.run(main())
