from config import settings
import ollama

class SummaryService:
    def __init__(self):
        self.model = settings.OLLAMA_MODEL

    async def generate_summary(self, text: str) -> str:
        payload = {"role": "user", "content": f"Summarize the following text in a clear, concise way:\n\n{text}"}

        response = ollama.chat(
            model = self.model,
            messages = [payload]
        )
        summary = response["message"]["content"]
        return {"summary": summary}