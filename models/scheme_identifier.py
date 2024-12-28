"""
"scheme_identifiers": [
    {
        "action": "activated",
        "description": "This scheme identifier has been activated.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "scheme_identifier_activated",
                "description": "This scheme identifier has been activated."
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class SchemeIdentifierActivated(BaseModel):
    action: Literal["activated"]
    description: str
    details: SchemeIdentifierActivatedSchemeIdentifierActivatedDetail


class SchemeIdentifierActivatedSchemeIdentifierActivatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["scheme_identifier_activated"]
    description: str


SchemeIdentifierType = Annotated[
    Union[SchemeIdentifierActivated,], Field(..., discriminator="action")
]

SchemeIdentifier = RootModel[SchemeIdentifierType]
