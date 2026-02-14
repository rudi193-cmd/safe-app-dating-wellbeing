RED_FLAG_KEYWORDS = {
    "love_bombing": ["soulmate","never felt this","you're perfect","move fast"],
    "control": ["don't waste my time","my ex was crazy","know what I want"],
    "age_gap_rationalize": ["mature for age","age is just a number"],
}

def scan_red_flags(profile):
    flags = []
    text = (profile.bio + profile.raw_text).lower()
    for category, phrases in RED_FLAG_KEYWORDS.items():
        if any(p in text for p in phrases):
            flags.append(category)
    return flags
