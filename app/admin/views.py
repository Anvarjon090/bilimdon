from starlette_admin.contrib.sqla import ModelView


class UserView(ModelView):
    fields = ["id", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser"]


class GameView(ModelView):
    fields = ["id", "title", "description", "start_time", "end_time", "topic_id", "score"]


class QuestionView(ModelView):
    fields = ["id", "title", "description", "topic_id"]


class ParticipationView(ModelView):
    fields = ["id", "user_id", "game", "start_time", "end_time", "gained_score"]


class SubmissionView(ModelView):
    fields = ["id", "user", "game", "question", "option", "is_correct"]


class OptionView(ModelView):
    fields = ["id", "question", "title", "is_correct"]


class TopicView(ModelView):
    fields = ["id", "name"]



    