import json
import random

from myproject.settings import BASE_DIR


CATEGORY_DIR = BASE_DIR / "quiz" / "categories"


class Leaderboard:
    def __init__(self,):
        self.players = []    
        self._load()

    def player_exists(self, name):
        return any(
            player["name"].lower() == name.lower()
            for player in self.players
        )

    def add_player(self, name, score):
        if self.player_exists(name):
            return False

        self.players.append({
            "name": name.strip(),
            "score": score
        })

        return True

    def get_score(self, player):
        return player["score"]


    def get_sorted(self):
        return sorted(
            self.players,
            key=self.get_score,
            reverse=True
        )

class QuizGame:
    DIFFICULTY_FILES = {
        "easy": "easy.json",
        "medium": "medium.json",
        "hard": "hard.json",
    }

    def __init__(self):
        self.category_dir = CATEGORY_DIR

    def get_difficulties(self):
        return list(self.DIFFICULTY_FILES.keys())

    def get_quiz_data(self, difficulty):
        filename = self.DIFFICULTY_FILES.get(difficulty)

        if not filename:
            return []

        return self.load_quiz_file(filename)

    def load_quiz_file(self, filename):
        path = self.category_dir / filename

        try:
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_random_quiz(self, difficulty):
        questions = self.get_quiz_data(difficulty)

        if not questions:
            return None

        return random.choice(questions)

    def score_quiz(self, quiz_data, answers):
        score = 0

        for question, answer in zip(quiz_data, answers):
            if (
                isinstance(answer, str)
                and answer.strip().upper() == question["answer"]
            ):
                score += 1

        return score