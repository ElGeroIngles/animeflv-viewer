import json

# JSON de ejemplo
data = {
    "success": True,
    "data": {
        "title": "Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season",
        "episodes": [
            {"number": 1, "slug": "rezero-kara-hajimeru-isekai-seikatsu-2nd-season-1", "url": "https://www3.animeflv.net/ver/rezero-kara-hajimeru-isekai-seikatsu-2nd-season-1"},
            {"number": 2, "slug": "rezero-kara-hajimeru-isekai-seikatsu-2nd-season-2", "url": "https://www3.animeflv.net/ver/rezero-kara-hajimeru-isekai-seikatsu-2nd-season-2"},
            {"number": 3, "slug": "rezero-kara-hajimeru-isekai-seikatsu-2nd-season-3", "url": "https://www3.animeflv.net/ver/rezero-kara-hajimeru-isekai-seikatsu-2nd-season-3"},
            # Otros episodios...
        ]
    }
}

# Buscar el episodio con number = 1 y obtener su slug
slug_episodio_1 = next((episodio['slug'] for episodio in data['data']['episodes'] if episodio['number'] == 1), None)

if slug_episodio_1:
    print(f"El slug del episodio 1 es: {slug_episodio_1}")
else:
    print("No se encontró el episodio con number 1.")
