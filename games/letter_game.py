import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT = pygame.font.Font(None, 74)
LETTER_FONT = pygame.font.Font(None, 150)
COLORS = {'background': (135, 206, 235), 'character': (255, 255, 0), 'letter': (0, 0, 0)}
LETTER_SPEEDS = {'easy': 1, 'medium': 3, 'hard': 5}
LEVELS = ['easy', 'medium', 'hard']

# Load Sounds
sounds = {
    'correct': pygame.mixer.Sound(os.path.join('sounds', 'correct.wav')),
    'wrong': pygame.mixer.Sound(os.path.join('sounds', 'wrong.wav'))
}

# Game Variables
level = 'easy'
target_letter = ''
score = 0
letters = []
character_position = SCREEN_WIDTH // 2

# Screen Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Letter Learning Game for Kids')

# Character Setup
character = pygame.Rect(character_position, SCREEN_HEIGHT - 50, 50, 50)

# Function to generate random letters
def generate_random_letters(num_letters):
    return [chr(random.randint(65, 90)) for _ in range(num_letters)]

# Main Game Loop
running = True
while running:
    screen.fill(COLORS['background'])

    # Draw Character
    pygame.draw.rect(screen, COLORS['character'], character)

    # Draw Letters
    for letter in letters:
        letter['position'][1] += LETTER_SPEEDS[level]
        screen.blit(LETTER_FONT.render(letter['char'], True, COLORS['letter']), letter['position'])

        # Check if letter is caught
        if character.colliderect(pygame.Rect(letter['position'][0], letter['position'][1], 50, 50)):
            if letter['char'] == target_letter:
                score += 1
                sounds['correct'].play()
            else:
                sounds['wrong'].play()
            letters.remove(letter)

    # Generate new letters if needed
    if not letters:
        target_letter = generate_random_letters(1)[0]
        letters = [{'char': l, 'position': [random.randint(0, SCREEN_WIDTH-50), 0]} for l in generate_random_letters(5)]

    # Draw Target Letter
    screen.blit(FONT.render(f"Find: {target_letter}", True, COLORS['letter']), (10, 10))
    pygame.display.flip()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and character_position > 0:
                character_position -= 50
            if event.key == pygame.K_RIGHT and character_position < SCREEN_WIDTH - 50:
                character_position += 50

    character.x = character_position
