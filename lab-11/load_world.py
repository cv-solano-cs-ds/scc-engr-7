from adventure_game import *

# Items in the game
ottoman_empire_book = Item(
    "ottoman_empire_book", "A book on the ottoman empire."
)
croissant = Item("croissant", "A fresh-baked croissant.")
silver_coin = Coin("silver_coin", "A small silver key.", 100)
tower_room_key = Key("tower_room_key", "A key that the Tower Room.")
master_key = Key("master_key", "A key that opens every room.")

# Characters in the game
strange_librarian = Character(
    "strange_librarian",
    "He seems to be in charge and is not very friendly.",
    "I am the librarian in this side of the library.",
    "If you want a book, go to the reading room through the antichamber.",
)

voiceless_girl = Character(
    "voiceless_girl",
    "She's wandering around, kind of like you.",
    "[gestures to the skyway]",
    "[getures to the skyway]",
)

shepherd = Character(
    "shepherd",
    "He seems friendly. He might be helpful.",
    "I've been stuck down here for years.",
    "I heard there is a key that opens the tower_room in the cryptic room.",
)

wandering_man = Character(
    "wandering_man",
    "Another lost person like you.",
    "I came here to read about the Ottoman Empire.",
    "I tried to go through the reading_room, but I was back in room107.",
)

chef = Character(
    "chef",
    "A chef who lives in the Strange Library.",
    "You look hungry.",
    "I just baked a fresh batch of croissants.",
)

tax_expert = Character(
    "tax_expert",
    "An expert on historical taxes.",
    "I was trying to learn about tax collection in the Ottoman Empire when I came here.",
    "I had a book somewhere, I think it is in the reading_room.",
)

# Rooms in the Strange Library
room107 = Room(
    "room107",
    "A hidden access from the Main Library to the Strange Library",
    {strange_librarian},
    set(),
    set(),
    locked=False,
)

antichamber = Room(
    "antichamber",
    "A small room outside of Room107",
    {shepherd},
    set(),
    set(),
    locked=False,
)

hallway2 = Room(
    "hallway2",
    "A very long and slanted hallway fully lined with books.",
    {wandering_man},
    {silver_coin},
    set(),
    locked=False,
)

hallway1 = Room(
    "hallway1",
    "A narrow hallway with a shallow ceiling.",
    {tax_expert},
    set(),
    set(),
    locked=False,
)

staircase_to_tower_room = Room(
    "staircase",
    "A brightly lit staircase. The sunlight pouring in must be a good sign!",
    set(),
    set(),
    set(),
    locked=False,
)

tower_room = Room(
    "tower_room",
    "Stacks of book reach the ceiling. There is a cool breeze.",
    set(),
    set(),
    set(),
    locked=True,
)

bridge = Room(
    "bridge",
    "A small brick bridge. It looks safe to cross.",
    set(),
    set(),
    set(),
    locked=False,
)

room007 = Room(
    "room007",
    "A room with a very small door.",
    set(),
    set(),
    set(),
    locked=False,
)

cell = Room(
    "prison_cell",
    "A prison cell! Don't get stuck here...",
    set(),
    set(),
    set(),
    locked=False,
)

portal = Room(
    "portal",
    "Interesting, this looks like a portal.",
    set(),
    set(),
    set(),
    locked=False,
)

room137 = Room(
    "room_137",
    "This room doesn't have any books ... it looks like a study room.",
    {voiceless_girl},
    set(),
    set(),
    locked=False,
)

kitchen = Room(
    "kitchen",
    "Why is there a kitchen in this library? Strange",
    {chef},
    {croissant},
    set(),
    locked=False,
)

cryptic_room = Room(
    "cryptic_room",
    "The books in this room are written in a cryptic language",
    set(),
    {tower_room_key},
    set(),
    locked=False,
)

reading_room = Room(
    "reading_room",
    "This must be where the Strange Librarian mentioned",
    set(),
    {ottoman_empire_book},
    set(),
    locked=False,
)

skyway = Room(
    "skyway",
    "A very long glass skyway, but you only see clouds.",
    set(),
    {master_key},
    set(),
    locked=False,
)

# Build graph by adding paths
# room 007 is attached to the bridge
for room in [bridge]:
    room007.add_accessible_room(room)
    room.add_accessible_room(room007)

# bridge leads to tower room and exit
for room in [tower_room, room007]:
    bridge.add_accessible_room(room)
    room.add_accessible_room(bridge)

# tower room leads to bridge and staircase
for room in [bridge, staircase_to_tower_room, skyway]:
    tower_room.add_accessible_room(room)
    room.add_accessible_room(tower_room)

for room in [tower_room, room137]:
    skyway.add_accessible_room(room)
    room.add_accessible_room(skyway)

# slanted hallway leads to stairs, kitchen, antichamber, and room 137
for room in [staircase_to_tower_room, kitchen, antichamber, room137]:
    hallway2.add_accessible_room(room)
    room.add_accessible_room(hallway2)

# antichamber leads to room107, hallway2, hallway1, cryptic_room
for room in [room107, hallway2, hallway1, cryptic_room]:
    antichamber.add_accessible_room(room)
    room.add_accessible_room(antichamber)

# hallway1 leads to the antichamber and reading_room
for room in [antichamber, reading_room]:
    hallway1.add_accessible_room(room)
    room.add_accessible_room(hallway1)

# reading_room leads to the cell and portal
for room in [cell, portal]:
    reading_room.add_accessible_room(room)
    room.add_accessible_room(reading_room)

# cell only leads back to reading_room
for room in [reading_room]:
    cell.add_accessible_room(room)
    room.add_accessible_room(cell)

# portal only leads back to the cell
for room in [portal]:
    portal.add_accessible_room(reading_room)
    room.add_accessible_room(cell)

# Portal leads to room107 only
portal.add_accessible_room(room107)
