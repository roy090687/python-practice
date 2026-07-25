def student_info(name, subject, dept="CS", year=1, *hobbies, **details):
    print("Name:", name)                      # Positional
    print("Subject:", subject)                # Positional
    print("Department:", dept)                 # Default
    print("Year:", year)                       # Default
    print("Hobbies (tuple):", hobbies)         # Positional arbitrary (*args)
    print("Details (dict):", details)          # Keyword arbitrary (**kwargs)

# Call 1 → Positional + Default
student_info("Roy", "Python")
# dept → "CS" (default), year → 1 (default)

# Call 2 → Keyword overrides default
student_info("Snehasish", "Automation", dept="IT", year=3)

# Call 3 → With arbitrary positional + keyword
student_info("Anita", "Maths", "Science", 2, "Reading", "Music", city="Kolkata", grade="A")
