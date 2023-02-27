from typing import Any, List, Optional

from classification_model.processing.validation import TitanicDataInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]
    predict_proba: Optional[List[float]]


# class TitanicDataInputSchema(BaseModel):
#     PassengerId: Optional[int]
#     Pclass: Optional[str]
#     Name: Optional[str]
#     Sex: Optional[str]
#     Age: Optional[float]
#     SibSp: Optional[str]
#     Parch: Optional[str]
#     Ticket: Optional[str]
#     Fare: Optional[float]
#     Cabin: Optional[str]
#     Embarked: Optional[str]


class MultiplePassengerDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "PassengerId": 894,
                        "Pclass": 2,
                        "Name": "Mr. Thomas Francis",
                        "Sex": "male",
                        "Age": 35,
                        "SibSp": "1",
                        "Parch": "0",
                        "Ticket": "SC/AH 3085",
                        "Fare": 9.225,
                        "Cabin": "B45",
                        "Embarked": "S",
                    }
                ]
            }
        }
