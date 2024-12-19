import asyncio
import sys
from merge_media import main as merge_main, update_loading_bar, out, bar_finished
import requests

# Configuración de la salida estándar para caracteres UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Función principal con barra de carga
async def main():
    global bar_finished

    # Obtener el título del anime
    await get_title()

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

    # Obtener el anime seleccionado por el usuario
    index = int(input("\nWhich is the one you want?: "))
    anime = requests.get(f"https://animeflv.ahmedrangel.com/api/anime/{out[index]['slug']}").json()

    # Pedir al usuario el episodio
    what_episode = int(input(f"\nSelect episode ({anime['data']['episodes'][0]['number']}-{anime['data']['episodes'][-1]['number']}): "))

    # Obtener el slug del episodio
    episode_slug = next((episodio['slug'] for episodio in anime['data']['episodes'] if episodio['number'] == what_episode), None)

    # Obtener los datos del episodio
    episode = requests.get(f"https://animeflv.ahmedrangel.com/api/anime/episode/{episode_slug}").json()

    # Mostrar todos los enlaces disponibles para el episodio
    print("\nHere are all the links available for that episode:")
    for x in episode['data']['servers']:
        print(f"\n{x['name']}:")

        try:
            print(f"Download: {x['download']}")
        except KeyError:
            pass

        try:
            print(f"Embed: {x['embed']}")
        except KeyError:
            pass

async def get_title():
    global title
    global searchs

    while True:
        title = input("\nName of the anime: ")
        print("\nSearching for animes with a similar name...")

        import aiohttp
        async with aiohttp.ClientSession() as session:
            try:
                url = f"https://animeflv.ahmedrangel.com/api/search?query={title}&page=1"
                async with session.get(url) as response:
                    if response.status == 200:
                        searchs = await response.json()
                        if searchs:
                            return  # Salir del bucle si la búsqueda fue exitosa
                        else:
                            print("\nCouldn't find any animes with that name, please try again.")
                    else:
                        print(f"\nCouldn't find any animes with that name, please try again.")
            except Exception as e:
                print(f"\nAn error occurred: {e}. Please try again.")

if __name__ == "__main__":
    asyncio.run(main())
    input("\nPress any key to exit...")
