from __future__ import annotations
from typing import Annotated, Literal, Union, List
from pydantic import BaseModel, Field, RootModel


class InstalmentScheduleResumed(BaseModel):
    """
    The instalment schedule has been rectified by remedying any failed payments.
    """

    action: Literal["resumed"]
    description: str
    details: InstalmentScheduleResumedInstalmentScheduleResumedDetail


class InstalmentScheduleCreationFailed(BaseModel):
    """
    The instalment schedule failed to create due to validation errors when creating the payments. The errors will be included in the event payload.
    """

    action: Literal["creation_failed"]
    description: str
    details: InstalmentScheduleCreationFailedInstalmentScheduleCreationFailedDetail


class InstalmentScheduleErrored(BaseModel):
    """
    One or more instalments in this instalment schedule failed to collect successfully.
    """

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
    """
    This instalment schedule has concluded. No further instalments will be collected.
    """

    action: Literal["completed"]
    description: str
    details: InstalmentScheduleCompletedInstalmentScheduleCompletedDetail


class InstalmentScheduleCreated(BaseModel):
    """
    The instalment schedule has been created.
    """

    action: Literal["created"]
    description: str
    details: InstalmentScheduleCreatedInstalmentScheduleCreatedDetail


class InstalmentScheduleCancelled(BaseModel):
    """
    The instalment schedule has been cancelled. Any pending payments have also been cancelled.
    """

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
    """
    Instalment schedule has resumed
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_resumed"]
    description: str


class InstalmentScheduleCreationFailedInstalmentScheduleCreationFailedDetail(BaseModel):
    """
    Instalment schedule failed to be created
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_creation_failed"]
    description: str


class InstalmentScheduleErroredInstalmentScheduleErroredDetail(BaseModel):
    """
    Instalment schedule has errored
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_errored"]
    description: str


class InstalmentScheduleErroredInstalmentScheduleErroredLateDetail(BaseModel):
    """
    One or more payments in the instalment schedule has had a late failure
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_errored_late"]
    description: str


class InstalmentScheduleCompletedInstalmentScheduleCompletedDetail(BaseModel):
    """
    Instalment schedule has completed
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_completed"]
    description: str


class InstalmentScheduleCreatedInstalmentScheduleCreatedDetail(BaseModel):
    """
    Instalment schedule has been created via the API
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_created"]
    description: str


class InstalmentScheduleCancelledInstalmentScheduleCancelledDetail(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_cancelled"]
    description: str


class InstalmentScheduleCancelledMandateCancelledDetail(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_cancelled"]
    description: str


class InstalmentScheduleCancelledMandateFailedDetail(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_failed"]
    description: str


class InstalmentScheduleCancelledMandateSuspendedByPayerDetail(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_suspended_by_payer"]
    description: str


class InstalmentScheduleCancelledMandateExpiredDetail(BaseModel):
    """
    Instalment schedule has been cancelled
    """

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
