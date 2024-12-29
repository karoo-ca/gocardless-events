from __future__ import annotations

from typing import Annotated, Any, Literal, Union

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class ExportFailed(BaseModel):
    """
    Export failed
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["exports"]
    action: Literal["failed"]
    description: str
    details: ExportFailedExportFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class ExportCompleted(BaseModel):
    """
    Export completed
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["exports"]
    action: Literal["completed"]
    description: str
    details: ExportCompletedExportCompletedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class ExportStarted(BaseModel):
    """
    Export started
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["exports"]
    action: Literal["started"]
    description: str
    details: ExportStartedExportStartedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class ExportFailedExportFailedDetail(BaseModel):
    """
    Export failed
    """

    origin: Literal["gocardless"]
    cause: Literal["export_failed"]
    description: str


class ExportCompletedExportCompletedDetail(BaseModel):
    """
    Export completed
    """

    origin: Literal["gocardless"]
    cause: Literal["export_completed"]
    description: str


class ExportStartedExportStartedDetail(BaseModel):
    """
    Export started
    """

    origin: Literal["gocardless"]
    cause: Literal["export_started"]
    description: str


ExportType = Annotated[
    Union[
        ExportFailed,
        ExportCompleted,
        ExportStarted,
    ],
    Field(..., discriminator="action"),
]

Export = RootModel[ExportType]
