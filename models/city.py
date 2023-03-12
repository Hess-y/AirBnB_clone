#!/usr/bin/python3
""" City module """


from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    state_id = ""
    name = ""

    def __init__(self, *prmargs, **prmkwargs):
        """
            Constructor
        """
        super().__init__(*prmargs, **prmkwargs)
