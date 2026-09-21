import streamlit as st

# 1. Initialize our card deck state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# Sample flashcard data
flashcards = [
    {"word": "Ephemeral", "definition": "Lasting for a very short time."},
    {"word": "Capricious", "definition": "Given to sudden and unaccountable changes of mood or behavior."},
    {"word": "Mitigate", "definition": "Make less severe, serious, or painful."},
    {"word": "Desultory", "definition": "Lacking a plan or purpose, occuring randomly in a disoriented way"},
    {"word": "Veracious", "definition": "Truthful and honest in character"},
    {"word": "Vituperative", "definition": "Habitually attacking ppl with bitter and harsh words"},
    {"word": "Mercurial", "definition": "Habitually having sudden changes of mood; ~capricious"},
    {"word": "Temerity", "definition": "reckless audacity"},
    {"word": "Phlegmatic", "definition": "Emotionless, calm, stoic"}
]

st.title("GRE Flashcards 🗂️")
st.write("Click 'Know It' or 'Review Later' to sort through your deck.")

# Check if we have run out of cards
if st.session_state.card_index < len(flashcards):
    current_card = flashcards[st.session_state.card_index]
    
    # Render the card UI block
    with st.container(border=True):
        st.subheader(current_card["word"])
        
        # Simple toggle to simulate flipping a card over
        if st.button("👁️ Reveal Definition"):
            st.info(current_card["definition"])
            
    # Decision Buttons mimicking a Left/Right swipe
    col1, col2 = st.columns(2)
    with col1:
        if st.button("❌ Review Later (Swipe Left)", use_container_width=True):
            st.warning(f"Marked '{current_card['word']}' for review.")
            st.session_state.card_index += 1
            st.rerun()
            
    with col2:
        if st.button("✅ Know It! (Swipe Right)", use_container_width=True):
            st.success(f"Mastered '{current_card['word']}'!")
            st.session_state.card_index += 1
            st.rerun()
else:
    st.balloons()
    st.success("🎉 You've finished all the cards in this deck!")
    if st.button("🔄 Restart Deck"):
        st.session_state.card_index = 0
        st.rerun()
