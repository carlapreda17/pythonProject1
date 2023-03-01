import time
from datetime import date

today = date.today()
luna = today.strftime("%B")
def transformare_luna(luna):

    if luna=="February":
         luna="Februarie"

    elif luna=="March":
         luna="Martie"

    elif luna=="April":
        luna="Aprilie"

    elif luna=="June":
        luna="Iunie"

    elif luna=="July":
        luna="Iulie"

    elif luna=="August":
         luna="August"

    elif luna=="September":
        luna="Septembrie"

    elif luna=="October":
        luna="Octombrie"

    elif luna=="November":
        luna="Noiembrie"

    elif luna=="December":
        luna="Decembrie"

    elif luna=="January":
        luna="Ianuarie"
    else:
        return False

    return luna

transformare_luna(luna)



