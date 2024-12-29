from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class SchemeIdentifierActivated(BaseModel):
    """
    This scheme identifier has been activated.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["scheme_identifiers"]
    action: Literal["activated"]
    details: SchemeIdentifierActivatedSchemeIdentifierActivatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class SchemeIdentifierActivatedSchemeIdentifierActivatedDetail(BaseModel):
    """
    This scheme identifier has been activated.
    """

    origin: Literal["gocardless"]
    cause: Literal["scheme_identifier_activated"]
    description: str


SchemeIdentifierType = Annotated[
    SchemeIdentifierActivated, Field(..., discriminator="action")
]

SchemeIdentifier = RootModel[SchemeIdentifierType]
