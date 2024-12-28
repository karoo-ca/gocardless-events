"""
"instalment_schedules": [
    {
        "action": "resumed",
        "description": "The instalment schedule has been rectified by remedying any failed payments.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "instalment_schedule_resumed",
                "description": "Instalment schedule has resumed"
            }
        ]
    },
    {
        "action": "creation_failed",
        "description": "The instalment schedule failed to create due to validation errors when creating the payments. The errors will be included in the event payload.",
        "details": [
            {
                "origin": "api",
                "cause": "instalment_schedule_creation_failed",
                "description": "Instalment schedule failed to be created"
            }
        ]
    },
    {
        "action": "errored",
        "description": "One or more instalments in this instalment schedule failed to collect successfully.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "instalment_schedule_errored",
                "description": "Instalment schedule has errored"
            },
            {
                "origin": "gocardless",
                "cause": "instalment_schedule_errored_late",
                "description": "One or more payments in the instalment schedule has had a late failure"
            }
        ]
    },
    {
        "action": "completed",
        "description": "This instalment schedule has concluded. No further instalments will be collected.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "instalment_schedule_completed",
                "description": "Instalment schedule has completed"
            }
        ]
    },
    {
        "action": "created",
        "description": "The instalment schedule has been created.",
        "details": [
            {
                "origin": "api",
                "cause": "instalment_schedule_created",
                "description": "Instalment schedule has been created via the API"
            }
        ]
    },
    {
        "action": "cancelled",
        "description": "The instalment schedule has been cancelled. Any pending payments have also been cancelled.",
        "details": [
            {
                "origin": "api",
                "cause": "instalment_schedule_cancelled",
                "description": "Instalment schedule has been cancelled"
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "description": "Instalment schedule has been cancelled"
            },
            {
                "origin": "gocardless",
                "cause": "mandate_failed",
                "description": "Instalment schedule has been cancelled"
            },
            {
                "origin": "gocardless",
                "cause": "mandate_suspended_by_payer",
                "description": "Instalment schedule has been cancelled"
            },
            {
                "origin": "gocardless",
                "cause": "mandate_expired",
                "description": "Instalment schedule has been cancelled"
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union, List
from pydantic import BaseModel, Field, RootModel


class InstalmentScheduleResumed(BaseModel):
    action: Literal["resumed"]
    description: str
    details: InstalmentScheduleResumedInstalmentScheduleResumedDetail


class InstalmentScheduleCreationFailed(BaseModel):
    action: Literal["creation_failed"]
    description: str
    details: InstalmentScheduleCreationFailedInstalmentScheduleCreationFailedDetail


class InstalmentScheduleErrored(BaseModel):
    action: Literal["errored"]
    description: str
    details: List[
        Annotated[
            Union[
                InstalmentScheduleErroredInstalmentScheduleErroredDetail,
                InstalmentScheduleErroredInstalmentScheduleErroredLateDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class InstalmentScheduleCompleted(BaseModel):
    action: Literal["completed"]
    description: str
    details: InstalmentScheduleCompletedInstalmentScheduleCompletedDetail


class InstalmentScheduleCreated(BaseModel):
    action: Literal["created"]
    description: str
    details: InstalmentScheduleCreatedInstalmentScheduleCreatedDetail


class InstalmentScheduleCancelled(BaseModel):
    action: Literal["cancelled"]
    description: str
    details: List[
        Annotated[
            Union[
                InstalmentScheduleCancelledInstalmentScheduleCancelledDetail,
                InstalmentScheduleCancelledMandateCancelledDetail,
                InstalmentScheduleCancelledMandateFailedDetail,
                InstalmentScheduleCancelledMandateSuspendedByPayerDetail,
                InstalmentScheduleCancelledMandateExpiredDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class InstalmentScheduleResumedInstalmentScheduleResumedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_resumed"]
    description: str


class InstalmentScheduleCreationFailedInstalmentScheduleCreationFailedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["instalment_schedule_creation_failed"]
    description: str


class InstalmentScheduleErroredInstalmentScheduleErroredDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_errored"]
    description: str


class InstalmentScheduleErroredInstalmentScheduleErroredLateDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_errored_late"]
    description: str


class InstalmentScheduleCompletedInstalmentScheduleCompletedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_completed"]
    description: str


class InstalmentScheduleCreatedInstalmentScheduleCreatedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["instalment_schedule_created"]
    description: str


class InstalmentScheduleCancelledInstalmentScheduleCancelledDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["instalment_schedule_cancelled"]
    description: str


class InstalmentScheduleCancelledMandateCancelledDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_cancelled"]
    description: str


class InstalmentScheduleCancelledMandateFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_failed"]
    description: str


class InstalmentScheduleCancelledMandateSuspendedByPayerDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_suspended_by_payer"]
    description: str


class InstalmentScheduleCancelledMandateExpiredDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    description: str


InstalmentScheduleType = Annotated[
    Union[
        InstalmentScheduleResumed,
        InstalmentScheduleCreationFailed,
        InstalmentScheduleErrored,
        InstalmentScheduleCompleted,
        InstalmentScheduleCreated,
        InstalmentScheduleCancelled,
    ],
    Field(..., discriminator="action"),
]

InstalmentSchedule = RootModel[InstalmentScheduleType]
