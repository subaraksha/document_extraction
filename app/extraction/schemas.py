from datetime import date
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

Quote = Annotated[str, Field(min_length=1)]
Evidence = Quote | Annotated[list[Quote], Field(min_length=1)]


class Party(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: str = Field(
        min_length=1,
        description="Full legal name of a contracting party, including any stated d/b/a name.",
    )
    evidence: Evidence = Field(
        description="One verbatim quote, or separate verbatim quotes from the contract."
    )


class AgreementDate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: date = Field(
        description="Agreement date: explicit date first, then an explicitly linked date definition; signature dates are a last resort only."
    )
    basis: Literal["explicit", "defined_date", "signature_fallback"] = Field(
        description="How the date was selected under the date precedence rules."
    )
    evidence: Evidence = Field(
        description="Verbatim supporting quote(s). For defined dates include the linking clause and definition; for signature fallback include the execution clause and signature dates."
    )


class GoverningLaw(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: str = Field(
        min_length=1, description="Jurisdiction whose laws govern the agreement."
    )
    evidence: Evidence = Field(
        description="One verbatim quote, or separate verbatim quotes from the contract."
    )


class ContractExtraction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parties: list[Party] = Field(description="Contracting parties; empty if not found.")
    agreement_date: AgreementDate | None = Field(
        description="Agreement date and supporting quote; null if not found."
    )
    governing_law: GoverningLaw | None = Field(
        description="Governing law and supporting quote; null if not found."
    )

    def check_evidence(self, source: str) -> dict[str, list[dict]]:
        """Check quote presence, not whether a quote proves the extracted value."""
        normalized_source = " ".join(source.split())
        checks = {}
        for field in type(self).model_fields:
            value = getattr(self, field)
            items = value if isinstance(value, list) else [value] if value else []
            checks[field] = []
            for item in items:
                quotes = (
                    [item.evidence] if isinstance(item.evidence, str) else item.evidence
                )
                for quote in quotes:
                    checks[field].append(
                        {
                            "quote": quote,
                            "found_in_source": bool(quote.strip())
                            and " ".join(quote.split()) in normalized_source,
                        }
                    )
        return checks
