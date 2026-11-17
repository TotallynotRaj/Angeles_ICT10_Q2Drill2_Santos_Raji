
from pyscript import document
import html

# Predefined members for each grade level
grade_7 = {"Soap Curry", "Aphia Batican", "Caela Regulation", "Leeroy Mides"}

grade_8 = {"Cheska Santos", "Cheska Torres", "Dezzarae Almirol", "Gab Ferrer"}

grade_9 = {"Kean Lardizabal", "Nastasia Tanglao", "Aubrey Cabrera", "Bella Canlas"}

grade_10 = {"Lacey Aguilar", "Megan Tan", "Lucas Tanglao", "Mica Frigillan"}

# Combine all four sets using the union operator
all_members = grade_7 | grade_8 | grade_9 | grade_10

def show_members():

    member_list = sorted(all_members)
    names = "<br>".join(html.escape(name) for name in member_list)

    output = f"""
        {names}
    """

    document.getElementById("member-output").innerHTML = output

    document.getElementById("member-count").innerText = (
        f"Total Members: {len(all_members)}"
    )

def add_member(event):

    global all_members

    first = document.getElementById("first-name").value.strip()
    last = document.getElementById("last-name").value.strip()

    full_name = f"{first} {last}".strip()
    new_member = {full_name}
    all_members = all_members | new_member

    show_members()

    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""

show_members()

