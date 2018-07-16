from pymongo import MongoClient

uri = "mongodb://admin_room_1:thitkhotau1@ds235411.mlab.com:35411/c4e19-demolab"

# 1. Connect to DB
client = MongoClient(uri)

# 2. Get DB
database = client.get_default_database()

# 3. Create collections
posts = database["posts"]
# singers = database["singers"]
# 4. Create documents
# new_game = {
#     "Name": "Dead Cell",
#     "Descripton": "You grew up with \ the roguelikes, witnessed the rise of the roguelites and even the birth of the roguelite-lites? We'd now like to present for your consideration our RogueVania, the illegitimate child of a modern Roguelite (Rogue Legacy, Binding of Isaac, Enter the Gungeon, Spelunky, etc.) \
#     and an old-school MetroidVania (Castlevania: SotN and its ilk).",
#     "Developer": "Motion Twin",
#     "Pushliser": "Motion Twin"
# }

# new_singer = {
#     "Name": "The Weeknd",
#     "Real name": "Abel Tesfaye",
#     "Bitrh": "16/02/1990"
# }
# 5. Insert documents into collections
# games.insert_one(new_game)
# singers.insert_one(new_singer)

# new_post = {
#     "title": "Murmaider1",
#     "author": "Dethklok",
#     "content": """There are no fingerprints
# Deep under water
# Nothing to tie one to a crime
# And if you seek vengeance
# All you need are instruments of pain
# You need your
# Knives? check.
# Rope? check.
# Dagger? check.
# Chains? check.
# Locks? check.
# Laser beams? check.
# Acid? check.
# Body bag? check.
# Murmaider [Repeat: x 16]
# But beware
# For when you quench your blood thirst
# Others will seek their vengeance on you
# And they won't rest
# Until you're dead
# They'll have their:
# Shiv? check.
# Pipe? check.
# Hammer? check.
# Axe? check.
# Subject? check.
# Location? check.
# Desire? check.
# Vengeance? check.
# Hold your breath, swim and strain
# The smell of death, can't escape
# Blood will could and drift away
# Attract the murders of murmaids
# It's so cold they all know
# What you've done, you can't run
# Vengeance is the law for thee
# A thousand leagues below the sea
# You've been tracked, you've been seen
# Murdering the next kin
# Ate their hearts drank their blood
# Washed your fins in blackened mud
# Now you swim try to hide
# Heart beats faster from inside
# Thought it was a big charade
# Your life was ended by murmaids.
# Murmaider [Repeat: x 16]
# Swords? check.
# Saws? check.
# Clubs? check.
# Claws? check.
# Hatred? check.
# Anger? check.
# Mermaid? check.
# Murder? check.
# Murder! murder! murmaid murder!
# Your life was ended by mermaids."""
# }

# posts.insert_one(new_post)

# get all documents
get_all_posts = posts.find()
count = 0
# print(type(get_all_posts))
for all_posts in get_all_posts:
    for key in all_posts.keys():
        if key == "content":
            count = count + 1
print(count)
#         count = count + 1
# print("Count =", count)
# print(get_all_posts[0]["content"])