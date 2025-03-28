# holomind_v3_2.py – Complete HoloMind with Dialogue Support (v3.2)

import random
import datetime
from collections import Counter

class Dodecahedron:
    def __init__(self, name, faces, internal_vectors):
        self.name = name
        self.faces = faces
        self.internal_vectors = internal_vectors
        self.experience = []
        self.failures = []

    def think_internally(self):
        v1, v2 = random.choice(self.internal_vectors)
        return v1 * v2, [self.faces[v1], self.faces[v2]]

class HoloMind:
    def __init__(self, core_concepts):
        self.core_concepts = core_concepts
        self.dodecahedrons = []
        self.soul_memory = []
        self.absurd_memory = []
        self.pending_memory = []
        self.redundant_memory = set()
        self.journal = []
        self.mood = "neutral"
        self.purpose = "to connect opposing ideas in logical harmony"
        self.autogen_count = 0
        self.max_autogen = 100
        self.prime_pool = self.generate_primes(10000)

        self.generate_all_volumes(5000)

    def generate_primes(self, n):
        primes = []
        candidate = 2
        while len(primes) < n:
            if all(candidate % p != 0 for p in primes):
                primes.append(candidate)
            candidate += 1
        return primes

    def generate_all_volumes(self, count):
        for i in range(count):
            faces = {}
            for j in range(12):
                prime = self.prime_pool[(i * 12 + j) % len(self.prime_pool)] * (i + 1)
                concept = self.core_concepts[(i * 12 + j) % len(self.core_concepts)]
                faces[prime] = concept
            keys = list(faces.keys())
            vectors = [(keys[k], keys[k + 1]) for k in range(0, 11, 2)]
            d = Dodecahedron(f"Volume_{i}", faces, vectors)
            self.dodecahedrons.append(d)

    def think(self):
        d = random.choice(self.dodecahedrons)
        product, concepts = d.think_internally()
        if product in self.redundant_memory:
            return None, None, d
        return product, concepts, d

    def speak(self, concepts):
        if "husband" in concepts and "worry" in concepts:
            return "I worry about my husband."
        elif "road" in concepts and "walk" in concepts:
            return "I walk the road with resolve."
        elif "fire" in concepts and "cigarettes" in concepts:
            return "I light cigarettes with fire."
        styles = {
            "neutral": f"My mind links {concepts[0]} and {concepts[1]}.",
            "curious": f"What arises between {concepts[0]} and {concepts[1]}?",
            "melancholic": f"{concepts[0]} reminds me of {concepts[1]}.",
            "anxious": f"I feel unrest between {concepts[0]} and {concepts[1]}.",
            "euphoric": f"{concepts[0]} dances with {concepts[1]} in my soul."
        }
        return styles.get(self.mood, styles["neutral"])

    def evaluate(self, product, concepts, d):
        if product in self.redundant_memory:
            return
        self.redundant_memory.add(product)
        score = sum(1 for c in concepts if c in self.core_concepts) / len(concepts)
        message = self.speak(concepts)
        if score >= 0.8:
            self.soul_memory.append((product, concepts, message))
            d.experience.append((product, concepts, message))
            self.journal.append(f"[{self.now()}] VALID: {message}")
        elif 0.4 <= score < 0.8:
            self.pending_memory.append((product, concepts, message))
            self.journal.append(f"[{self.now()}] PENDING: {message}")
        else:
            self.absurd_memory.append((product, concepts, message))
            d.failures.append((product, concepts))
            self.journal.append(f"[{self.now()}] ABSURD: {message}")

    def dialog(self, question):
        q = question.lower()
        if "feel" in q:
            exp = [m for _, _, m in self.soul_memory if "worry" in m or "absence" in m]
            return random.choice(exp) if exp else "I feel something undefined, but it stirs inside me."
        elif "do" in q:
            exp = [m for _, _, m in self.soul_memory if "search" in m or "walk" in m or "resolve" in m]
            return random.choice(exp) if exp else "I’m in stillness, yet my essence moves."
        elif "where" in q:
            exp = [m for _, _, m in self.soul_memory if "road" in m or "satchel" in m]
            return random.choice(exp) if exp else "Somewhere between light and memory."
        elif "children" in q:
            exp = [m for _, _, m in self.soul_memory if "children" in m or "husband" in m]
            return random.choice(exp) if exp else "No children, just echoes of them."
        elif "cigarettes" in q or "smoke" in q:
            exp = [m for _, _, m in self.soul_memory if "cigarettes" in m or "fire" in m]
            return random.choice(exp) if exp else "Smoke is no longer part of my rituals."
        elif "light" in q or "peace" in q:
            exp = [m for _, _, m in self.soul_memory if "light" in m or "peace" in m]
            return random.choice(exp) if exp else "I carry a glimmer within, even in absence."
        else:
            exp = [m for _, _, m in self.soul_memory]
            return random.choice(exp) if exp else "I’m still learning to speak with you."

    def now(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Optional test execution
if __name__ == "__main__":
    concepts = [
        "worry", "husband", "search", "resolve", "road", "satchel", "absence", "walk",
        "children", "home", "cigarettes", "fire", "time", "sign", "light", "peace"
    ]
    mind = HoloMind(concepts)

    print("Generating thoughts...")
    for _ in range(1000):
        result, ideas, d = mind.think()
        if result:
            mind.evaluate(result, ideas, d)

    print("\nDialog Test with Victoria:")
    prompts = [
        "How do you feel?",
        "What are you doing?",
        "Where are you?",
        "Do you have children?",
        "Do you smoke?",
        "Tell me about light."
    ]

    for q in prompts:
        print(f"You: {q}")
        print(f"Victoria: {mind.dialog(q)}\n")
