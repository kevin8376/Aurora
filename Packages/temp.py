from Aurora.Packages.dependencies import *

# -------------------------------------------------------------

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen_height = screen.get_height() - 40
screen_width = screen.get_width()


def sh(percentage):
    """Takes fraction of screen height in percentage
     and returns the corresponding value in pixels."""
    return int(percentage*screen_height/100)


def sw(percentage):
    """Takes fraction of screen width in percentage
    and returns the corresponding value in pixels."""
    return int(percentage*screen_width/100)


def pix_w(pix):
    """Takes fraction of screen width in pixels
    and returns the corresponding value in percentage."""
    return pix*(100/screen_width)


def pix_h(pix):
    """Takes fraction of screen height in pixels
    and returns the corresponding value in percentage."""
    return pix*(100/screen_height)

# ----------------------------------------------------------


def hover_place(icon, rect, hover=True):
    """This function places an image over a rect,
    The images placed have a default hover effect which can be removed."""
    if hover and rect.collidepoint(pygame.mouse.get_pos()):
        hicon = icon.copy()
        hicon.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
        screen.blit(hicon, rect)
    else:
        screen.blit(icon, rect)


def clicked(attacks, x, y):
    """Calls the attack method of a image in a given sequence if it has been clicked"""
    for i in range(len(attacks)):
        if attacks[i].rect.collidepoint(x, y):
            attacks[i].attack()
            break


def mass_place(seq):
    """Places an array of images on screen"""
    for i in range(len(seq)):
        seq[i].place()


# ----------------------------------------------------------
class GameLoop(object):
    running = True

    @classmethod
    def handle_quit(cls, event):
        if event.type == pygame.QUIT:
            cls.running = False


class Control(object):
    """Class to manage all control icons"""
    def __init__(self, y, file):
        base_dir = 'Images/icons/'
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(y - (self.icon.get_height() / 2))
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

    def place(self):
        """Place an instance of the class on specified rect"""
        hover_place(self.icon, self.rect)


class Text(object):
    """Class to handle to Text Output"""
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.SysFont('showcardgothic', self.size)
        self.text = ''
        self.color = (255, 255, 255)

    def write(self, txt):
        """Add to string"""
        self.text += txt

    def clear(self):
        """Clear the text string"""
        self.text = ''

    def render(self):
        """Renders text on the screen"""
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))


class Planet(object):
    def __init__(self, file, base_rating):
        base_dir = 'Images/Planet/'
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(sh(2) + 128 - (self.icon.get_height() / 2))
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

        self.base_rating = base_rating
        self.damage = base_rating*0.1
        self.health = base_rating
        self.defence = base_rating*0.01

    def place(self):
        screen.blit(self.icon, self.rect)

    def attack(self):
        pass


class Attacks(object):
    def __init__(self, x, y, file, base_dir, base_rating):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.rect = self.icon.get_rect()
        self.rect.top = self.y - self.icon.get_width()/2
        self.rect.left = self.x - self.icon.get_height()/2
        self.base_Rating = base_rating
        self.damage = self.base_Rating

    def place(self):
        hover_place(self.icon, self.rect)

    def attack(self):
        print(self)
        pass


class Spell(Attacks):
    def __init__(self, x, y, file, base_rating=0):
        base_dir = 'Images/32px/'
        super().__init__(x, y, file, base_dir, base_rating)


class Troop(Attacks):
    def __init__(self, x, y, file, base_rating):
        base_dir = 'Images/32px/'
        super().__init__(x, y, file, base_dir, base_rating)
        self.defence = self.base_Rating*0.5
        self.health = self.base_Rating*0.75

        troop_dir = 'Images/64px/'
        self.img = pygame.image.load(os.path.join(troop_dir, file)).convert_alpha()
        self.rectT = self.img.get_rect()
