'''

Author: Nihal

'''

import streamlit as st
import test
from pyairtable import Table

table = Table("keyJATezWi7crhHO2", "appjjEFJddbBeuBoN", "Table_1")

st.title("NLP Based Search")
sentence = st.text_input("Enter the search query")

if sentence:
    Ent_names, Ent_types = test.test(sent=sentence)
    st.write("Please provide a rating for the output")
    rating = st.radio("1 being the lowest and 5 being the highest", (1, 2, 3, 4, 5))
    rev = st.text_input("Please give feedback about the entity recognition model")
    st.write("Click Add Data to store the input:")
    if st.button("Add data"):
        table.create(
            {
                "Sentence": sentence,
                "Rating": rating,
                "Entity_Names": Ent_names,
                "Entity_Types": Ent_types,
                "Feedback": rev,
            }
        )
        st.title("Now you can try a new query")
        st.write("New queries to be over-written on the old query")
