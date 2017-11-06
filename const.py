import libtcodpy as libtcod

########################################################################################################################
# SCREEN ###############################################################################################################
########################################################################################################################

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

CAMERA_WIDTH = 80
CAMERA_HEIGHT = 43

########################################################################################################################
# MAP ##################################################################################################################
########################################################################################################################

MAP_WIDTH = 100
MAP_HEIGHT = 100

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

########################################################################################################################
# FOV ##################################################################################################################
########################################################################################################################

FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

########################################################################################################################
# NPC ##################################################################################################################
########################################################################################################################

MAX_ROOM_MONSTERS = 3

########################################################################################################################
# APPEARANCE ###########################################################################################################
########################################################################################################################

#Sets the colour of the tiles out of the player's line of sight
color_dark_wall = libtcod.Color(0, 0, 100)
color_light_wall = libtcod.Color(130, 110, 50)
color_dark_ground = libtcod.Color(50, 50, 150)
color_light_ground = libtcod.Color(200, 180, 50)

########################################################################################################################
# PANEL ################################################################################################################
########################################################################################################################

BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT

MSG_X = BAR_WIDTH + 2
MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1

########################################################################################################################
# INVENTORY ############################################################################################################
########################################################################################################################

INVENTORY_WIDTH = 50

########################################################################################################################
# APPLY & OTHER ########################################################################################################
########################################################################################################################

panel = libtcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)

#The bedrock layer of the library's screen handling. Where the UI and panels are drawn
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Loomings', False)

#A buffer console whereupon the sprites will be written is drawn over the root console
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

libtcod.sys_set_fps(LIMIT_FPS)

