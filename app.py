import streamlit as st
from google.cloud import firestore

# # Authenticate to Firestore with the JSON account key.
# db = firestore.Client.from_service_account_json("firestore-key.json")
#
# # Create a reference to the Google post.
# doc_ref = db.collection("posts").document("Google")
#
# # Then get the data at that reference.
# doc = doc_ref.get()
#
# # Let's see what we got!
# st.write("The id is: ", doc.id)
# st.write("The contents are: ", doc.to_dict())
#
#
# with st.container():
#     st.json({
#          'foo': 'bar',
#          'baz': 'boz',
#          'stuff': [
#              'stuff 1',
#              'stuff 2',
#              'stuff 3',
#              'stuff 5',
#          ],
#      })
print("Huy oky")