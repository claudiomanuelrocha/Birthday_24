import streamlit as st


def main():
    st.image('Who_wants_.png', use_column_width=True)
    name = st.text_input("Enter your First Name")
    address = st.text_input("Enter your favourite Address")
    complete_sentence_0 = st.text_input("Complete: I am known as Miss....")
    complete_sentence = st.text_input("Complete: I love you more than....")

    # answers
    a_name = 'Elena'
    a_address = 'Portland'
    a_chocolate = 'Chocolate'
    a_brand = 'Cadbury'
    a_matcha = 'Matcha'
    a_trip = 'Trip'
    a_barcelona = 'Barcelona'

    if st.button("Submit"):
        # name
        if name.lower() == a_name.lower():
            st.write(f"\u2705 Hola guapa de mi vida!!! \U0001F60D \U0001F60D \U0001F60D")
        else:
            st.write("\u274C \U0001F644 \U0001F644 \U0001F644")

        # address
        if a_address.lower() in address.lower():
            st.write(f"\u2705 Yep, there is a great bakery just around the corner \U0001F92D")
        else:
            st.write("\u274C \U0001F914 \U0001F914 \U0001F914")
        # matcha
        if complete_sentence_0.lower() == a_matcha.lower():
            st.write(f"\u2705 Miss \U0001F375 \u2764")
        else:
            st.write("\u274C \U0001F525 \U0001F7E9")

        # chocolate
        if complete_sentence.lower() == a_chocolate.lower():
            st.write(f"\u274C Ok, but the brand.... \U0001F62C")
        elif a_brand.lower() in complete_sentence.lower():
            st.write(f"\u2705 That is quiet an achievement! \U0001F61A \U0001F36B")
        else:
            st.write("\u274C \U0001F440 \U0001F440 \U0001F440")

    if (complete_sentence.lower() == 'cadbury' and
            name.lower() == 'elena' and
            address.lower() == 'portland' and
            complete_sentence_0 == 'matcha'):
        trip = st.text_input("Your present for 2024 is....")
        if st.button("Confirm"):
            # trip
            if trip.lower() == a_trip.lower():
                st.write(f"\u274C Ok, but where.... \U0001F601")
                st.image('Barcelona.jpg', use_column_width=True)
                st.image('Gaudi.jpeg', use_column_width=True)
                st.image('Rose.png', use_column_width=True)
            elif trip.lower() == a_barcelona.lower():
                st.write("\u2705 \u2764 5 April - 9 April \u2764")
            else:
                st.write("\u274C \U0001F937 \U0001F937 \U0001F937 \U0001F4BC")


if __name__ == '__main__':
    main()

