"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    round_scores_list = []
    for i in range(len(student_scores)-1, -1, -1):
        round_scores_list.append(round(student_scores[i]))

    return round_scores_list


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count_failed = 0
    for i in range(len(student_scores)):
        if student_scores[i] <= 40:
            count_failed+=1

    return count_failed


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    top_scores = []
    for i in range(len(student_scores)):
        if student_scores[i] >= threshold:
            top_scores.append(student_scores[i])

    return top_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    interval = (highest - 40)/4
    grade_thresholds = [41]
    for i in range(1, 4):
        grade_thresholds.append(round(grade_thresholds[i-1] + interval))

    return grade_thresholds
        

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    new_list = zip(student_scores, student_names)
    formatted_list = []
    
    for rank, (score, name) in enumerate(new_list, start=1):
        formatted_list.append(f"{rank}. {name}: {score}")
        
    return formatted_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for i in range(len(student_info)):
        if student_info[i][1] == 100:
            return student_info[i]

    return []
