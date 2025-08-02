import re
from typing import List

POSITIVE_WORDS: List[str] = [
    "good", "great", "excellent", "fantastic", "yes", "evet", "love",
    "olumlu", "harika", "mükemmel", "heyecanlı", "pozitif"
]
NEGATIVE_WORDS: List[str] = [
    "bad", "terrible", "awful", "no", "hayır", "hayir", "hate", "kötü",
    "negatif", "berbat", "dreadful"
]


def _sentiment_score(text: str) -> int:
    words = re.findall(r"\w+", text.lower())
    score = 0
    for w in words:
        if w in POSITIVE_WORDS:
            score += 1
        if w in NEGATIVE_WORDS:
            score -= 1
    return score


def make_decision(question: str) -> str:
    """Return a clear decision derived from a tiny word-based sentiment model."""
    options = re.split(r"\bor\b|\bveya\b|\bya da\b", question, flags=re.IGNORECASE)
    cleaned = [opt.strip() for opt in options if opt.strip()]
    if len(cleaned) >= 2:
        scores = [_sentiment_score(opt) for opt in cleaned]
        best_option = cleaned[scores.index(max(scores))]
        best_option = re.sub(r"^(should|shall)\s+i\s+", "", best_option, flags=re.IGNORECASE)
        best_option = best_option.strip(" ?!.")
        return f"Bunu seç: {best_option}"
    score = _sentiment_score(question)
    return "EVET, bunu yap." if score >= 0 else "HAYIR, bunu yapma."


def main() -> None:
    import sys
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        print(make_decision(q))
    else:
        q = input("Sorunuzu yazın: ")
        print(make_decision(q))


if __name__ == "__main__":
    main()
