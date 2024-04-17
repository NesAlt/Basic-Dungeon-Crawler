import pygame,sys,os
from settings import *
from entity import Entity
import random
from LevelLoader import import_folder
from debug import debug

class Player(Entity):
  def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_magic):
    super().__init__(groups)
    self.image =pygame.image.load('Assets/player/player.png').convert_alpha()
    self.rect=self.image.get_rect(topleft = pos)
    self.hitbox=self.rect.inflate(0,-35)

    self.import_player_assets()
    self.status='down'

    self.game_over=False

    self.attacking=False
    self.attack_cooldown=500
    self.attack_speed=0
    self.guard=False
    self.guard_cooldown=400

    self.stats={'health':200,'agility':3,'attack':25,'mana':100,'crit ratio':5}

    self.health=self.stats['health']
    # self.armor=self.stats['armor']
    self.speed=self.stats['agility']
    self.attack=self.stats['attack']
    self.mana=self.stats['mana']
    self.crit=self.stats['crit ratio']

    self.vulnerable=True
    self.hurt_time=None
    self.invulnerablity_duration=200

    self.obstacle_sprites =obstacle_sprites

    self.create_attack=create_attack
    self.destroy_attack=destroy_attack
    self.weapon_index=0
    self.weapon=list(weapon_data.keys())[self.weapon_index]
    self.can_switch_weapon=True
    self.weapon_switch_time=None
    self.weapon_switch_cooldown=200

    self.create_magic=create_magic
    # self.destroy_magic=destroy_magic
    self.magic_index=0
    self.magic=list(magic_data.keys())[self.magic_index]
    # self.can_switch_magic=True
    # self.magic_switch_time=None

  def import_player_assets(self):
    character_path='Assets\\player'
    self.animations={'up':[],'down':[],'left':[],'right':[],
                    'up_idle':[],'down_idle':[],'left_idle':[],'right_idle':[],
                    'up_attack':[],'down_attack':[],'left_attack':[],'right_attack':[],
                    'up_guard':[],'down_guard':[],'left_guard':[],'right_guard':[]}
    
    for animation in self.animations.keys():
      full_path=character_path+'\\'+animation
      self.animations[animation]=import_folder(full_path)

  def get_status(self):
    if self.direction.x==0 and self.direction.y==0:
      if not 'idle' in self.status and not 'attack' in self.status and not 'guard' in self.status:
        self.status=self.status+'_idle'

    if self.attacking:
      self.direction.x=0
      self.direction.y=0
      if not 'attack' in self.status:
        if 'idle' in self.status:
            self.status=self.status.replace('_idle','_attack')
        elif 'guard' in self.status:
            self.status=self.status.replace('_guard','_attack')
        else:
          self.status=self.status+'_attack'
    else:
      if 'attack' in self.status:
        self.status=self.status.replace('_attack','')
    
    if self.guard:
      self.direction.x=0
      self.direction.y=0
      if not 'guard' in self.status:
        if 'idle' in self.status:
            self.status=self.status.replace('_idle','_guard')
        elif 'attack' in self.status:
            self.status=self.status.replace('_attack','_guard')
        else:
          self.status=self.status+'_guard'
    else:
      if 'guard' in self.status:
        self.status=self.status.replace('_guard','')

  def entity_input(self):
    if not self.attacking and not self.guard:
      keys = pygame.key.get_pressed()
    
      if keys[pygame.K_w] or keys[pygame.K_UP]:
        self.direction.y=-1
        self.status='up'
      elif keys[pygame.K_s]or keys[pygame.K_DOWN]:
        self.direction.y=1
        self.status='down'
      else:
        self.direction.y=0

      if keys[pygame.K_d]or keys[pygame.K_RIGHT]:
        self.direction.x=1
        self.status='right'
      elif keys[pygame.K_a]or keys[pygame.K_LEFT]:
        self.direction.x=-1
        self.status='left'
      else:
        self.direction.x=0

      if keys[pygame.K_SPACE]:
        if not self.attack_pressed_last_frame:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
        self.attack_pressed_last_frame = True
      else:
        self.attack_pressed_last_frame = False
      
      if keys[pygame.K_f]:
        self.attacking=True
        self.attack_time=pygame.time.get_ticks()
        style=list(magic_data.keys())[self.magic_index]
        amount=list(magic_data.values())[self.magic_index]['amount']
        cost=list(magic_data.values())[self.magic_index]['cost']
        self.create_magic(style,amount,cost)

      if keys[pygame.K_v]:
        self.guard=True
        self.guard_time=pygame.time.get_ticks()
      
      if keys[pygame.K_q] and self.can_switch_weapon:
        self.can_switch_weapon=False
        self.weapon_switch_time=pygame.time.get_ticks()

        if self.weapon_index<len(list(weapon_data.keys()))-1:
          self.weapon_index+=1
        else:
          self.weapon_index=0
        self.weapon=list(weapon_data.keys())[self.weapon_index]

  def cooldowns(self):
    current_time=pygame.time.get_ticks()

    if self.attacking:
      if current_time -self.attack_time >= self.attack_cooldown+weapon_data[self.weapon]['cooldown']:
        self.attacking=False
        self.destroy_attack()
    if self.guard:
      if current_time -self.guard_time >= self.guard_cooldown:
        self.guard=False
    if not self.can_switch_weapon:
      if current_time-self.weapon_switch_time>=self.weapon_switch_cooldown:
        self.can_switch_weapon=True

    if not self.vulnerable:
      if current_time-self.hurt_time>=self.invulnerablity_duration:
        self.vulnerable=True
    
  def animate(self):
    animation=self.animations[self.status]

    self.frame_index+=self.animation_speed
    if self.frame_index>= len(animation):
      self.frame_index=0

    self.image=animation[int(self.frame_index)]
    self.rect=self.image.get_rect(center=self.hitbox.center)

    if not self.vulnerable:
      alpha=self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)

  def mana_regen(self):
    if self.mana<self.stats['mana']:
      self.mana+=0.05
    else:
      self.mana=self.stats['mana']

  def get_full_weapon_damage(self):
    base_damage=self.stats['attack']
    weapon_damage=weapon_data[self.weapon]['damage']
    crit_ratio=weapon_data[self.weapon]['crit ratio']
    if random.random() < crit_ratio / 100:
      val=base_damage+weapon_damage*2
      # print(f'crit damage={val}')
      return val
    else:
      val=base_damage+weapon_damage
      # print(f'damage={val}')
      return val

  def update(self):
    self.entity_input()
    self.cooldowns()
    self.get_status()
    self.animate()
    self.move(self.speed)
    self.mana_regen()