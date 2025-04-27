import streamlit as st
import pandas as pd

# Language selection with flags
language = st.selectbox(
    "Choose your language / Choisissez votre langue:",
    ("🇬🇧 English", "🇫🇷 Français")
)

st.title("BMI Calculator" if language == "🇬🇧 English" else "Calculateur d'IMC")

# User inputs
height = st.number_input(
    "Enter your height in meters:" if language == "🇬🇧 English" else "Entrez votre taille en mètres:",
    min_value=0.0,
    format="%.2f"
)
weight = st.number_input(
    "Enter your weight in kilograms:" if language == "🇬🇧 English" else "Entrez votre poids en kilogrammes:",
    min_value=0.0,
    format="%.1f"
)

if st.button("Calculate BMI" if language == "🇬🇧 English" else "Calculer l'IMC"):
    if height > 0:
        bmi = weight / (height ** 2)
        bmi = round(bmi, 1)

        if language == "🇬🇧 English":
            st.subheader(f"Your BMI is: {bmi}")
            if bmi < 18.5:
                st.warning("You are underweight.")
            elif bmi < 24.9:
                st.success("You are in the normal range.")
            elif bmi < 29.9:
                st.info("You are overweight.")
            else:
                st.error("You are obese.")
            
            # Show BMI Categories Table
            st.markdown("### BMI Categories")
            bmi_table = pd.DataFrame({
                "Category": ["Underweight", "Normal weight", "Overweight", "Obesity"],
                "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30 and above"]
            })
            st.table(bmi_table)

        else:  # French
            st.subheader(f"Votre IMC est : {bmi}")
            if bmi < 18.5:
                st.warning("Vous êtes en insuffisance pondérale.")
            elif bmi < 24.9:
                st.success("Vous êtes dans la norme.")
            elif bmi < 29.9:
                st.info("Vous êtes en surpoids.")
            else:
                st.error("Vous êtes obèse.")

            # Show BMI Categories Table
            st.markdown("### Catégories d'IMC")
            bmi_table = pd.DataFrame({
                "Catégorie": ["Insuffisance pondérale", "Poids normal", "Surpoids", "Obésité"],
                "Plage d'IMC": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30 et plus"]
            })
            st.table(bmi_table)

    else:
        st.error("Height must be greater than 0." if language == "🇬🇧 English" else "La taille doit être supérieure à 0.")
