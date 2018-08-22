from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

database = client.get_default_database()

posts = database["posts"]

new_post = {
"title": "Murmaider",
"author": "Dethklok",
"content": """There are no fingerprints
Deep under water
Nothing to tie one to a crime
And if you seek vengeance
All you need are instruments of pain
You need your
Knives? check.
Rope? check.
Dagger? check.
Chains? check.
Locks? check.
Laser beams? check.
Acid? check.
Body bag? check.
Murmaider [Repeat: x 16]
But beware
For when you quench your blood thirst
Others will seek their vengeance on you
And they won't rest
Until you're dead
They'll have their:
Shiv? check.
Pipe? check.
Hammer? check.
Axe? check.
Subject? check.
Location? check.
Desire? check.
Vengeance? check.
Hold your breath, swim and strain
The smell of death, can't escape
Blood will could and drift away
Attract the murders of murmaids
It's so cold they all know
What you've done, you can't run
Vengeance is the law for thee
A thousand leagues below the sea
You've been tracked, you've been seen
Murdering the next kin
Ate their hearts drank their blood
Washed your fins in blackened mud
Now you swim try to hide
Heart beats faster from inside
Thought it was a big charade
Your life was ended by murmaids.
Murmaider [Repeat: x 16]
Swords? check.
Saws? check.
Clubs? check.
Claws? check.
Hatred? check.
Anger? check.
Mermaid? check.
Murder? check.
Murder! murder! murmaid murder!
Your life was ended by mermaids."""
}

posts.insert_one(new_post)