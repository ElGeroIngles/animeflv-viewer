import asyncio
import sys
from merge_media import main as merge_main, update_loading_bar, out, bar_finished
import requests

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
    index = int(input(""))
    anime = requests.get(f"https://animeflv.ahmedrangel.com/api/anime/{out[index]['slug']}").json()
    
    # ask for the episode
    what_episode = int(input(f"Select episode ({anime['data']['episodes'][0]['number']}-{anime['data']['episodes'][-1]['number']}): "))
    
    # get the url of the episode
    episode_slug = next((episodio['slug'] for episodio in anime['data']['episodes'] if episodio['number'] == what_episode), None)
    
    # get the episode
    episode = requests.get(f"https://animeflv.ahmedrangel.com/api/anime/episode/{episode_slug}").json()

    # print all the links to see the episode
    for x in episode['data']['servers']:
        print(f"\n{x['name']}:")

        try:
            print(f"Download: {x['download']}")
        except:
            pass

        try:
            print(f"Embed: {x['embed']}")
        except:
            pass



if __name__ == "__main__":
    asyncio.run(main())
