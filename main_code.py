import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
win_width, win_height = 1000, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pygame Button Example")

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PRIMARY = (255, 221, 210)
SECONDARY = (11, 132, 148)
TERTIARY = (18, 91, 154)
BACKGROUND_COLOR = PRIMARY

# Button Class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.action = action
        self.visible = True  # Flag to control button visibility

    def draw(self, win):
        if self.visible:  # Only draw the button if it's set to be visible
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                pygame.draw.rect(win, self.hover_color, self.rect, border_radius=10)
            else:
                pygame.draw.rect(win, self.color, self.rect, border_radius=10)

            # Draw text
            font = pygame.font.Font(None, 45)
            text_surf = font.render(self.text, True, WHITE)
            text_rect = text_surf.get_rect(center=self.rect.center)
            win.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.visible:  # Check for mouse button release
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if self.action:
                    self.action()


def bubble_sort():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = PRIMARY  # Set background to the main color
    bubble_sort_button.visible = False
    selection_sort_button.visible = False
    insertion_sort_button.visible = False
    tower_of_hanoi_button.visible = False

    array = [10 * (i + 1) for i in range(20)]  # Create an array of 10 elements
    random.shuffle(array)  # Shuffle the array to randomize
    array_length = len(array)
    bar_width = (win_width - 40) // array_length  # Set bar width based on window size
    max_value = max(array)  # Get the maximum value to scale the bar height

    sorting = True
    while sorting:
        sorting = False
        for i in range(array_length - 1):
            # Draw the background
            win.fill(BACKGROUND_COLOR)
            
            # Draw the array as vertical bars
            for j in range(array_length):
                bar_height = (array[j] / max_value) * (win_height - 40)  # Scale bar height
                bar_color = GREEN if j == i or j == i + 1 else SECONDARY  # Highlight the bars being compared
                pygame.draw.rect(win, bar_color, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))

            pygame.display.update()  # Update the display to show the sorting progress
            pygame.time.delay(500)  # Delay to slow down the visualization

            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Swap the elements
                sorting = True  # Continue sorting if a swap was made

    # Show sorted array
    win.fill(BACKGROUND_COLOR)
    for j in range(array_length):
        bar_height = (array[j] / max_value) * (win_height - 40)
        pygame.draw.rect(win, GREEN, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))

    pygame.display.update()
    pygame.time.delay(1000)  # Pause to view the sorted state

    # Return to main menu
    bubble_sort_button.visible = True
    selection_sort_button.visible = True
    insertion_sort_button.visible = True
    tower_of_hanoi_button.visible = True

    return "main_menu"  # Return to main menu


def insertion_sort():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = PRIMARY  # Set background to the main color
    bubble_sort_button.visible = False
    selection_sort_button.visible = False
    insertion_sort_button.visible = False
    tower_of_hanoi_button.visible = False

    array = [10 * (i + 1) for i in range(20)]  # Create an array of 10 elements
    random.shuffle(array)  # Shuffle the array to randomize
    array_length = len(array)
    bar_width = (win_width - 40) // array_length  # Set bar width based on window size
    max_value = max(array)  # Get the maximum value to scale the bar height

    # Insertion sort algorithm
    for i in range(1, array_length):
        key = array[i]
        key_height = (key / max_value) * (win_height - 40)  # Calculate height of the key bar
        key_pos = 20 + i * bar_width  # X position of the key bar
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

            # Draw the background
            win.fill(BACKGROUND_COLOR)

            # Draw the array as vertical bars
            for k in range(array_length):
                bar_height = (array[k] / max_value) * (win_height - 40)  # Scale bar height

                if k == i:
                    # Draw the key bar
                    pygame.draw.rect(win, GREEN, pygame.Rect(20 + k * bar_width, win_height - key_height - 20, bar_width - 2, key_height))
                elif k == j + 1:
                    # Draw the bar being compared
                    pygame.draw.rect(win, RED, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
                else:
                    # Draw other bars
                    pygame.draw.rect(win, SECONDARY, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))

            pygame.display.update()  # Update the display to show the sorting progress
            pygame.time.delay(500)  # Delay to slow down the visualization

        array[j + 1] = key

        # Draw the background
        win.fill(BACKGROUND_COLOR)

        # Draw the array as vertical bars
        for k in range(array_length):
            bar_height = (array[k] / max_value) * (win_height - 40)  # Scale bar height

            if k == i:
                # Draw the key bar
                pygame.draw.rect(win, GREEN, pygame.Rect(20 + k * bar_width, win_height - key_height - 20, bar_width - 2, key_height))
            else:
                # Draw other bars
                pygame.draw.rect(win, SECONDARY, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))

        pygame.display.update()  # Update the display to show the sorting progress
        pygame.time.delay(500)  # Delay to slow down the visualization

    # Final update to show the sorted array
    win.fill(BACKGROUND_COLOR)
    for j in range(array_length):
        bar_height = (array[j] / max_value) * (win_height - 40)
        pygame.draw.rect(win, GREEN, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))

    pygame.display.update()
    pygame.time.delay(1000)  # Pause to view the sorted state

    # Return to main menu
    bubble_sort_button.visible = True
    selection_sort_button.visible = True
    insertion_sort_button.visible = True
    tower_of_hanoi_button.visible = True


def selection_sort():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = PRIMARY  # Set background to the main color
    bubble_sort_button.visible = False
    selection_sort_button.visible = False
    insertion_sort_button.visible = False
    tower_of_hanoi_button.visible = False

    array = [10 * (i + 1) for i in range(20)]  # Create an array of 10 elements
    random.shuffle(array)  # Shuffle the array to randomize
    array_length = len(array)
    bar_width = (win_width - 40) // array_length  # Set bar width based on window size
    max_value = max(array)  # Get the maximum value to scale the bar height

    # Selection sort algorithm
    for i in range(array_length):
        min_index = i
        # Draw the background
        win.fill(BACKGROUND_COLOR)

        # Draw the array as vertical bars
        for j in range(array_length):
            bar_height = (array[j] / max_value) * (win_height - 40)  # Scale bar height
            
            # Highlight the bars being compared
            if j == i:
                pygame.draw.rect(win, RED, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
            elif j == min_index:
                pygame.draw.rect(win, GREEN, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
            else:
                pygame.draw.rect(win, SECONDARY, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
        
        pygame.display.update()  # Update the display to show the sorting progress
        pygame.time.delay(500)  # Delay to slow down the visualization

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, array_length):
            # Draw the background
            win.fill(BACKGROUND_COLOR)

            # Draw the array as vertical bars
            for k in range(array_length):
                bar_height = (array[k] / max_value) * (win_height - 40)  # Scale bar height
                
                # Highlight the bars being compared
                if k == i or k == j:
                    pygame.draw.rect(win, RED, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
                elif k == min_index:
                    pygame.draw.rect(win, GREEN, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
                else:
                    pygame.draw.rect(win, SECONDARY, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
            
            pygame.display.update()  # Update the display to show the sorting progress
            pygame.time.delay(500)  # Delay to slow down the visualization

            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]

        # Draw the background
        win.fill(BACKGROUND_COLOR)

        # Draw the array as vertical bars
        for k in range(array_length):
            bar_height = (array[k] / max_value) * (win_height - 40)  # Scale bar height
            
            if k == i or k == min_index:
                pygame.draw.rect(win, GREEN, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
            else:
                pygame.draw.rect(win, SECONDARY, pygame.Rect(20 + k * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))
        
        pygame.display.update()  # Update the display to show the sorting progress
        pygame.time.delay(500)  # Delay to slow down the visualization

    # Final update to show the sorted array
    win.fill(BACKGROUND_COLOR)
    for j in range(array_length):
        bar_height = (array[j] / max_value) * (win_height - 40)
        pygame.draw.rect(win, GREEN, pygame.Rect(20 + j * bar_width, win_height - bar_height - 20, bar_width - 2, bar_height))

    pygame.display.update()
    pygame.time.delay(1000)  # Pause to view the sorted state

    # Return to main menu
    bubble_sort_button.visible = True
    selection_sort_button.visible = True
    insertion_sort_button.visible = True
    tower_of_hanoi_button.visible = True


def visualize_tower_of_hanoi():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = PRIMARY  # Set background to the main color
    bubble_sort_button.visible = False
    selection_sort_button.visible = False
    insertion_sort_button.visible = False
    tower_of_hanoi_button.visible = False

    # Define the number of disks
    num_disks = 5
    pegs = [list(range(num_disks, 0, -1)), [], []]  # Initial configuration: all disks on peg 0

    # Define disk colors
    disk_colors = [(255, 190, 11), (251, 86, 7), (255, 0, 110), (131, 56, 236), (58, 134, 255)]

    # Define disk size
    disk_height = 50
    disk_widths = [100 + disk * 30 for disk in range(num_disks)]  # Increased disk width

    def draw_pegs_and_disks():
        win.fill(BACKGROUND_COLOR)
        peg_spacing = (win_width - 80) // 3
        peg_positions = [200 + i * peg_spacing for i in range(3)]  # Adjust to keep pegs within bounds

        # Draw disks
        for i, peg in enumerate(pegs):
            peg_x = peg_positions[i]
            for j, disk in enumerate(peg):
                disk_width = disk_widths[disk - 1]  # Width of the current disk
                pygame.draw.rect(
                    win, 
                    disk_colors[disk - 1], 
                    pygame.Rect(
                        peg_x - disk_width // 2, 
                        win_height - disk_height * (j + 1) - 30,  # Adjusted y-position to correctly stack disks
                        disk_width, 
                        disk_height
                    )
                )

        pygame.display.update()

    def move_disk(from_peg, to_peg):
        disk = pegs[from_peg].pop()
        pegs[to_peg].append(disk)
        draw_pegs_and_disks()
        pygame.time.delay(500)

    def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
        if n == 1:
            move_disk(from_peg, to_peg)
        else:
            tower_of_hanoi(n - 1, from_peg, aux_peg, to_peg)
            move_disk(from_peg, to_peg)
            tower_of_hanoi(n - 1, aux_peg, to_peg, from_peg)

    # Initial drawing
    draw_pegs_and_disks()
    
    pygame.time.delay(1000)
    
    # Start the Tower of Hanoi visualization
    tower_of_hanoi(num_disks, 0, 2, 1)

    # Pause to show the final state
    pygame.time.delay(1000)

    # Return to main menu
    bubble_sort_button.visible = True
    selection_sort_button.visible = True
    insertion_sort_button.visible = True
    tower_of_hanoi_button.visible = True


def quit():
    pygame.quit()
    sys.exit()


# Create button instances
bubble_sort_button = Button(150, 50, 300, 150, "Bubble Sort", SECONDARY, TERTIARY, lambda:bubble_sort())
selection_sort_button = Button(550, 50, 300, 150, "Selection Sort", SECONDARY, TERTIARY, lambda:selection_sort())
insertion_sort_button = Button(150, 300, 300, 150, "Insertion Sort", SECONDARY, TERTIARY, lambda:insertion_sort())
tower_of_hanoi_button = Button(550, 300, 300, 150, "Tower of Hanoi", SECONDARY, TERTIARY, lambda:visualize_tower_of_hanoi())
quit_button = Button(450, 500, 100, 50, "EXIT", SECONDARY, RED, lambda:quit())

# Main loop
current_state = "main_menu"  # Initial state

running = True
while running:
    print("Hello")
    if current_state == "main_menu":
        win.fill(BACKGROUND_COLOR)  # Fill the window with the current background color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Check for button click
            bubble_sort_button.check_click(event)
            selection_sort_button.check_click(event)
            insertion_sort_button.check_click(event)
            tower_of_hanoi_button.check_click(event)
            quit_button.check_click(event)

        # Draw buttons
        bubble_sort_button.draw(win)
        selection_sort_button.draw(win)
        insertion_sort_button.draw(win)
        tower_of_hanoi_button.draw(win)
        quit_button.draw(win)

        pygame.display.update()

    elif current_state == "visualizing":
        # This state is handled within the visualize_bubble_sort function
        current_state = bubble_sort()
