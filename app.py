import pygame
import time
import datetime

# 🔄 Pygame sound initialize
pygame.mixer.init()

# 🔥 User se alarm time lo
alarm_time = input("⏰ Set alarm time (HH:MM:SS AM/PM): ").strip()

# 🛠 MP3 ka path
sound_file = "F:/python-challenge-task/Tic-Tac-Mechanical-Alarm-Clock.mp3"

# ✅ MP3 File Load Check
try:
    sound = pygame.mixer.Sound(sound_file)
except pygame.error:
    print("❌ MP3 file not found ya format issue!")
    exit()

print(f"⏳ Waiting for alarm at {alarm_time}...")

# ✅ Convert Input String to 24-Hour Format
try:
    alarm_dt = datetime.datetime.strptime(alarm_time, "%I:%M:%S %p")  # 🛠 Convert 12-hour format to 24-hour
    alarm_time_24 = alarm_dt.strftime("%H:%M:%S")  # ✅ 24-hour format main convert
except ValueError:
    print("❌ Invalid time format! Please use HH:MM:SS AM/PM")
    exit()

while True:
    # 🔄 Get Current Time in 24-Hour Format
    now = datetime.datetime.now().strftime("%H:%M:%S")

    # 🛠 Debugging (current time check)
    print(f"🔄 Checking time: {now}", end="\r", flush=True)

    # ✅ Check if time matches
    if now == alarm_time_24:
        print("\n🔊 Alarm ringing!")
        sound.play()
        
        # ⏳ User ko alarm band karne ka option
        input("🔇 Alarm band karne ke liye ENTER press karein...")  

        # 🔴 Alarm Stop
        sound.stop()
        print("✅ Alarm band ho gaya!")
        
        # 🌞 Motivational Message
        print("🌞 Ek nai subha ap ki muntazir hai! 🚀")
        break  # ✅ Exit after alarm

    time.sleep(1)  # ⏳ Loop delay

