import random
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Suppress Pygame startup message
pygame.mixer.init()

# Define the audio files for each number and their lifted versions
audio_files = {
    '0': '0.wav',
    '1': '1.wav',
    '2': '2.wav',
    '3': '3.wav',
    '4': '4.wav',
    '5': '5.wav',
    '6': '6.wav',
    '7': '7.wav',
    '8': '8.wav',
    '9': '9.wav',
}

lifted_files = {
    '0': '0_lifted.wav',
    '1': '1_lifted.wav',
    '2': '2_lifted.wav',
    '3': '3_lifted.wav',
    '4': '4_lifted.wav',
    '5': '5_lifted.wav',
    '6': '6_lifted.wav',
    '7': '7_lifted.wav',
    '8': '8_lifted.wav',
    '9': '9_lifted.wav',
}

# Define other audio files
tune_file = 'tune.wav'
ding_file = 'ding.wav'
dong_file = 'dong.wav'

log_file = 'numbers_log.txt'

def play_audio(file, delay_after=0):
    """Play an audio file and wait until it finishes, with an optional delay after."""
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    time.sleep(delay_after)

def play_tune(repeat=1):
    """Play the Lincolnshire Poacher tune multiple times with a half-second delay between each."""
    for i in range(repeat):
        print(f"\rPlaying Interval Signal 'The Lincolnshire Poacher' {i + 1}/{repeat}", end='', flush=True)
        play_audio(tune_file, delay_after=0.5)
    print()  # Move to the next line after completion

def play_chimes():
    """Play the chimes (ding-dong) six times, with 0.5s between ding and dong, and 1s between rounds."""
    print()  # Ensure chimes start on a fresh line
    for i in range(6):
        print(f"\rPlaying Gongs {i + 1}/6", end='', flush=True)
        play_audio(ding_file, delay_after=0.5)
        play_audio(dong_file, delay_after=1)
    print()  # Move to the next line after completion

def generate_number_group():
    """Generate a group of 5 random numbers."""
    return [str(random.randint(0, 9)) for _ in range(4)] + [str(random.randint(0, 9))]

def play_number_group(group):
    """Play a group of 5 numbers, with the 5th being the lifted version."""
    for digit in group[:4]:
        play_audio(audio_files[digit], delay_after=0.5)
    play_audio(lifted_files[group[4]], delay_after=1)

def log_to_file(agent_id, message):
    """Log the agent_id and message to a file at the start."""
    with open(log_file, 'w') as log:
        log.write("Lincolnshire Poacher Numbers Log\n")
        log.write("===============================\n")
        log.write("Agent ID:\n")
        log.write(" ".join(agent_id) + "\n\n")
        log.write("Message:\n")
        for group in message:
            log.write(" ".join(group) + "\n")
        log.write("\nEnd of Message\n")

def main():
    # Print the introductory message with the warning and additional fun note
    print("\nWelcome to the E03 - The Lincolnshire Poacher Emulator\n")
    print("When I was bound apprentice in famous Lincolnshire,")
    print("I serv'd my master truly, for nearly seven odd year,")
    print("Till I took up to poaching, as you shall quickly hear.")
    print("Oh, 'tis my delight on a shining night, in the season of the year.\n")
    print("IMPORTANT WARNING: This emulator is for educational and entertainment purposes only.")
    print("Never broadcast this emulator using any medium including radio frequencies,")
    print("telegraphy, or similar, and do not use it as a means of encryption.\n")
    input("\nPlease acknowledge the warning by pressing Enter to continue...\n")
    print("--------------------------------------------------------------------------------\n")
    print("\nE03 was a numbers station and was so named after the 2 bar tune taken from an old folk song called")
    print("'The Lincolnshire Poacher' - which was played as an interval (or tuning) signal before the main broadcast.\n")
    print("Much and little is known about number stations, as no government has acknowledged their existence or")
    print("operation. What we think we know about E03 is that at one time it broadcasted from RAF Akrotiri in Cyprus")
    print("and stopped transmissions around July 2008. E03 also had a sister station in the southern hemisphere,")
    print("E03a, which used the folk song 'Cherry Ripe' as its interval signal and was last reported in December 2009.\n")
    print("This emulator was created as a bit of fun to cast light on the mysterious world of Number Stations.\n")   
    print("\nMore information about numbers stations can be found at priyom.org.")
    print("\nWe hope you enjoy this emulator!")
    
    # Acknowledge randomised message
    input("\nPlease Enter to generate a randomised computer generated message\n")

    # Generate the agent_id (5-digit group)
    agent_id = generate_number_group()

    # Generate the main message (200 five-figure groups)
    message = [generate_number_group() for _ in range(200)]

    # Log the agent_id and message to the log file
    log_to_file(agent_id, message)

    # Acknowledge warning message
    input("Message generated and saved, Press ENTER to 'broadcast'\n")
    
    # Play the initial Lincolnshire Poacher tune 12 times
    play_tune(12)

    # Play the agent_id group repeated 10 times
    for i in range(10):
        print(f"\rPlaying Message/Agent ID {i + 1}/10: {''.join(agent_id)}", end='', flush=True)
        play_number_group(agent_id)
    print()  # Move to the next line after completion

    # Play chimes (ding-dong) 6 times
    play_chimes()

    # Play the main message, each group once, then immediately repeat
    for i, group in enumerate(message):
        print(f"\r5 Digit message group {i + 1}/200: {''.join(group)}", end='', flush=True)
        play_number_group(group)
        play_number_group(group)
    print()  # Move to the next line after completion

    # Play chimes (ding-dong) 6 times again
    play_chimes()

    # Play the Lincolnshire Poacher tune 6 times to finish
    play_tune(6)

if __name__ == "__main__":
    main()

# Quit pygame mixer after finishing the script
pygame.mixer.quit()
