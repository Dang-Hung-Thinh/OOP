def check_collision(bird_rect, pipes):
    for pipe in pipes:
        top, bottom = pipe.get_rects()
        if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
            return True
    return False
