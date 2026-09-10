default character_dialogue_seen = set()

init python:
    def first_time(dialogue_id):
        # checks if dialogue has been seen before, if not adds it to the set and returns True, otherwise returns False
        if dialogue_id in character_dialogue_seen:
            return False
        character_dialogue_seen.add(dialogue_id)
        return True
