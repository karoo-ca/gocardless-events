from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class SchemeIdentifierActivated(BaseModel):
    """
    This scheme identifier has been activated.
    """

    action: Literal["activated"]
    description: str
    details: SchemeIdentifierActivatedSchemeIdentifierActivatedDetail


class SchemeIdentifierActivatedSchemeIdentifierActivatedDetail(BaseModel):
    """
    This scheme identifier has been activated.
    """

    origin: Literal["gocardless"]
    cause: Literal["scheme_identifier_activated"]
    description: str


SchemeIdentifierType = Annotated[
    Union[SchemeIdentifierActivated,], Field(..., discriminator="action")
]

SchemeIdentifier = RootModel[SchemeIdentifierType]
