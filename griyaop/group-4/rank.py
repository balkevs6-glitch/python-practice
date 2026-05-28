import json
import os
import random
  
class Leaderboard:
    def __init__(self, filename="rank.json"):
        self.filename = filename
        self.player = []
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.player = json.load(file)
            except (json.JSONDecodeError, IOError):
                self.player = []
        else:
            self.player = []

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.player, file, indent=2)

    def player_exists(self, name):
        return any(player["name"].lower() == name.lower() for player in self.player)

    def add_player(self, name, score):
        if self.player_exists(name):
            return False

        self.player.append({"name": name, "score": score})
        self._save()
        return True

    def get_sorted(self):
        return sorted(self.player, key=lambda x: x["score"], reverse=True)


class QuizGame:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard

    def score_quiz(self, quiz_data, answers):
        score = 0
        for question, answer in zip(quiz_data, answers):
            if isinstance(answer, str) and answer.strip().upper() == question["answer"]:
                score += 1
        return score
   
    def add_player_score(self, name, score):
        return self.leaderboard.add_player(name, score)
    