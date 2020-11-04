# -*- coding:utf-8 -*- 
import pygame
from settings import Settings
from game_stats import GameStats
from pygame.sprite import Group
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    ai_settings = Settings()
    pygame.init()
    # ���ڴ�С
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    bg_color = (230, 230, 230)
    alien = Alien(ai_settings, screen)
    # ��ѭ��
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)  # 1
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)  # 2 12����˳��һ����ʲô�鰡������


run_game()
