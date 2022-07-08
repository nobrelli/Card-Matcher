import pygame as pg
from random import randint, choice

from .cdtimer import CountDownTimer
from .progress_bar import ProgressBar
from .card import Card
from gui import Point, Size


class CardGrid:
    CARD_W = 50
    CARD_H = 50
    COLORS = (
        (76, 58, 81),
        (119, 67, 96),
        (178, 80, 104),
        (231, 171, 121)
    )

    def __init__(self, canvas, position, time, rows, cols, spacing=5):
        self.canvas = canvas

        # Left-top position
        self.position: Point = position

        # No. of rows & columns
        self.rows = rows
        self.cols = cols

        # The grid size
        self.gsize = rows * cols

        # For working with pairs
        self.total_pairs = self.gsize // 2

        # The grid size must be even so that all cards have their pairs
        if self.gsize % 2 != 0:
            raise ValueError('The grid size must be even.')

        # Spacing between the cards
        self.spacing = spacing

        # Calculate the total grid dimensions (+spacing)
        self.gdim = Size(
            ((self.spacing + CardGrid.CARD_W) * cols) + self.spacing,
            ((self.spacing + CardGrid.CARD_H) * rows) + self.spacing
        )

        # Cards container
        self.cards = []

        # A pair of cards that have been clicked will be put here, just to keep track of them
        self.pair = [None, None]

        # The number of pair matches made
        # This should equal to the half of the grid size to win
        self.matches = 0

        # Game's progress indicator
        self.prog_bar = ProgressBar(Point(), Size(canvas.get_width(), 20), pg.Color(178, 80, 104))

        tbar_pos = Point(0, canvas.get_height() - 20)
        self.timer_bar = ProgressBar(tbar_pos, Size(canvas.get_width(), 20), pg.Color(178, 80, 104), pg.Color(255, 0, 0))

        self.time_limit = 1000 * time  # ms
        self._hint_time = 3000
        self.time_before_bonus = .45  # 45%
        self.time_bonus = 2000

        self.main_timer = CountDownTimer(self.time_limit, self.declare_lost)
        self._hint_timer = CountDownTimer(self._hint_time, self.hide_cards)
        self.losing_time = CountDownTimer(300, self.timer_bar.toggle_state, True)

        self._font = pg.font.SysFont('Arial-Black', 20)

        # Create the cards
        self.make_cards()

        # The board under the cards
        self.board = pg.Rect(0, 0, 0, 0)

        self._on_win = None
        self._on_lose = None

        # Sounds
        self.flip_snd = pg.mixer.Sound('././assets/sounds/flip7.ogg')
        self.won_snd = pg.mixer.Sound('././assets/sounds/won.ogg')
        self.lost_snd = pg.mixer.Sound('././assets/sounds/lost.ogg')
        self.match_snd = pg.mixer.Sound('././assets/sounds/matched.ogg')

    @property
    def on_win(self):
        return self._on_win

    @on_win.setter
    def on_win(self, func):
        if not callable(func):
            raise Exception('Must be a function')

        self._on_win = func

    @property
    def on_lose(self):
        return self._on_lose

    @on_lose.setter
    def on_lose(self, func):
        if not callable(func):
            raise Exception('Must be a function')

        self._on_lose = func

    def hide_cards(self):
        for card in self.cards:
            if not card.paired and card.is_flipped():
                card.flip()

    def show_cards(self):
        self.main_timer.pause()
        for card in self.cards:
            if not card.paired and not card.is_flipped():
                card.flip()

    def handle_event(self, event):
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if event.button == pg.BUTTON_LEFT:
                    # Only detect if the cursor is on/inside the board
                    if self.board.collidepoint(pg.mouse.get_pos()):
                        self.select_card()

    def update(self, time):
        # self._hint_timer.update()

        if self.main_timer.started:
            self.main_timer.update()

            # Update the main_timer bar
            self.timer_bar.progress = self.main_timer.remaining / self.time_limit
            self.timer_bar.update(time)

            if self.timer_bar.progress <= self.time_before_bonus and not self.losing_time.started:
                self.losing_time.start()

            if self.losing_time.started:
                self.losing_time.update()

        self.prog_bar.update(time)

    def render(self):
        # Draw the board
        self.board = pg.draw.rect(self.canvas, self.COLORS[0], (
            self.position.X - self.gdim.width / 2,
            self.position.Y - self.gdim.height / 2,
            self.gdim.width,
            self.gdim.height
        ))

        # Draw each card
        for card in self.cards:
            card.render(self.canvas)

        self.prog_bar.render(self.canvas)
        self.timer_bar.render(self.canvas)

    def update_progress(self):
        self.matches += 1
        self.prog_bar.progress = self.matches / self.total_pairs

        if self.timer_bar.progress <= self.time_before_bonus:
            self.main_timer.add(self.time_bonus)

    def declare_win(self):
        self.won_snd.play()
        self.main_timer.stop()
        self.losing_time.stop()
        self.on_win()

    def declare_lost(self):
        self.lost_snd.play()
        self.main_timer.stop()
        self.losing_time.stop()
        self.on_lose()

    def pause(self):
        self.main_timer.pause()

    def resume(self):
        self.main_timer.resume()

    def select_card(self):
        if not self._hint_timer.started:
            for card in self.cards:
                # The player clicks on a card...
                if card.detect_click() and not card.paired:
                    # Start the main_timer on click
                    if not self.main_timer.started:
                        self.main_timer.start()

                    # Flip the card
                    card.flip()
                    self.flip_snd.play()

                    # Set this card as the first member of the "clicked pair"
                    # if and only if the pair container is empty. If it's full, flip back
                    # the existing members, replace the first member with a newly clicked
                    # card and remove the second member.
                    if not self.pair[0] and not self.pair[1]:
                        self.pair[0] = card
                    elif self.pair[0] and self.pair[1]:
                        # Flip back and remove
                        # Don't flip if they've already been matched
                        if not self.pair[0].paired and not self.pair[1].paired:
                            self.pair[0].flip()
                            self.pair[1].flip()

                        self.pair[0] = card
                        self.pair[1] = None
                    # If this is the second member of the pair...
                    # elif self.pair[0]:
                    else:
                        # If it's the same card again, ignore it
                        if self.pair[0].address != card.address:
                            self.pair[1] = card

                            # Check if the pair match
                            if self.pair[0].text == self.pair[1].text:
                                # The pair will not be clickable anymore
                                self.pair[0].paired = True
                                self.pair[1].paired = True

                                self.update_progress()
                                if self.matches == self.total_pairs:
                                    self.declare_win()
                                else:
                                    self.match_snd.play()
                        else:
                            self.pair[0] = None

    def make_cards(self):
        # available numbers to choose from
        available = [*range(1, self.total_pairs + 1)]

        # for already occupied cells
        occupied = []

        for _ in range(self.total_pairs):
            # Generate a random color & number for the pair
            pair_color = choice(self.COLORS)
            pair_num = choice(available)

            # Remove the randomly generated number so that
            # it won't be picked up again.
            available.remove(pair_num)

            # Generate a cell for element of a pair
            for _ in range(2):
                # Generate a random row and column (cell).
                # Keep generating if that cell is already taken.
                while True:
                    rand_cell = (
                        randint(0, self.rows - 1),
                        randint(0, self.cols - 1)
                    )

                    if rand_cell not in occupied:
                        occupied.append(rand_cell)
                        break

                # Make a card
                card = Card(self._font)
                card.address = rand_cell
                card.color = pair_color
                card.text = str(pair_num)

                # Position the card in the grid
                card.rect = pg.Rect(
                    ((self.spacing + CardGrid.CARD_W) * rand_cell[1]) +
                    self.spacing + (self.position.X - self.gdim.width / 2),
                    ((self.spacing + CardGrid.CARD_H) * rand_cell[0]) +
                    self.spacing + (self.position.Y - self.gdim.height / 2),
                    CardGrid.CARD_W, CardGrid.CARD_H
                )

                # Add the card to the container
                self.cards.append(card)
