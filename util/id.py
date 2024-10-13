def get_order_id(personality_id: int) -> int:
    first_three_digits = str(personality_id)[:3]

    match first_three_digits:
        case "101":
            return 1
        case "102":
            return 2
        case "103":
            return 3
        case "104":
            return 4
        case "105":
            return 5
        case "106":
            return 6
        case "107":
            return 7
        case "108":
            return 8
        case "109":
            return 9
        case "110":
            return 10
        case "111":
            return 11
        case "112":
            return 12
        case _:
            return 0
