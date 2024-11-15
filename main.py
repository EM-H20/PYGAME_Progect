import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game")

# 색상 정의 (RGB 형식)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 플레이어 설정
player = {
    'rect': pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT-50, 50, 50),  # x, y, 너비, 높이
    'color': BLUE,
    'speed': 5
}

# 적(enemy) 설정
enemy = {
    'rect': pygame.Rect(random.randint(0, SCREEN_WIDTH-50), 0, 30, 30),
    'color': RED,
    'speed': 3
}

# 게임 상태
score = 0
clock = pygame.time.Clock()  # 프레임 조절을 위한 Clock 객체

# 게임 루프
running = True
while running:
    # 1. 이벤트 처리
    for event in pygame.event.get():
        # 창 닫기 버튼을 눌렀을 때
        if event.type == pygame.QUIT:
            running = False
    
    # 2. 키보드 입력 처리
    keys = pygame.key.get_pressed()
    # 왼쪽 화살표 키
    if keys[pygame.K_LEFT] and player['rect'].left > 0:
        player['rect'].x -= player['speed']
    # 오른쪽 화살표 키
    if keys[pygame.K_RIGHT] and player['rect'].right < SCREEN_WIDTH:
        player['rect'].x += player['speed']
    
    # 3. 게임 로직 업데이트
    # 적 이동
    enemy['rect'].y += enemy['speed']
    # 적이 화면 밖으로 나갔을 때
    if enemy['rect'].top > SCREEN_HEIGHT:
        enemy['rect'].x = random.randint(0, SCREEN_WIDTH-30)
        enemy['rect'].y = 0
        score += 1
    
    # 충돌 감지
    if player['rect'].colliderect(enemy['rect']):
        print(f"Game Over! Score: {score}")
        running = False
    
    # 4. 화면 그리기
    # 배경 채우기
    screen.fill(WHITE)
    # 플레이어 그리기
    pygame.draw.rect(screen, player['color'], player['rect'])
    # 적 그리기
    pygame.draw.rect(screen, enemy['color'], enemy['rect'])
    # 점수 표시
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # 화면 업데이트
    pygame.display.flip()
    
    # FPS 설정 (60프레임)
    clock.tick(60)

# Pygame 종료
pygame.quit()