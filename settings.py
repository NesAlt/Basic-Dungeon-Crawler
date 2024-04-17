import pygame
pygame.font.init()

WIDTH=1024
HEIGHT=768
FPS=60
TILESIZE=32

BAR_HEIGHT=20
HEALTH_BAR_WIDTH=200
MANA_BAR_WIDTH=100
# ARMOR_RATING=20
ITEM_BOX_SIZE=80
UI_FONT='Assets/fonts/ui fonts/joystix monospace.ttf'
UI_FONT_SIZE=18

BUTTON_FONT_SIZE=10
BUTTON_FONT = pygame.font.Font('Assets/fonts/ui fonts/joystix monospace.ttf', BUTTON_FONT_SIZE)

WATER_COLOR='#71ddee'
UI_BG_COLOR='#222222'
UI_BORDER_COLOR='#111111'
TEXT_COLOR='#EEEEEE'

HEALTH_COLOR='red'
MANA_COLOR='blue'
# ARMOR_COLOR='silver'
UI_BORDER_ACTIVE_COLOR='gold'

LEVELS = ['MainMap','CityMap','ForestMap']

weapon_data={
  'sword':{'cooldown':100,'damage':15,'crit ratio':5,'graphic':'Assets/weapons/sword/sword.png'},
  'spear':{'cooldown':600,'damage':25,'crit ratio':10,'graphic':'Assets/weapons/spear/spear.png'},
  'dagger':{'cooldown':50,'damage':8,'crit ratio':15,'graphic':'Assets/weapons/dagger/dagger.png'},
  'staff':{'cooldown':100,'damage':5,'crit ratio':5,'graphic':'Assets/weapons/staff/staff.png'},
  'shotgun':{'cooldown':80,'damage':12,'crit ratio':0,'graphic':'Assets/weapons/shotgun/shotgun.png'}}

magic_data={
  'heal':{'amount':50,'cost':50,'graphic':'Assets\particles\heal\heal.png'}
}

monster_data = {
	'elite guard': {'health': 500,'damage':15,'exp':0,'attack_type': 'slam','cooldown':600, 'speed': 0.4, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 250},
	'knight': {'health': 150,'damage':5,'exp':8,'attack_type': 'slash','cooldown':100, 'speed': 1.5, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 500},
	'zombie': {'health': 80,'damage':3,'exp':5,'attack_type': 'punch','cooldown':80, 'speed': 2, 'resistance': 1, 'attack_radius': 20, 'notice_radius': 350},
	'zombie king': {'health': 380,'damage':10,'exp':20,'attack_type': 'claw','cooldown':500, 'speed': 0.5, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
  'worm': {'health': 450,'damage':12,'exp':20,'attack_type': 'crunch','cooldown':350, 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 450},
  'slime': {'health': 50,'damage':2,'exp':3,'attack_type': 'slash','cooldown':50, 'speed': 2.5, 'resistance': 1, 'attack_radius': 20, 'notice_radius': 500}
  }