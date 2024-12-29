from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class ExportFailed(BaseModel):
    """
    Export failed
    """

    action: Literal["failed"]
    description: str
    details: ExportFailedExportFailedDetail


class ExportCompleted(BaseModel):
    """
    Export completed
    """

    action: Literal["completed"]
    description: str
    details: ExportCompletedExportCompletedDetail


class ExportStarted(BaseModel):
    """
    Export started
    """

    action: Literal["started"]
    description: str
    details: ExportStartedExportStartedDetail


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
