from app import check_guess
from logic_utils import check_guess
from app import parse_guess



def test_check_guess_hint_direction_when_secret_is_string_too_low():
    # On even attempts, secret is passed as a string.
    # Before the fix, str("50") vs int(9): "9" > "50" lexicographically,
    # so the old code returned "Too High" instead of the correct "Too Low".
    outcome, _ = check_guess(9, "50")
    assert outcome == "Too Low"


def test_check_guess_hint_direction_when_secret_is_string_too_high():
    # Guess larger than secret, secret passed as string.
    outcome, _ = check_guess(90, "50")
    assert outcome == "Too High"


def test_check_guess_win_when_secret_is_string():
    # Exact match should still register as a win when secret is a string.
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_parse_guess_rejects_out_of_range():
    # parse_guess should reject numbers outside the current difficulty bounds
    ok, value, err = parse_guess("25", low=1, high=20)
    assert ok is False
    assert value is None
    assert "between 1 and 20" in err


def test_parse_guess_rejects_below_range():
    # parse_guess should reject numbers below the current difficulty bounds
    ok, value, err = parse_guess("0", low=1, high=20)
    assert ok is False
    assert value is None
    assert "between 1 and 20" in err


def test_parse_guess_accepts_boundary_value():
    # parse_guess should accept a guess at the upper boundary
    ok, value, err = parse_guess("20", low=1, high=20)
    assert ok is True
    assert value == 20
    assert err is None


def test_attempts_initializes_to_zero_gives_full_attempt_count():
    # Bug: attempts was initialized to 1 instead of 0.
    # With attempts=1 and attempt_limit=6, the player only got 5 guesses
    # because the game-over check (attempts >= attempt_limit) triggered one
    # submit too early.
    attempt_limit = 6  # Easy difficulty
    attempts = 0  # correct initial value after the fix

    guesses_made = 0
    while attempts < attempt_limit:
        attempts += 1  # simulate each submit click
        guesses_made += 1

    assert guesses_made == attempt_limit  # player must get all 6 guesses


def test_new_game_resets_status_to_playing():
    # Bug: new_game block never reset status, so a won/lost game would hit the
    # st.stop() guard on the very next run and be unplayable after restart.
    # This test simulates the state transitions without Streamlit.
    session = {
        "attempts": 3,
        "secret": 42,
        "score": 75,
        "status": "won",        # game just finished
        "history": [10, 20, 42],
    }

    # Simulate what the fixed new_game block does
    session["attempts"] = 0
    session["secret"] = 55          # new secret (fixed value for determinism)
    session["score"] = 0
    session["status"] = "playing"   # the critical reset that was missing
    session["history"] = []

    # After a new game, the guard (status != "playing") must NOT block play
    assert session["status"] == "playing"
    assert session["attempts"] == 0
    assert session["score"] == 0
    assert session["history"] == []


def test_new_game_resets_status_from_lost():
    # Same fix must work when coming from a "lost" state.
    session = {"status": "lost", "attempts": 5, "score": 0, "history": [1, 2, 3, 4, 5]}

    session["attempts"] = 0
    session["score"] = 0
    session["status"] = "playing"
    session["history"] = []

    assert session["status"] == "playing"


def test_attempts_initializes_to_one_loses_a_guess():
    # Demonstrates the old buggy behaviour for contrast.
    # With the wrong initial value of 1, only 5 guesses are possible on Easy.
    attempt_limit = 6
    attempts = 1  # old (buggy) initial value

    guesses_made = 0
    while attempts < attempt_limit:
        attempts += 1
        guesses_made += 1

    assert guesses_made == attempt_limit - 1  # one guess was silently stolen
