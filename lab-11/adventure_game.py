from __future__ import annotations
from numpy.random import randint


class Item:
    """
    Represents any Item.

    An Item has a name and a description. Both are strings.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def describe(self):
        print(self.description)


class Key(Item):
    """
    Represents a key (subclass of Item)
    """

    def __init__(self, name: str, description: str):
        Item.__init__(self, name, description)

    def use(self, room: Room):
        """
        Use a Key to lock or unlock a room
        """
        room.toggle_lock(self)


class Coin(Item):
    """
    Represents a coin (subclass of Item)
    """

    def __init__(self, name: str, description: str, value: int | float):
        Item.__init__(self, name, description)
        self.value = value


class Room:
    """
    A Room is has a name and a description.
    Each room has a list of characters present and some items.
    A Room also has a list of accessible_rooms representing other Rooms
    that can be accessed from this location.
    A room can be locked or unlocked.

    A Room has the following variables:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * `characters`         -   Set of Characters in the Room
    * `items`              -   Set of Items in the Room
    * `accessible_rooms`   -   Set of other Rooms that are accessible from Room
    * `locked`             -   Boolean representing if the location is locked (from all directions).

    A Room has the following methods:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * `describe()`                -   Print description of Room and all Characters and Items
    * `toggle_lock(key)`          -   Toggle the Room.locked value between True/False. Must use a Key.
    * `get_room(name)`            -   Returns the Room object with name name if the name is part of self.accessible_room
    * `get_item(name)`            -   Returns the Item with name name if name is in self.items
    * `add_accessible_room(room)` -   Add a new room to the self.accessible_rooms set.
    """

    def __init__(
        self,
        name: str,
        description: str,
        characters: set[Character],
        items: set[Item],
        accessible_rooms: set[Room] = set(),
        locked: bool = False,
    ):
        """
        Initialize Room and its variables
        """
        self.name = name
        self.description = description
        self.characters = characters
        self.items = items
        self.accessible_rooms = set(accessible_rooms)
        self.locked = locked

    def describe(self):
        """
        Prints a discription of the Room including the Characters
        and Items present in the Room
        """
        if len(self.characters) > 0:
            print("\nThere are some other people here")
            for character in self.characters:
                print(
                    "\t {}:\t {}".format(character.name, character.description)
                )

        # TODO add code here to print description of all items in the Room
        # print("****** Room.describe() is not complete ******")
        if len(self.items) > 0:
            print("\nYou notice some items in here")
            for item in self.items:
                print(f"\t{item.name}:", end="\t ")
                item.describe()

        if len(self.items) == 0 and len(self.characters) == 0:
            print("\nYou are alone here...")

        print("\nFrom here, you can go to")
        for room in self.accessible_rooms:
            print("\t {}:\t {}".format(room.name, room.description))

    def toggle_lock(self, key):
        """
        Toggle the lock on a location from locked to unlock using a key.

        Input
            key     -    Any Key object
        """
        if not isinstance(key, Key):
            print("This room is locked! You need to find a key.")
        else:
            self.locked = not self.locked

    def get_room(self, name: str) -> Room | None:
        """
        Return room object if it is reachable from this room.

        :param name: The name of the room.
        :return: If the room is accessible, return the Room object. Else, None.
        """
        # TODO replace print statement with your code
        # print("****** Room.get_room() is not yet implemented ******")
        for room in self.accessible_rooms:
            if room.name == name:
                return room
        print(f"It doesn't look like {name} is accessible from here.")

    def get_character(self, name: str) -> Character | None:
        """
        Return character object if a Person with this name is in Room

        :param name: The name of the character.
        :return: If the Character is here, return the Character. Else, None.
        """
        for character in self.characters:
            if character.name == name:
                return character
        print("It doesn't look like", name, "is in this room.")

    def get_item(self, name: str) -> Item | None:
        """
        Return an item that is present at this location. Item will be removed
        from self.locations and returned.

        :param name: The name of the item.
        :return: The Item object with the input name if it is in the Room.
        """
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item
        print("It doesn't look like", name, "is in this room.")

    def add_accessible_room(self, room: Room):
        """
        Add a room leading to a reachable room to self.accessible_rooms

        :param room: The Room object.
        """
        if not room in self.accessible_rooms:
            self.accessible_rooms.add(room)


class Character:
    """
    Represents a Character in our game.

    A Character has the following variables:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * `self.name`           -   Character's name (a string)
    * `self.description`    -   Character's description (a string)
    * `self.message`        -   A message the Character has to convey.
    * `self.other_message`  -   A second message the Character has to convey.

    A Character is able to
    ~~~~~~~~~~~~~~~~~~~~~~

    * `talk()`      -   Randomly returns self.message or self.other_message.
    * `describe()`  -   Prints self.name and self.description

    """

    def __init__(
        self, name: str, description: str, message: str, other_message: str = ""
    ):
        """
        Initialize a Character with a name, description, messages, and an
        empty backpack
        """
        self.name = name
        self.description = description
        self.message = message
        self.other_message = other_message

    def talk(self):
        """
        Returns a message
        """

        if self.other_message == "":
            return self.message
        else:
            if randint(0, 2):
                return self.other_message
            else:
                return self.message

    def describe(self):
        """
        Prints a description of the Character
        """
        print("{}:\n\t {}".format(self.name, self.description))


class Hero(Character):
    """
    Represents a Hero. A Hero is a specific Character. In addition to having a
    name, description, messages like all Characters, the Hero has a location,
    and a set of items called the backpack.

    A Hero has the additional variables:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * `location`    -   Current Room the Hero is in
    * `backpack`    -   Set of Items the Hero is holding

    The Hero is able to:
    ~~~~~~~~~~~~~~~~~~~~

    * `explore()`      -    Look around.
    * `go_to(name)`    -    Updated self.location to be Room with name "name"
                            only if name is in the
                            self.location.accessible_rooms set.
    * `talk_to(name)`  -    Talk to a Character with name "name" only if that
                            Character is in the self.location.characters set.
    * `pick_up(name)`  -    Pick up an Item if it is in self.location.items
    * `unlock(name)`   -    Unlock a room only a key exists in self.backpack
                            AND the location with name is accessible from self.location.

    Example usage:
    ~~~~~~~~~~~~~~

    >>> # Create a hero object
    >>> alice = Hero(
    >>>    "Alice", "Game hero", staircase, "Hello, I'm looking for the exit"
    >>> )

    >>> # Move alice to the "antichamber"
    >>> alice.go_to("antichamber")

    >>> # Ask Alice to explore:
    >>> alice.explore()
    """

    def __init__(
        self,
        name: str,
        description: str,
        message: str,
        other_message: str,
        location: Room,
        backpack: set[Item] = set(),
    ):
        """
        Initialize the Hero
        """
        Character.__init__(self, name, description, message, other_message)
        self.location = location
        self.backpack = backpack

    def explore(self):
        """
        Take in your surroundings!
        """
        print(
            "You are currently in {}:\n\t{}.".format(
                self.location.name, self.location.description
            )
        )
        self.location.describe()

    def go_to(self, name):
        """
        Move your hero around. If a Room named "name" exists in
        self.location.accessible_rooms, move Hero by updated self.location to
        this room.

        :param name: The name of a Room that the Hero is to move to.
        """
        # Check if any Room with "name" is accesible from the current Room
        if self.location.get_room(name):
            if name == "portal":
                print(
                    "You walk through the magic portal and somehow you ended "
                    + "up back in room107."
                )
                portal = self.location.get_room(name)
                self.location = portal.get_room("room107")
            else:
                new_room = self.location.get_room(name)
                if not new_room.locked:
                    print(
                        "You move from the {} to the {}.".format(
                            self.location.name, name
                        )
                    )
                    self.location = new_room
                else:
                    print(
                        f"You can't get into {name}. It's locked. "
                        + "Do you have a key?"
                    )

    def talk_to(self, name: str):
        """
        Talk to character if character is at hero's current place.

        :param name: The name of a Character. If there is a Character with this
        name in self.location.characters, talk to them.
        """
        if self.location.get_character(name):
            character = self.location.get_character(name)
            print('You turn to {} and say, "{}".'.format(name, self.talk()))
            print('They respond, "{}"'.format(character.talk()))

    def pick_up(self, name: str):
        """
        Take a thing if thing is at hero's current place.

        Method will check if there is an Item in self.location.items
        with the input name. If so, the Item will be added to self.backpack.

        :param name: The name of the Item.
        """
        # TODO replace with your code
        # print("****** Hero.pick_up is not yet implemented ******")
        item = self.location.get_item(name)
        if item is not None:
            print(f"You pick up the {name} and put it in your backpack.")
            self.backpack.add(item)
            return
        print(f"It looks like {name} is not in your current room!")

    def rummage(self) -> list[Item]:
        """
        Print each item in self.backpack with its description and return a list
        of item names.
        """
        # TODO replace with your code
        # print("****** Hero.rummage is not yet implemented ******")
        item_names = []
        print("You rummage through your backpack.", end=" ")
        if len(self.backpack) > 0:
            print("You have the following items:")
            for item in self.backpack:
                item_names.append(item)
                print(f"\t{item.name}:", end="\t ")
                item.describe()
        else:
            print("Your inventory is empty!")
        return item_names

    def unlock(self, name: str):
        """
        If hero has a key, toggle a room lock only if the room is accessible
        from current location.

        Method will check if there is a Room in self.accessible_rooms with the
        input name AND self.backpack contains at least on Key object before
        using the Key to unlock the Room.

        :param name: The name of the Room object."""
        # TODO replace with your code
        # print("****** Hero.unlock is not implemented ******")

        # First, check to see if Hero has *any* key:
        has_key: bool = False
        for item in self.backpack:
            if isinstance(item, Key):
                has_key = True
                key_to_unlock = item
                break
        if not has_key:
            print("You do not have a key in your inventory!")
            return

        # Check for `name` in accessible rooms:
        has_room: bool = False
        for room in self.location.accessible_rooms:
            if room.name == name:
                has_room = True
                room_to_open = room
                break
        if not has_room:
            print(
                "The room you are trying to unlock is not accessible from here!"
            )
            return

        # Use the key to unlock the room:
        key_to_unlock.use(room=room_to_open)
        print(f"You unlock {room_to_open.name} using {key_to_unlock.name}.")

    def describe(self):
        """
        Prints out information on our hero.
        """
        print("This is you -- the hero of our adventure \n")
        print("{}:\t{}".format(self.name, self.description))
        print("Location: {}".format(self.location.name))
        if len(self.backpack) > 0:
            print("\n\t You have a few items in your backpack:")
            for item in self.backpack:
                print(item.name, ": ", item.description)
        else:
            print("\n\tYour backpack is empty.")


def welcome_scene():
    print("Welcome! Let's go on an adventure!\n")
    print("It is a bright day and you were just on your way home ")
    print("from class when you decided to stop at the library.\n")
    print("As you wander down a familiar maze of stacks, you notice")
    print("a room you never saw before.\n")
    print("The room is marked 107.")
    print("You enter the room and find you are in a Strange Library.")
    print("The exit leading back to the main library is now locked...\n\n")
    print("It looks like you have to find another way out of this place!")
    print("~~~~~~~~~~~~~~~~~~~~ Good Luck! ~~~~~~~~~~~~~~~~~~~~~\n\n")
    print_guide()


def print_guide():
    print("Enter one of the following commands:\n")
    print("\t'whoami'\t\t Print out information about yourself.")
    print("\t'explore'\t\t Take a look around in the current room.")
    print(
        "\t'rummage'\t\t Check the belongings you currently have in your backpack."
    )
    print(
        "\t'talk_to [name]\t\t Talk to another Chacater in the same room as you."
    )
    print(
        "\t'go_to [name]'\t\t Walk through a room accessible from the current room you are in."
    )
    print("\t'pick_up [name]'\t Pick up an item that is in the room.")
    print(
        "\t'unlock [name]'\t\t Unlock a nearby room. Will only work if you currently have a Key item."
    )
    print("")
    print('To leave the game early, type "exit"')


from load_world import *

if __name__ == "__main__":
    hero_name = input("Before we begin, what is your name?\n>>")
    hero = Hero(
        hero_name,
        "Hero of the game (You!)",
        "I'm trying to get out of here!",
        "Can you help me find the exit?",
        room107,
    )

    welcome_scene()

    playing_game = True
    while playing_game:
        input_cmd = input('\nEnter a command or "help" for help\n>> ')
        try:
            input_words = input_cmd.split(" ")
            if "help" in input_words:
                print_guide()
            elif "exit" in input_words:
                print(
                    "~~~~~~~~~~~~~~ Thank you for playing!  ~~~~~~~~~~~~~~\n\n"
                )
                playing_game = False
            elif "whoami" in input_words:
                print("{}:\t{}".format(hero.name, hero.description))
                print("You are currently in: {}".format(hero.location.name))
            elif "explore" in input_words:
                hero.explore()
            elif "rummage" in input_words:
                hero.rummage()
            elif "pick_up" in input_words:
                obj_name = input_words[input_words.index("pick_up") + 1]
                hero.pick_up(obj_name)
            elif "go_to" in input_words:
                obj_name = input_words[input_words.index("go_to") + 1]
                hero.go_to(obj_name)
            elif "talk_to" in input_words:
                char_name = input_words[input_words.index("talk_to") + 1]
                hero.talk_to(char_name)
            elif "unlock" in input_words:
                room_name = input_words[input_words.index("unlock") + 1]
                hero.unlock(room_name)
            else:
                print("Invalid command")
                print_guide()

        except:
            print("Invalid command")
            print_guide()

        if hero.location.name == "room007":
            print("Wait -- This is not a room but an exit!")
            print("You run outside. It is a sunny day! Congratulations!\n")
            print("~~~~~~~~~~~~~~ Thank you for playing!  ~~~~~~~~~~~~~~\n\n")
            playing_game = False
