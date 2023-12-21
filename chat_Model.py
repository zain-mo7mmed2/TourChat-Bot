Orgenal = ["10", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Emojies = ["🔟", "0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

def reply(message):
    reply = """
        Best time to visit:
        Spring (April to June) or Fall (September to October) is the best time to visit.

        Day 1: Arrival in Istanbul
        - Arrive in Istanbul and check into your accommodation.
        - Spend the evening exploring the Sultanahmet Square area, where you can see the Blue Mosque and Hagia Sophia from the outside.

        What to eat\n
        Try a classic Turkish kebab or Iskender kebab at a local restaurant.

        Day 2: Istanbul\n
        - Explore Hagia Sophia and the Blue Mosque (make sure to check the visiting hours).
        - Visit the Topkapi Palace and its beautiful gardens.
        - Stroll through the Grand Bazaar for shopping.
        """

    for i in range(len(Orgenal)):
        reply = reply.replace(Orgenal[i], Emojies[i])

    return reply