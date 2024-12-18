import requests
global out
global current_got
# current_got = 0
# progress = []
# percentage_left = []
out = []
# merge all episodes from all pages into a single array:
def merge(list, name):
    # print(list)
    for x in list['data']['media']:
        out.append(x)
        # update_progress(list['data']['foundPages'])

    if list['data']['hasNextPage'] == True:
        next = requests.get(f"https://animeflv.ahmedrangel.com/api/search?query={name}&page={list['data']['currentPage']+1}").json()
        # print("kjsagdsjahdga")
        # print(next)
        merge(next, name)

    return out

# def update_progress(total_pages):
#     current_got += 1
#     total = total_pages * 24
#     percentage = int((current_got * total) / 1000)

#     for x in range(percentage):
#         progress.append("#")

#     if animation == "":


#     while len(percentage) < 11:
#         percentage_left.append("-")

#     print(f"\r[{"".join(progress)}]", end="", flush=True)
