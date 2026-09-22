import random


def get_daily_lesson():
    vault = [
        ("S-CLASS", "The Great Attractor",
         "There is a gravitational anomaly in intergalactic space that is pulling our galaxy and others toward it. Its nature remains unknown."),
        ("B-CLASS", "The Voynich Manuscript",
         "A 15th-century book written in an unknown script that has defied all attempts at decryption for centuries."),
        ("A-CLASS", "Quantum Entanglement",
         "Particles can remain connected such that the state of one instantly influences the other, regardless of the distance separating them."),
        ("C-CLASS", "The Library of Ashurbanipal",
         "One of the first systemic archives of human knowledge, containing thousands of clay tablets from ancient Mesopotamia.")
    ]
    classification, title, fact = random.choice(vault)
    return (
        f"--- INTEL BRIEF: {classification} ---\n"
        f"SUBJECT: {title}\n"
        f"DATA: {fact}\n"
        f"----------------------------"
    )
