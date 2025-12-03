import pytest
from app.services.summary_service import SummaryService

@pytest.mark.asyncio
async def test_ai_service_mocked(monkeypatch):
    # Prepared a fake ollama.chat response structure
    fake_response = {"message": {"content": "mocked summary"}}

    # Monkeypatch the ollama.chat function used inside the service
    import ollama as _ollama

    def fake_chat(model, messages):
        return fake_response

    monkeypatch.setattr(_ollama, "chat", fake_chat)

    service = SummaryService()
    result = await service.generate_summary("Hello World")

    # Current implementation returns a dict with 'summary' key
    assert isinstance(result, dict)
    assert result.get("summary") == "mocked summary"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])