#!/usr/bin/env python3
"""A tiny choose-your-own-adventure game for the MLH GHW GitHub Copilot challenge."""

STORY = {
    "start": ("You wake up in a dark server room. A door is to the LEFT and a glowing terminal is to the RIGHT.",
              {"left": "hallway", "right": "terminal"}),
    "hallway": ("The hallway splits. You hear music UP the stairs and see a coffee machine DOWN the hall.",
                {"up": "party", "down": "coffee"}),
    "terminal": ("The terminal asks: 'Merge the pull request?' Type YES or NO.",
                 {"yes": "merged", "no": "start"}),
    "party": ("You found the Hacktoberfest party and won a sticker pack. You win!", {}),
    "coffee": ("The coffee machine is out of order. Your adventure ends in sadness.", {}),
    "merged": ("CI passes on the first try. Legendary! You win!", {}),
}


def play():
    scene = "start"
    while True:
        text, choices = STORY[scene]
        print("\n" + text)
        if not choices:
            print("\nThanks for playing!")
            return
        choice = input(f"Choose ({'/'.join(choices)}): ").strip().lower()
        if choice in choices:
            scene = choices[choice]
        else:
            print("That's not an option, try again.")


if __name__ == "__main__":
    play()
