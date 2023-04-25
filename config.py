import pathlib

TOKEN = "" # Your bot's token here
PREFIX = "" # Your desired prefix here

MODERATOR =  [] # Your Moderator role's id here
ADMIN =  [] # Your Admin role's id here

EMBED_COLOR = "discord.Color.random()" # Your desired color's integer value(leave as it is for random color everytime)

# List of slap gifs(add custom as per your choice)
SLAP_GIFS = [
    "https://media.giphy.com/media/gSIz6gGLhguOY/giphy.gif",
    "https://media.giphy.com/media/mEtSQlxqBtWWA/giphy.gif",
    "https://media.giphy.com/media/lX03hULhgCYQ8/giphy.gif",
    "https://media.giphy.com/media/Qumf2QovTD4QxHPjy5/giphy.gif",
    "https://media.giphy.com/media/uqSU9IEYEKAbS/giphy.gif",
    "https://media.giphy.com/media/XDRoTw2Fs6rlIW7yQL/giphy.gif",
    "https://media.giphy.com/media/qyjexFwQwJp9yUvMxq/giphy.gif",
    "https://media.giphy.com/media/Qs0I2VdbIqNkk/giphy.gif",
    "https://media.giphy.com/media/l4FGKYL37dnOyjkty/giphy.gif",
    "https://media.giphy.com/media/vi2ciYHi5u0FO/giphy.gif"
    ]

# List of punch gifs(add custom as per your choice)
PUNCH_GIFS = [
    "",
    "",
    ""
]

# List of kill gifs(add custom as per your choice)
KILL_GIFS = [
    "",
    "",
    ""
]

# Rooting to main directory and the "cogs" folder
MAIN_DIR = pathlib.Path(__file__).parent
COGS_DIR = MAIN_DIR / "cogs"