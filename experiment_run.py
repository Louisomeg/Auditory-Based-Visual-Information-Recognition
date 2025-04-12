import pygame
import os
import csv
import time
import sys

def load_pattern_images(pattern_dir):
    # Load all PNG files in the directory
    pattern_files = [f for f in os.listdir(pattern_dir) if f.endswith(".png")]
    pattern_files.sort()  # Sort for consistency
    return pattern_files

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up full-screen display mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Acoustic Signal Experiment")
    
    # Directory where the pattern images are stored
    pattern_dir = "patterns"
    if not os.path.exists(pattern_dir):
        print("Pattern directory not found. Please run generate_patterns.py first.")
        sys.exit(1)
        
    pattern_files = load_pattern_images(pattern_dir)
    
    # Open a CSV file to log timestamps
    log_filename = "experiment_log.csv"
    with open(log_filename, mode="w", newline="") as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow(["Pattern Filename", "Display Start Time", "Display End Time"])
        
        # Set display duration per image (in seconds)
        display_duration = 5  
        
        # Loop through each pattern image and display it
        for pattern_file in pattern_files:
            image_path = os.path.join(pattern_dir, pattern_file)
            image = pygame.image.load(image_path)
            
            # Scale the image to full screen (if needed)
            screen_width, screen_height = screen.get_size()
            image = pygame.transform.scale(image, (screen_width, screen_height))
            
            # Clear any pending events
            pygame.event.clear()
            
            # Record the start time and begin display loop
            start_time = time.time()
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
                    # Pressing the ESC key exits the experiment
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit(0)
                screen.blit(image, (0, 0))
                pygame.display.flip()
                
                # After the set duration, exit the display loop for this image
                if time.time() - start_time >= display_duration:
                    running = False
            
            end_time = time.time()
            log_writer.writerow([pattern_file, start_time, end_time])
            csvfile.flush()  # Save progress after each pattern

    pygame.quit()
    print("Experiment completed. Timestamp log saved in", log_filename)

if __name__ == "__main__":
    main()
