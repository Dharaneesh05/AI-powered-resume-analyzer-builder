from config.database import save_feedback, get_feedback_stats

class FeedbackManager:
    def save_feedback(self, feedback_data):
        """Save feedback using the database function."""
        save_feedback(feedback_data)

    def get_feedback_stats(self):
        """Retrieve feedback statistics using the database function."""
        return get_feedback_stats()