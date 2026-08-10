import easygui as eg


def mi(miles):
    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360
    eg.msgbox(
        f"{miles} miles is equal to {yards} yards, {feet} feet, and {inches} inches."
    )


def km(kilometers):
    meters = kilometers * 1000
    centimeters = kilometers * 100000
    millimeters = kilometers * 1000000
    eg.msgbox(
        f"{kilometers} kilometers is equal to {meters} meters, {centimeters} centimeters, and {millimeters} millimeters."
    )


imp_met = eg.buttonbox("choose miles or km:", choices=["mi", "km"])
distance = eg.enterbox(f"Enter distance in {imp_met}: ")
match imp_met:
    case "mi":
        mi(float(distance))
    case "km":
        km(float(distance))
