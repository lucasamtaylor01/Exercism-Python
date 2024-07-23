"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return coordinate[0], coordinate[1]


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    azara_coordinate = get_coordinate(azara_record)
    rui_coordinate = get_coordinate(rui_record)

    if azara_coordinate[0] == rui_coordinate[0] and azara_coordinate[1] == rui_coordinate[1]:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if azara_record[1][0] == rui_record[1][0] and azara_record[1][1] == rui_record[1][1]:
        return azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2]
    else:
        return "not a match"

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    
    cleaned_records = ""
    for record in combined_record_group:
        name = record[0]
        location = record[2]
        coordinates = record[3]
        color = record[4]
        
        formatted_record = f"('{name}', '{location}', {coordinates}, '{color}')\n"
        cleaned_records += formatted_record
    
    return cleaned_records
    
