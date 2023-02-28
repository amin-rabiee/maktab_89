from fastapi import FastAPI

app = FastAPI()

items = [
    {"name":"horse", "des":"a large plant-eating domesticated mammal with solid hoofs and a flowing mane and tail, used for riding, racing, and to carry and pull loads." },
    {"name": "bear", "des": "Bears are carnivoran mammals of the family Ursidae. They are classified as caniforms, or doglike carnivorans. Although only eight species of bears are extant, they are widespread, appearing in a wide variety of habitats throughout the Northern Hemisphere and partially in the Southern Hemisphere. Bears are found on the continents of North America, South America, Europe, and Asia."},
    {"name": "fish", "des": "Fish are aquatic, craniate, gill-bearing animals that lack limbs with digits. Included in this definition are the living hagfish, lampreys, ..."},
    {"name": "lion", "des": "The lion (Panthera leo) is a large cat of the genus Panthera native to Africa and India. It has a muscular, broad-chested body; short, rounded head; ..."}
]

@app.get("/")
def query(search: str):
    result = []
    for i in items:
        name = i.get("name")
        des = i.get("des")
        if search in name or search in des:
            result.append(i)
    return {"result":result}

