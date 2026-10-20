from pyscript import document, display

def add_member(e):
    document.getElementById("output1").innerHTML = ""

    # Sets for each brand
    grade7 = {'Giorgio Armani', 'Thierry Hermès', 'Coco Chanel', 'Jeanne Lanvin'}
    grade8 = {'Yves Saint Laurent', 'Charles Lewis Tiffany', 'Sotirio Bulgari', 'Louis Vuitton'}
    grade9 = {'Cristóbal Balenciaga', 'Mario Prada', 'Guccio Gucci', 'Christian Dior'}
    grade10 = {'Pierre Balmain', 'Adele Fendi', 'Hubert de Givenchy', 'Valentino Garavani'}

    # Retrieve input values for first name and last name
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    # Combine first and last name and create a new set
    new_member_set = {f"{first_name} {last_name}"}

    # Combine all sets and the new member using union set operators (|)
    all_members_set = grade7 | grade8 | grade9 | grade10 | new_member_set

    total_members = len(all_members_set)

    member_list = "<br>".join(sorted(all_members_set))

    # Output
    document.getElementById("output1").innerHTML = f'All members:<br>{member_list}'
    display(f'Total members: {total_members}', target="output1")