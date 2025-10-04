from itertools import cycle
from random import randrange, choice
from tkinter import Canvas, Tk, messagebox, font, PhotoImage
import winsound  # works on Windows (optional for sound)

# Window setup
canvas_width = 800
canvas_height = 400

root = Tk()
root.title("🥚 Egg Catcher Game - By KoKo")
root.resizable(False, False)

# Create Canvas
c = Canvas(root, width=canvas_width, height=canvas_height)
c.pack()

# Optional background image (fallback to color if missing)
try:
    bg_image = PhotoImage(file="background.png")
    c.create_image(0, 0, image=bg_image, anchor="nw")
except Exception:
    c.configure(background="deep sky blue")
    c.create_rectangle(-5, canvas_height-100, canvas_width+5,
                       canvas_height+5, fill="sea green", width=0)
    c.create_oval(-80, -80, 120, 120, fill='orange', width=0)

# Sounds
def play_catch_sound():
    try:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    except:
        pass

def play_drop_sound():
    try:
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    except:
        pass

# Game variables
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty = 0.95
catcher_color = "blue"
catcher_width = 100
catcher_height = 100
score = 0
lives_remaining = 3
eggs = []

# Catcher setup
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2,
                       start=200, extent=140, style="arc", outline=catcher_color, width=3)

# Game UI
game_font = font.nametofont("TkFixedFont")
game_font.config(size=16, weight="bold")

score_text = c.create_text(
    10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: " + str(score))

lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font,
                           fill="darkblue", text="Lives: " + str(lives_remaining))

level_text = c.create_text(canvas_width/2, 10, anchor="n", font=game_font,
                           fill="darkred", text="Level: 1")


# Functions
def create_egg():
    """Create new egg at random X position."""
    x = randrange(10, canvas_width - egg_width - 10)
    y = 40
    color = choice(["red", "blue", "yellow", "green", "purple", "orange", "pink"])
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=color, width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)


def move_eggs():
    """Move eggs downward."""
    for egg in eggs.copy():
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg, 0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)


def egg_dropped(egg):
    """Handle when an egg hits the ground."""
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    play_drop_sound()
    if lives_remaining == 0:
        game_over()


def lose_a_life():
    """Reduce life count."""
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: " + str(lives_remaining))


def increase_score(points):
    """Increase score and difficulty."""
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    c.itemconfigure(score_text, text="Score: " + str(score))
    update_level()


def update_level():
    """Update level based on speed."""
    level = max(1, 500 // max(egg_speed, 1))
    c.itemconfigure(level_text, text="Level: " + str(level))


def check_catch():
    """Check if egg caught by catcher."""
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs.copy():
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
            play_catch_sound()
    root.after(100, check_catch)


def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)


def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)


def game_over():
    """Show Game Over and ask to restart."""
    again = messagebox.askyesno("Game Over!", f"Final Score: {score}\nPlay again?")
    if again:
        restart_game()
    else:
        root.destroy()


def restart_game():
    """Reset all game variables."""
    global score, lives_remaining, egg_speed, egg_interval, eggs
    for egg in eggs:
        c.delete(egg)
    eggs.clear()
    score = 0
    lives_remaining = 3
    egg_speed = 500
    egg_interval = 4000
    c.itemconfigure(score_text, text="Score: " + str(score))
    c.itemconfigure(lives_text, text="Lives: " + str(lives_remaining))
    c.itemconfigure(level_text, text="Level: 1")


# Bindings
c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()

# Game start
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)

root.mainloop()
