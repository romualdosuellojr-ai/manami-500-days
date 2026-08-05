import datetime
import time
import sys

# 1. Anniversary Details
partner_name = "Manami"
start_date = datetime.date(2025, 3, 23)

# 2. Day Calculation
today = datetime.date.today()
days_together = (today - start_date).days

# 3. Typewriter Animation Function
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 4. Animated Text Presentation
print("\n" + "🌸" * 25 + "\n")
typewriter(f"✨ Loading special milestone for {partner_name}... ✨\n", 0.08)
time.sleep(1)

print("🌸" * 25 + "\n")
typewriter(f"   ❤️  HAPPY {days_together} DAYS OF LOVE!  ❤️   ", 0.06)
print("\n" + "🌸" * 25 + "\n")

typewriter(f"Today marks exactly {days_together} beautiful days since March 23, 2025.")
typewriter("Thank you for filling my life with so much joy and sweetness.\n")
time.sleep(1)

print("✨ My message to you:")
typewriter(f"To Manami, happy {days_together} days anniversary of being together!")
typewriter("Thank you for always making me happy. I will love you forever. ❤️\n")
time.sleep(1)

# 5. Massive Cherry Blossom Heart (Bypasses all photo errors!)
print("      🌸🌸🌸       🌸🌸🌸      ")
print("    🌸🌸   🌸🌸   🌸🌸   🌸🌸    ")
print("  🌸🌸       🌸🌸🌸       🌸🌸  ")
print("  🌸🌸         🌸         🌸🌸  ")
print("    🌸🌸                 🌸🌸    ")
print("      🌸🌸             🌸🌸      ")
print("        🌸🌸         🌸🌸        ")
print("          🌸🌸     🌸🌸          ")
print("            🌸🌸 🌸🌸            ")
print("              🌸🌸              ")
print("\n" + "🌸" * 25 + "\n")
