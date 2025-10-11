import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

UI_BLACK = (20, 20, 20)
UI_WHITE = (240, 240, 240)
UI_BLUE = (70, 130, 180)
UI_GREEN = (50, 205, 50)
UI_RED = (220, 20, 60)
UI_YELLOW = (255, 215, 0)
UI_ORANGE = (255, 140, 0)
UI_PURPLE = (138, 43, 226)
UI_CYAN = (0, 255, 255)


class Car:
    def __init__(self, x, y, color, is_player=False):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.color = color
        self.speed = 0
        self.max_speed = 8
        self.acceleration = 0.3
        self.deceleration = 0.2
        self.turn_speed = 3
        self.angle = 0
        self.is_player = is_player
        self.health = 100
        
        if is_player:
            self.image = pygame.image.load("assets/topcar.png")
        else:
            if color == RED:
                self.image = pygame.image.load("assets/redcar2.png")
            elif color == BLUE:
                self.image = pygame.image.load("assets/bluecar.png")
            elif color == YELLOW:
                self.image = pygame.image.load("assets/yellowcar.png")
            else:
                self.image = pygame.image.load("assets/redcar2.png")
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def add_health(self, amount):
        self.health = min(100, self.health + amount)

    def update(self, keys=None):
        if self.is_player and keys:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.speed += self.acceleration
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.speed -= self.acceleration

            if abs(self.speed) > 0.1:
                turn_multiplier = 1 if self.speed >= 0 else -1
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.angle -= self.turn_speed * turn_multiplier
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.angle += self.turn_speed * turn_multiplier
        else:
            pass

        self.speed = max(-self.max_speed/2, min(self.max_speed, self.speed))

        if self.is_player and not (keys and
                (keys[pygame.K_UP] or keys[pygame.K_w] or
                 keys[pygame.K_DOWN] or keys[pygame.K_s])):
            self.speed *= 0.95

        if self.is_player:
            angle_rad = math.radians(self.angle)
            self.x += self.speed * math.sin(angle_rad)
            self.y -= self.speed * math.cos(angle_rad)
        else:
            self.y += self.speed

        if self.is_player:
            self.x = max(150 + 30, min(SCREEN_WIDTH - 155 - 30, self.x))
            self.y = max(50, min(SCREEN_HEIGHT - 50, self.y))

    def draw(self, screen):
        rotated_car = pygame.transform.rotate(self.image, -self.angle)
        car_rect = rotated_car.get_rect(center=(self.x, self.y))

        screen.blit(rotated_car, car_rect)

    def get_rect(self):
        hitbox_size = 40
        return pygame.Rect(self.x - hitbox_size//2, self.y - hitbox_size//2,
                           hitbox_size, hitbox_size)


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.color = RED

    def update(self):
        self.y += 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLACK,
                         (self.x, self.y, self.width, self.height), 2)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class PowerUp:
    def __init__(self, x, y, power_type):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.power_type = power_type
        self.colors = {'speed': YELLOW, 'health': GREEN, 'shield': BLUE}
        self.color = self.colors[power_type]

    def update(self):
        self.y += 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x + self.width//2, self.y + self.height//2),
                           self.width//2)
        pygame.draw.circle(screen, BLACK,
                           (self.x + self.width//2, self.y + self.height//2),
                           self.width//2, 2)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Car Racing Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Car(SCREEN_WIDTH//2, SCREEN_HEIGHT - 100, BLUE, True)
        self.enemy_cars = []
        self.obstacles = []
        self.power_ups = []

        self.score = 0
        self.level = 1
        self.obstacle_timer = 0
        self.power_up_timer = 0
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        self.road_lines = []
        for i in range(0, SCREEN_HEIGHT, 50):
            self.road_lines.append(i)

    def spawn_enemy_car(self):
        base_spawn_chance = 0.4
        max_cars = 5
        
        level_multiplier = 1 + (self.level - 1) * 0.2
        spawn_chance = min(0.8, base_spawn_chance * level_multiplier)
        max_cars = min(8, max_cars + (self.level - 1))
        
        if random.random() < spawn_chance and len(self.enemy_cars) < max_cars:
            x = random.randint(150 + 30, SCREEN_WIDTH - 155 - 30)
            y = -100
            color = random.choice([RED, BLUE, YELLOW])
            enemy_car = Car(x, y, color)
            base_speed = random.uniform(4, 7)
            speed_boost = (self.level - 1) * 0.5
            enemy_car.speed = base_speed + speed_boost
            self.enemy_cars.append(enemy_car)

    def spawn_obstacle(self):
        pass

    def spawn_power_up(self):
        if random.random() < 0.1:
            x = random.randint(150 + 15, SCREEN_WIDTH - 155 - 15)
            power_type = random.choice(['speed', 'health', 'shield'])
            self.power_ups.append(PowerUp(x, -50, power_type))

    def handle_collisions(self):
        player_rect = self.player.get_rect()

        for enemy in self.enemy_cars[:]:
            if player_rect.colliderect(enemy.get_rect()):
                self.player.health -= 20
                self.enemy_cars.remove(enemy)
                if self.player.health <= 0:
                    self.game_over()

        for power_up in self.power_ups[:]:
            if player_rect.colliderect(power_up.get_rect()):
                if power_up.power_type == 'speed':
                    self.player.max_speed += 1
                elif power_up.power_type == 'health':
                    self.player.add_health(30)
                elif power_up.power_type == 'shield':
                    self.player.add_health(10)
                self.power_ups.remove(power_up)
                self.score += 50

    def update(self):
        keys = pygame.key.get_pressed()

        self.player.update(keys)

        for enemy in self.enemy_cars[:]:
            enemy.update()
            if enemy.y > SCREEN_HEIGHT + 50:
                self.enemy_cars.remove(enemy)
                self.score += 10

        for power_up in self.power_ups[:]:
            power_up.update()
            if power_up.y > SCREEN_HEIGHT:
                self.power_ups.remove(power_up)

        self.obstacle_timer += 1
        self.power_up_timer += 1

        base_spawn_interval = 60
        level_speed_boost = (self.level - 1) * 5
        spawn_interval = max(30, base_spawn_interval - level_speed_boost)
        
        if self.obstacle_timer > spawn_interval:
            self.spawn_enemy_car()
            self.obstacle_timer = 0

        if self.power_up_timer > 180:
            self.spawn_power_up()
            self.power_up_timer = 0

        self.handle_collisions()

        self.score += 1

        if self.score > self.level * 1000:
            self.level += 1

    def draw_road(self):
        pygame.draw.rect(self.screen, DARK_GRAY,
                         (150, 0, SCREEN_WIDTH - 300, SCREEN_HEIGHT))

        for line_y in self.road_lines:
            pygame.draw.rect(self.screen, YELLOW,
                             (SCREEN_WIDTH//2 - 2, line_y, 4, 30))

        pygame.draw.rect(self.screen, WHITE, (150, 0, 5, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, WHITE,
                         (SCREEN_WIDTH - 155, 0, 5, SCREEN_HEIGHT))

    def draw(self):
        self.screen.fill(UI_BLACK)
        
        self.draw_road()

        for enemy in self.enemy_cars:
            enemy.draw(self.screen)

        for power_up in self.power_ups:
            power_up.draw(self.screen)

        self.player.draw(self.screen)

        self.draw_ui()

        pygame.display.flip()

    def draw_ui(self):
        self.draw_ui_panels()
        self.draw_score()
        self.draw_level()
        self.draw_health_bar()
        self.draw_speed_indicator()
        self.draw_controls()
        self.draw_power_up_indicators()

    def draw_ui_panels(self):
        pygame.draw.rect(self.screen, UI_BLACK, (5, 5, 200, 120), 0)
        pygame.draw.rect(self.screen, UI_BLUE, (5, 5, 200, 120), 3)
        
        pygame.draw.rect(self.screen, UI_BLACK, (SCREEN_WIDTH - 205, 5, 200, 80), 0)
        pygame.draw.rect(self.screen, UI_BLUE, (SCREEN_WIDTH - 205, 5, 200, 80), 3)

    def draw_score(self):
        score_text = self.font.render(f"SCORE", True, UI_CYAN)
        self.screen.blit(score_text, (15, 15))
        
        score_value = self.font.render(f"{self.score:,}", True, UI_WHITE)
        self.screen.blit(score_value, (15, 45))

    def draw_level(self):
        level_text = self.font.render(f"LEVEL", True, UI_YELLOW)
        self.screen.blit(level_text, (15, 75))
        
        level_value = self.font.render(f"{self.level}", True, UI_WHITE)
        self.screen.blit(level_value, (15, 105))

    def draw_health_bar(self):
        bar_x, bar_y = 15, 140
        bar_width, bar_height = 170, 20
        
        pygame.draw.rect(self.screen, UI_BLACK, (bar_x, bar_y, bar_width, bar_height), 0)
        pygame.draw.rect(self.screen, UI_WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
        
        health_percentage = self.player.health / 100.0
        fill_width = int(bar_width * health_percentage)
        
        if health_percentage > 0.6:
            health_color = UI_GREEN
        elif health_percentage > 0.3:
            health_color = UI_YELLOW
        else:
            health_color = UI_RED
            
        pygame.draw.rect(self.screen, health_color, (bar_x + 2, bar_y + 2, fill_width - 4, bar_height - 4), 0)
        
        health_text = self.small_font.render(f"HEALTH: {self.player.health}/100", True, UI_WHITE)
        self.screen.blit(health_text, (bar_x, bar_y + 25))

    def draw_speed_indicator(self):
        speed = abs(self.player.speed)
        max_speed = self.player.max_speed
        
        bar_x, bar_y = 15, 180
        bar_width, bar_height = 170, 15
        
        pygame.draw.rect(self.screen, UI_BLACK, (bar_x, bar_y, bar_width, bar_height), 0)
        pygame.draw.rect(self.screen, UI_WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
        
        speed_percentage = speed / max_speed
        fill_width = int(bar_width * speed_percentage)
        
        if speed_percentage > 0.7:
            speed_color = UI_RED
        elif speed_percentage > 0.4:
            speed_color = UI_YELLOW
        else:
            speed_color = UI_GREEN
            
        pygame.draw.rect(self.screen, speed_color, (bar_x + 2, bar_y + 2, fill_width - 4, bar_height - 4), 0)
        
        speed_text = self.small_font.render(f"SPEED: {speed:.1f}", True, UI_WHITE)
        self.screen.blit(speed_text, (bar_x, bar_y + 20))

    def draw_controls(self):
        controls_title = self.small_font.render("CONTROLS", True, UI_CYAN)
        self.screen.blit(controls_title, (SCREEN_WIDTH - 195, 15))
        
        controls_text = self.small_font.render("WASD / Arrow Keys", True, UI_WHITE)
        self.screen.blit(controls_text, (SCREEN_WIDTH - 195, 35))
        
        controls_text2 = self.small_font.render("ESC to quit", True, UI_WHITE)
        self.screen.blit(controls_text2, (SCREEN_WIDTH - 195, 55))

    def draw_power_up_indicators(self):
        speed_boosts = self.player.max_speed - 8
        if speed_boosts > 0:
            boost_text = self.small_font.render(f"SPEED BOOSTS: {speed_boosts}", True, UI_YELLOW)
            self.screen.blit(boost_text, (SCREEN_WIDTH - 195, 80))
        
        if self.level > 1:
            difficulty_text = self.small_font.render(f"DIFFICULTY: {self.level}x", True, UI_ORANGE)
            self.screen.blit(difficulty_text, (SCREEN_WIDTH - 195, 100))

    def game_over(self):
        self.running = False
        self.screen.fill(UI_BLACK)
        
        panel_width, panel_height = 400, 300
        panel_x = (SCREEN_WIDTH - panel_width) // 2
        panel_y = (SCREEN_HEIGHT - panel_height) // 2
        
        pygame.draw.rect(self.screen, UI_BLACK, (panel_x, panel_y, panel_width, panel_height), 0)
        pygame.draw.rect(self.screen, UI_RED, (panel_x, panel_y, panel_width, panel_height), 5)
        
        game_over_text = self.font.render("GAME OVER", True, UI_RED)
        title_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, panel_y + 60))
        self.screen.blit(game_over_text, title_rect)
        
        final_score_text = self.font.render(f"Final Score: {self.score:,}", True, UI_WHITE)
        score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, panel_y + 120))
        self.screen.blit(final_score_text, score_rect)
        
        level_text = self.small_font.render(f"Level Reached: {self.level}", True, UI_YELLOW)
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH//2, panel_y + 150))
        self.screen.blit(level_text, level_rect)
        
        restart_text = self.small_font.render("Press SPACE to restart", True, UI_CYAN)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, panel_y + 200))
        self.screen.blit(restart_text, restart_rect)
        
        quit_text = self.small_font.render("Press ESC to quit", True, UI_CYAN)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, panel_y + 220))
        self.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                        self.restart_game()
                    elif event.key == pygame.K_ESCAPE:
                        waiting = False
                        self.running = False

    def restart_game(self):
        self.__init__()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()