### Tree file
- miniproject/
  - __pycache__/
  - assets/
    - bird.png
    - pipe_bottom.png
    - pipe_top.png
  - utils/
    - __pycache__/
    - __init__.py
    - collision.py
  - bird.py
  - game.py
  - main.py
  - pipe.py
  - settings.py
<br>

### setting.py

```python
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_GAP = 150
```
JUMP_STRENGTH: The force applied by the space key, PIPE_GAP: The distance between two pipes (top and bottom)

### bird.py
- Define the bird's behavior: fall down, jump up, draw on the screen
- Protect internal data using encapsulation
```python
import pygame
import os
from settings import GRAVITY, JUMP_STRENGTH

class Bird:
    def __init__(self, x, y):
        # Vị trí khởi tạo
        self.__x = x
        self.__y = y
        
        # Vận tốc rơi (tăng dần do trọng lực)
        self.__velocity = 0

        # Load hình ảnh chim
        CURRENT_DIR = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(CURRENT_DIR, "assets", "bird.png"))

    def update(self):
        """Cập nhật vị trí chim theo thời gian (do trọng lực)"""
        self.__velocity += GRAVITY
        self.__y += self.__velocity

    def jump(self):
        """Khi nhấn Space, chim nhảy lên (đảo chiều vận tốc)"""
        self.__velocity = JUMP_STRENGTH

    def get_position(self):
        """Trả về vị trí hiện tại của chim (dùng để vẽ hoặc kiểm tra va chạm)"""
        return self.__x, self.__y

    def draw(self, screen):
        """Vẽ chim lên màn hình"""
        screen.blit(self.image, (self.__x, self.__y))
```
