from google import genai
from google.genai import types

from app.core.config import Settings
from app.extraction.prompts import EXTRACTION_PROMPT
from app.extraction.schemas import ContractExtraction


def extract_contract(
    text: str, settings: Settings
) -> tuple[ContractExtraction, dict[str, int | None]]:
    if not text.strip():
        raise ValueError("Contract text is empty.")

    with genai.Client(api_key=settings.gemini_api_key) as client:
        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=text,
            config=types.GenerateContentConfig(
                system_instruction=EXTRACTION_PROMPT,
                response_mime_type="application/json",
                response_json_schema=ContractExtraction.model_json_schema(),
            ),
        )

    if not response.text:
        raise ValueError("Gemini returned no extraction text.")
    extraction = ContractExtraction.model_validate_json(response.text)
    metadata = response.usage_metadata
    usage = {
        "input_tokens": metadata.prompt_token_count if metadata else None,
        "output_tokens": metadata.candidates_token_count if metadata else None,
        "thinking_tokens": metadata.thoughts_token_count if metadata else None,
        "total_tokens": metadata.total_token_count if metadata else None,
    }
    return extraction, usage
