class Player:

    def __init__(self, name):
        self.name = name
        self._lives = 3  # so that python knows its for private use
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:

            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            x = level - self._level
            self._level = level
            self._score += (1000 * x)
        else:
            print("Level cant be negative")
            self._level = 1

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0._lives}, Level: {0.level}, score: {0.score}".format(self)
