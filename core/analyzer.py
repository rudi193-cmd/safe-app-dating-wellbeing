from .models import Profile, IntakeAnswers, AnalysisResult
from .redflags import scan_red_flags
from .scoring import calculate_score

def analyze_profile(profile: Profile, intake: IntakeAnswers, history=None):
    red_flags = scan_red_flags(profile)
    score = calculate_score(profile, user_prefs={})
    result = AnalysisResult(
        score=score,
        category="surface",
        depth_vs_fantasy="mixed",
        red_flags=red_flags,
        yellow_flags=[],
        intervention_level="none",
        recommendation="Reflect before proceeding.",
        reflection_questions=["What draws you to this person?", "What pattern might this continue?"],
        confidence=0.7
    )
    return result
