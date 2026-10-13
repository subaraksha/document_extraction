from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class Party(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: str = Field(
        min_length=1, description="Full legal name of a contracting party."
    )
    evidence: str = Field(
        min_length=1, description="Supporting quote from the contract."
    )


class AgreementDate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: date = Field(description="Agreement date, not the effective date.")
    evidence: str = Field(
        min_length=1, description="Supporting quote from the contract."
    )


class GoverningLaw(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: str = Field(
        min_length=1, description="Jurisdiction whose laws govern the agreement."
    )
    evidence: str = Field(
        min_length=1, description="Supporting quote from the contract."
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
