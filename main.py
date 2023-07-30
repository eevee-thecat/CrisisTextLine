import re


def adminQuestions(questions):
    answers = []
    for q in questions:
        print(q, end=" ")
        invalid = True
        while invalid:
            invalid = False
            ans_current = input("Enter 'Y' or 'N': ").upper()
            if ans_current == "Y" or ans_current == "N":
                answers.append(ans_current)
            else:
                print(q, end=" ")
                invalid = True

    return answers


def new_texter(queue):
    def validNumber(phone_nuber):
        pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$", re.IGNORECASE)
        return pattern.match(phone_nuber) is not None

    questions = [
        "1. In the past few weeks, have you wished you were dead? ",
        "2. In the past few weeks, have you felt that you or your family would be better off if you were dead? ",
        "3. In the past week, have you been having thoughts about killing yourself? ",
        "4. Have you ever tried to kill yourself? ",
        "5. Are you having thoughts of killing yourself right now? ",
    ]

    print(
        "Thank you for reaching out to CrisisTextLine today. Before we match you up with a Crisis Counsellor, we would like to ask you some questions and get a general idea of your safety."
    )
    while True:
        id = input(
            "What is the phone number you are texting us with today? Enter in the format XXX-XXX-XXXX: "
        )
        if validNumber(id):
            break
        else:
            print("Please enter a valid phone number in the format XXX-XXX-XXXX")

    print("\n")
    response = adminQuestions(questions[0:4])
    answered_yes = 0
    for ans in response:
        if ans == "Y":
            answered_yes += 1

    if answered_yes >= 4:
        while True:
            response = input(f"{questions[4]} Enter 'Y' or 'N': ").upper()
            if response == "Y":
                risk = "High"
                break
            elif response == "N":
                risk = "Mod"
                break
            else:
                print("Please enter a valid response, 'Y' or 'N'")
    else:
        risk = "Low"

    queue[id] = risk
    print("\n")
    print(
        "Thank you for taking the time to answer the questions. A Crisis Counsellor will be with you shortly."
    )
    input("Enter anything to return to the main menu. ")
    print("\n")

    return queue


def print_queue(queue):
    for phone, risk in queue.items():
        print(f"Phone: {phone}\tRisk: {risk}")
    input("Enter anything to return to the menu. ")
    pass


def sort_queue(queue):
    risk_to_prio = {"High": 1, "Mod": 2, "Low": 3}
    queue_list = [(pair[0], pair[1]) for pair in queue.items()]
    queue_list.sort(key=lambda pair: risk_to_prio[pair[1]])

    return {pair[0]: pair[1] for pair in queue_list}


def queue_health(queue):
    queue_len = len(queue)
    print(f"There are currently: {queue_len} texter(s) waiting in the queue.")
    if queue_len >= 15:
        print(
            "There are a lot of texters waiting in the queue right now! We might want to get some more Crisis Counsellors Online to help clear out the queue."
        )
    elif queue_len >= 10:
        print(
            "The texters in the queue are building up. We should reach out to our online Crisis Counsellors to see if they can try to take an extra conversation."
        )
    else:
        print("The queue health looks good! :)")

    input("Enter anything to return to the menu. ")
    pass


def menu(queue):
    while True:
        print("--------------------------------------")
        print(
            """Please choose an option:
0. Exit program.
1. Add a new texter to the queue.
2. View current queue.
3. View queue health.
"""
        )
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Error: Please select a valid menu entry")
            continue

        if not 0 <= choice <= 3:
            print("Error: Please select a valid menu entry")
            continue

        if choice == 0:
            print("Goodbye!")
            exit(0)
        elif choice == 1:
            queue = new_texter(queue)
            queue = sort_queue(queue)
        elif choice == 2:
            print_queue(queue)
        elif choice == 3:
            queue_health(queue)


def main():
    texters_in_queue = {}
    print("Welcome to CrisisTextLine. \n")
    menu(texters_in_queue)


main()
