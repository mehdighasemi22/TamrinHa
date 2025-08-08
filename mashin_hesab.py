def mashin_hesab(a: float, b: float, operation: str):
    match operation:
        case "jam":
            return a + b
        case "tafrigh":
            return a - b
        case "zarb":
            return a * b
        case "taghsim":
            if b == 0:
                return "nemishe"
            return a / b          
        case _:
            return "nemishe"
