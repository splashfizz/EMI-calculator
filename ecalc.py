import streamlit as st

# Define a function to calculate emi
def emicalc(p,n,r):
	emi = p*(r/100)*((1+(r/100))**n)/((1+r/100)**n-1)
	st.write('EMI claculated=',round(emi,3))
	# Apply the formula


	# Print the calculted EMI on screen



# Add the title to the app
st.title('emi calculator')

# Take the inputs from user
principle=st.slider('loan amount',1000.0,100000.0)

# Calculate the 'n' and 'r' values
tenure=st.slider('tenure in years',1,30)
roi=st.slider('rate of interest',1.0,15.0)
# Create the button and event to calculate EMI. Call the function to calculate EMI.
n=tenure*12
r=roi/12
if st.button('calculate'):
	emicalc(principle,n,r)