from gpt_functions import generate_name_suggestions
from select_data import *
from streamlit.components.v1 import html
import streamlit as st
import random

other_background = False
other_country = False
other_religion = False
other_siblings = False

def confetti_animation():
    return """
        <script>
            var confettiSettings = { target: 'confetti', max: 100 };
            var confetti = new ConfettiGenerator(confettiSettings);
            confetti.render();
        </script>
        <div id="confetti"></div>
    """

def main():
    # Header
    st.title("BabyNameGPT")

    random_tag_line = random.choice(tag_lines)
    st.markdown(f"### {random_tag_line}")

    # Space between header and config variables
    st.write("\n\n")

    # Config variables
    st.sidebar.markdown("### Configuration Options")

    # Gender
    gender = st.sidebar.radio("Gender", gender_list)

    # Nationality
    nationality = st.sidebar.selectbox("Nationality", country_list)

    if nationality=="Others (Specify)":
        custom_nationality = st.sidebar.text_input("Enter the name of your Country")
        other_country = True
    else:
        other_country = False

    # Cultural Background
    cultural_background = st.sidebar.selectbox("Cultural Background", background_list)

    if cultural_background=="Others (Specify)":
        # allow the user to enter a custom value
        custom_cultural_background = st.sidebar.text_input("Enter your custom cultural background")
        other_background = True
    else:
        other_background = False

    # Theme Preferences
    theme_preferences = st.sidebar.multiselect("Theme Preferences", theme_list)

    # Sound or Letter Preferences
    sound_letter_preferences = st.sidebar.radio("Sound or Letter Preferences", ["Soft sounds", "Strong sounds", "Alliteration", "Rhyming", "Other (Specify)"])


    #religious preferences
    religious_views = st.sidebar.selectbox("Religious Views", religion_list)

    if religious_views=="Others (Specify)":
        custom_religious_views = st.sidebar.text_input("Enter your Religious preference")
        other_religion = True
    else:
        other_religion = False

    # Family Heritage
    family_heritage = st.sidebar.text_input("Family Heritage")

    # Personal Meaning
    personal_meaning = st.sidebar.text_area("Personal Meaning")

    # Sibling Name Compatibility
    sibling_compatibility = st.sidebar.radio("Sibling Name Compatibility", yes_no_list, index=1)
    
    if sibling_compatibility == "Yes":
        sibling_names = st.sidebar.text_input("Enter Names of siblings seperated by commas")
        other_siblings = True
    else:
        other_siblings = False

    # Name Length
    # add the option to choose which letter they don't want appearing, etc...
    name_length = st.sidebar.radio("Name Length", name_length_list)

    # Language
    language = st.sidebar.selectbox("Language", language_list)
    
    if language=="Others (Specify)":
        custom_language = st.sidebar.text_input("Enter your language preference")
        other_language = True
    else:
        other_language = False

    # Tribe
    tribe = st.sidebar.text_input("Tribe")

    # Add a button to submit options
    if st.sidebar.button("Submit"):

        # Make request to GPT

        response = generate_name_suggestions(
            cultural_background=custom_cultural_background if other_background else cultural_background,
            theme_preferences=', '.join(theme_preferences),
            sound_preferences=sound_letter_preferences,
            religious_context=custom_religious_views if other_religion else religious_views,
            family_heritage=family_heritage,
            personal_meaning=personal_meaning,
            sibling_compatibility=sibling_names if other_siblings else sibling_compatibility,
            name_length=name_length,
            language=custom_language if other_language else language,
            tribe=tribe,
            gender=gender,
            nationality=custom_nationality if other_country else nationality
        )

        # Display the generated output.
        st.write("### Here are the Top 5 names for your baby")
        

        st.write(response[0].choices[0].message.content)
        print("Done with request")
        print(response[1])

        # Display confetti animation after generating suggestions
        st.components.v1.html(confetti_animation(), height=300)

        

    
    else:

        st.write("### Submit to view our Suggestions!")

if __name__ == "__main__":
    main()
