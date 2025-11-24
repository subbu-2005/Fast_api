import time
import sys
from pathlib import Path

try:
    import pygame
    pygame_available = True
except ImportError:
    pygame_available = False
    print("pygame not installed. Install it with: pip install pygame")


def type_text(text, delay=0.03):
    """Simulate typing animation for text"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line after typing complete


def play_synced_lyrics():
    """Play music with perfectly synced lyrics using pygame with typing animation"""

    music_file = r"C:\Users\subra\Desktop\WhatsApp Audio 2025-11-24 at 10.40.37_03005a06.mp3"

    # Adjusted timestamps - shifted 1.61 seconds later (28.8 - 27.19 = 1.61)
    synced_lyrics = [
        (28.80, "It's always around me, all this noise"),
        (33.31, "But not nearly as loud as the voice saying"),
        (39.06, "\"Let it happen, let it happen\" (It's gonna feel so good)"),
        (45.06, "\"Just let it happen, let it happen\""),
        (55.81, "All this running around"),
        (60.57, "Trying to cover my shadow"),
        (64.09, "A notion growing inside"),
        (67.85, "Now all the others seem shallow"),
        (72.35, "All this running around"),
        (76.62, "Bearing down on my shoulders"),
        (79.38, "I can hear an alarm"),
        (83.13, "It must be morning"),
        (87.39, ""),  # Instrumental break
        (109.90, "I heard about a whirlwind that's coming 'round"),
        (115.66, "It's gonna carry off all that isn't bound"),
        (121.15, "And when it happens, when it happens (I won't be holding on)"),
        (126.15, "So let it happen, let it happen"),
        (129.68, ""),  # Short break
        (132.93, "All this running around"),
        (136.93, "I can't fight it much longer"),
        (140.61, "Something's trying to get out"),
        (144.36, "And it's never been closer"),
        (148.11, "If my take-off fails"),
        (151.86, "Make up some other story"),
        (155.61, "If I never come back"),
        (159.36, "Tell my mother I'm sorry"),
        (163.11, ""),  # Bridge section
        (195.61, "I cannot vanish, you will not scare me"),
        (199.11, "Try to get through it, try to push through it"),
        (202.61, "You were not thinking that I will not do it"),
        (206.11, "They be lovin' someone and I'm another story"),
        (209.61, "Take the next ticket, get the next train"),
        (213.11, "Why would I do it? Anyone'd think that"),
        (216.61, ""),
        (220.61, "I cannot vanish, you will not scare me"),
        (224.11, "Try to get through it, try to push through it"),
        (227.61, "You were not thinking that I will not do it"),
        (231.11, "They be lovin' someone and I'm another story"),
        (234.61, "Take the next ticket, get the next train"),
        (238.11, "Why would I do it? Anyone'd think that"),
        (241.61, ""),
        (245.61, "Try to get through it, try to push through it"),
        (249.11, "You were not thinking that I will not do it"),
        (252.61, "They be lovin' someone and I'm another story"),
        (256.11, "Take the next ticket, get the next train"),
        (259.61, "Why would I do it? Anyone'd think that"),
        (263.11, ""),
        (340.61, "Baby, now I'm ready, moving on"),
        (344.61, "Oh, but maybe I was ready all along"),
        (348.61, "Oh, I'm ready for the moment and the sound"),
        (352.61, "Oh, but maybe I was ready all along"),
        (356.61, ""),
        (360.61, "Baby, now I'm ready, moving on"),
        (364.61, "Oh, but maybe I was ready all along"),
        (368.61, "Oh, I'm ready for the moment and the sound"),
        (372.61, "Oh, but maybe I was ready all along"),
    ]

    if not Path(music_file).exists():
        print(f"❌ Music file not found: {music_file}")
        return

    if not pygame_available:
        return

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)

    print("\n" + "=" * 70)
    print(" " * 20 + "🎵 LET IT HAPPEN - TAME IMPALA 🎵")
    print("=" * 70)
    print("\n")

    # Start playing music
    pygame.mixer.music.play()
    start_time = time.time()

    # Display lyrics synced with music
    lyric_index = 0

    while pygame.mixer.music.get_busy() and lyric_index < len(synced_lyrics):
        # Calculate current playback position
        current_time = time.time() - start_time

        # Check if it's time to display the next lyric
        if lyric_index < len(synced_lyrics):
            timestamp, lyric = synced_lyrics[lyric_index]

            if current_time >= timestamp:
                if lyric:  # Only print non-empty lines
                    sys.stdout.write("♪  ")
                    sys.stdout.flush()
                    type_text(lyric, delay=0.03)  # Typing animation
                else:
                    print()  # Empty line for spacing
                lyric_index += 1

        time.sleep(0.05)  # Check every 0.05 seconds for precise timing

    print("\n")
    print("=" * 70)
    print("✨ Song finished! Press Ctrl+C to exit...")
    print("=" * 70)

    # Keep program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\n👋 Stopped!")


if __name__ == "__main__":
    if not pygame_available:
        print("\n⚠️  You need to install pygame first!")
        print("Run this command in your terminal:")
        print("   pip install pygame")
        print("\nThen run this script again.")
    else:
        play_synced_lyrics()