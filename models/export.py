"""
"exports": [
    {
        "action": "failed",
        "description": "Export failed",
        "details": [
            {
                "origin": "gocardless",
                "cause": "export_failed",
                "description": "Export failed"
            }
        ]
    },
    {
        "action": "completed",
        "description": "Export completed",
        "details": [
            {
                "origin": "gocardless",
                "cause": "export_completed",
                "description": "Export completed"
            }
        ]
    },
    {
        "action": "started",
        "description": "Export started",
        "details": [
            {
                "origin": "gocardless",
                "cause": "export_started",
                "description": "Export started"
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class ExportFailed(BaseModel):
    action: Literal["failed"]
    description: str
    details: ExportFailedExportFailedDetail


class ExportCompleted(BaseModel):
    action: Literal["completed"]
    description: str
    details: ExportCompletedExportCompletedDetail


class ExportStarted(BaseModel):
    action: Literal["started"]
    description: str
    details: ExportStartedExportStartedDetail


class ExportFailedExportFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["export_failed"]
    description: str


class ExportCompletedExportCompletedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["export_completed"]
    description: str


class ExportStartedExportStartedDetail(BaseModel):
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
