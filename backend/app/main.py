from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Hero(BaseModel):
    id: Optional[int] = None
    name: str
    difficulty: str
    description: str
    attack_type: str


class Review(BaseModel):
    id: Optional[int] = None
    username: str
    hero_name: str
    text: str
    rating: int


# База данных на основе вашего файла
heroes_db = [
    Hero(id=1, name="Abaddon", difficulty="Easy", description="Roamer", attack_type="melee"),
    Hero(id=2, name="Alchemist", difficulty="Easy", description="Carry", attack_type="melee"),
    Hero(id=3, name="Ansient Apparition", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=4, name="Anti-Mage", difficulty="Easy", description="Сarry", attack_type="melee"),
    Hero(id=5, name="Arc Warden", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=6, name="Axe", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=7, name="Bane", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=8, name="Batrider", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=9, name="Beastmaster", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=10, name="Bloodseeker", difficulty="Easy", description="Сarry", attack_type="melee"),
    Hero(id=11, name="Bounty Hunter", difficulty="Easy", description="Mid", attack_type="melee"),
    Hero(id=12, name="Brewmaster", difficulty="Hard", description="Offlaner", attack_type="melee"),
    Hero(id=13, name="Bristleback", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=14, name="Broodmother", difficulty="Medium", description="Mid", attack_type="melee"),
    Hero(id=15, name="Centaur Warrunner", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=16, name="Chaos Knight", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=17, name="Chen", difficulty="Hard", description="Support", attack_type="ranged"),
    Hero(id=18, name="Clinkz", difficulty="Medium", description="Roamer", attack_type="ranged"),
    Hero(id=19, name="Clockwerk", difficulty="Medium", description="Roamer", attack_type="melee"),
    Hero(id=20, name="Crystal Maiden", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=21, name="Dark Seer", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=22, name="Dark Willow", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=23, name="Dawnbreaker", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=24, name="Dazzle", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=25, name="Death Prophet", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=26, name="Disruptor", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=27, name="Doom", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=28, name="Dragon Knight", difficulty="Easy", description="Mid", attack_type="melee"),
    Hero(id=29, name="Drow Ranger", difficulty="Easy", description="Carry", attack_type="ranged"),
    Hero(id=30, name="Earth Spirit", difficulty="Hard", description="Roamer", attack_type="melee"),
    Hero(id=31, name="Earthshaker", difficulty="Medium", description="Roamer", attack_type="melee"),
    Hero(id=32, name="Elder Titan", difficulty="Hard", description="Offlaner", attack_type="melee"),
    Hero(id=33, name="Ember Spirit", difficulty="Medium", description="Mid", attack_type="melee"),
    Hero(id=34, name="Enchantress", difficulty="Medium", description="Offlaner", attack_type="ranged"),
    Hero(id=35, name="Enigma", difficulty="Medium", description="Offlaner", attack_type="ranged"),
    Hero(id=36, name="Faceless Void", difficulty="Medium", description="Carry", attack_type="melee"),
    Hero(id=37, name="Grimstroke", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=38, name="Gyrocopter", difficulty="Medium", description="Carry", attack_type="ranged"),
    Hero(id=39, name="Hoodwink", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=40, name="Huskar", difficulty="Easy", description="Mid", attack_type="ranged"),
    Hero(id=41, name="Invoker", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=42, name="Io", difficulty="Hard", description="Support", attack_type="ranged"),
    Hero(id=43, name="Jakiro", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=44, name="Juggernaut", difficulty="Easy", description="Carry", attack_type="melee"),
    Hero(id=45, name="Keeper of the Light", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=46, name="Kunkka", difficulty="Medium", description="Mid", attack_type="melee"),
    Hero(id=47, name="Legion Commander", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=48, name="Leshrac", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=49, name="Lich", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=50, name="Lifestealer", difficulty="Easy", description="Carry", attack_type="melee"),
    Hero(id=51, name="Lina", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=52, name="Lion", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=53, name="Lone Druid", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=54, name="Luna", difficulty="Easy", description="Carry", attack_type="ranged"),
    Hero(id=55, name="Lycan", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=56, name="Magnus", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=57, name="Marci", difficulty="Medium", description="Support", attack_type="melee"),
    Hero(id=58, name="Mars", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=59, name="Medusa", difficulty="Easy", description="Carry", attack_type="ranged"),
    Hero(id=60, name="Meepo", difficulty="Hard", description="Mid", attack_type="melee"),
    Hero(id=61, name="Mirana", difficulty="Medium", description="Roamer", attack_type="ranged"),
    Hero(id=62, name="Monkey King", difficulty="Medium", description="Mid", attack_type="melee"),
    Hero(id=63, name="Morphling", difficulty="Hard", description="Carry", attack_type="ranged"),
    Hero(id=64, name="Muerta", difficulty="Medium", description="Carry", attack_type="ranged"),
    Hero(id=65, name="Naga Siren", difficulty="Hard", description="Carry", attack_type="melee"),
    Hero(id=66, name="Nature's Prophet", difficulty="Medium", description="Offlaner", attack_type="ranged"),
    Hero(id=67, name="Necrophos", difficulty="Easy", description="Offlaner", attack_type="ranged"),
    Hero(id=68, name="Night Stalker", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=69, name="Nyx Assassin", difficulty="Medium", description="Roamer", attack_type="melee"),
    Hero(id=70, name="Ogre Magi", difficulty="Easy", description="Support", attack_type="melee"),
    Hero(id=71, name="Omniknight", difficulty="Easy", description="Support", attack_type="melee"),
    Hero(id=72, name="Oracle", difficulty="Hard", description="Support", attack_type="ranged"),
    Hero(id=73, name="Outworld Destroyer", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=74, name="Pangolier", difficulty="Hard", description="Mid", attack_type="melee"),
    Hero(id=75, name="Phantom Assassin", difficulty="Easy", description="Carry", attack_type="melee"),
    Hero(id=76, name="Phantom Lancer", difficulty="Medium", description="Carry", attack_type="melee"),
    Hero(id=77, name="Phoenix", difficulty="Medium", description="Offlaner", attack_type="ranged"),
    Hero(id=78, name="Primal Beast", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=79, name="Puck", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=80, name="Pudge", difficulty="Easy", description="Roamer", attack_type="melee"),
    Hero(id=81, name="Pugna", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=82, name="Queen of Pain", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=83, name="Razor", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=84, name="Riki", difficulty="Medium", description="Roamer", attack_type="melee"),
    Hero(id=85, name="Rubick", difficulty="Hard", description="Support", attack_type="ranged"),
    Hero(id=86, name="Sand King", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=87, name="Shadow Demon", difficulty="Hard", description="Support", attack_type="ranged"),
    Hero(id=88, name="Shadow Fiend", difficulty="Medium", description="Mid", attack_type="ranged"),
    Hero(id=89, name="Shadow Shaman", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=90, name="Silencer", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=91, name="Skywrath Mage", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=92, name="Slardar", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=93, name="Slark", difficulty="Medium", description="Carry", attack_type="melee"),
    Hero(id=94, name="Snapfire", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=95, name="Sniper", difficulty="Easy", description="Mid", attack_type="ranged"),
    Hero(id=96, name="Spectre", difficulty="Medium", description="Carry", attack_type="melee"),
    Hero(id=97, name="Spirit Breaker", difficulty="Easy", description="Roamer", attack_type="melee"),
    Hero(id=98, name="Storm Spirit", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=99, name="Sven", difficulty="Easy", description="Carry", attack_type="melee"),
    Hero(id=100, name="Techies", difficulty="Hard", description="Support", attack_type="ranged"),
    Hero(id=101, name="Templar Assassin", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=102, name="Terrorblade", difficulty="Hard", description="Carry", attack_type="melee"),
    Hero(id=103, name="Tidehunter", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=104, name="Timbersaw", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=105, name="Tinker", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=106, name="Tiny", difficulty="Medium", description="Roamer", attack_type="melee"),
    Hero(id=107, name="Treant Protector", difficulty="Easy", description="Support", attack_type="melee"),
    Hero(id=108, name="Troll Warlord", difficulty="Medium", description="Carry", attack_type="ranged"),
    Hero(id=109, name="Tusk", difficulty="Easy", description="Roamer", attack_type="melee"),
    Hero(id=110, name="Underlord", difficulty="Medium", description="Offlaner", attack_type="melee"),
    Hero(id=111, name="Undying", difficulty="Easy", description="Roamer", attack_type="melee"),
    Hero(id=112, name="Ursa", difficulty="Easy", description="Carry", attack_type="melee"),
    Hero(id=113, name="Vengeful Spirit", difficulty="Easy", description="Roamer", attack_type="ranged"),
    Hero(id=114, name="Venomancer", difficulty="Easy", description="Roamer", attack_type="ranged"),
    Hero(id=115, name="Viper", difficulty="Easy", description="Mid", attack_type="ranged"),
    Hero(id=116, name="Visage", difficulty="Hard", description="Mid", attack_type="ranged"),
    Hero(id=117, name="Void Spirit", difficulty="Medium", description="Mid", attack_type="melee"),
    Hero(id=118, name="Warlock", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=119, name="Weaver", difficulty="Medium", description="Carry", attack_type="ranged"),
    Hero(id=120, name="Windranger", difficulty="Medium", description="Carry", attack_type="ranged"),
    Hero(id=121, name="Winter Wyvern", difficulty="Medium", description="Support", attack_type="ranged"),
    Hero(id=122, name="Witch Doctor", difficulty="Easy", description="Support", attack_type="ranged"),
    Hero(id=123, name="Wraith King", difficulty="Easy", description="Offlaner", attack_type="melee"),
    Hero(id=124, name="Zeus", difficulty="Easy", description="Mid", attack_type="ranged")
]

reviews_db = []


@app.get("/api/heroes")
async def get_heroes():

    result = []
    for hero in heroes_db:
        hero_ratings = [r.rating for r in reviews_db if r.hero_name == hero.name]
        avg_rating = round(sum(hero_ratings) / len(hero_ratings), 1) if hero_ratings else 0.0
        hero_dict = hero.dict()
        hero_dict["avg_rating"] = avg_rating
        result.append(hero_dict)
    return result


@app.get("/api/heroes/top")
async def get_top_heroes():

    stats = []
    for hero in heroes_db:
        count = len([r for r in reviews_db if r.hero_name == hero.name])
        if count > 0:
            stats.append({"name": hero.name, "count": count})


    sorted_stats = sorted(stats, key=lambda x: x['count'], reverse=True)
    return sorted_stats[:3]


@app.get("/api/reviews", response_model=List[Review])
async def get_reviews():
    return reviews_db


@app.post("/api/reviews")
async def add_review(review: Review):
    review.id = len(reviews_db) + 1
    reviews_db.append(review)
    return review


@app.delete("/api/reviews/{review_id}")
async def delete_review(review_id: int):
    global reviews_db
    reviews_db = [r for r in reviews_db if r.id != review_id]
    return {"status": "deleted"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8010)