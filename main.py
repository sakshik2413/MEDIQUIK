import streamlit as st
import requests

def get_background_image(category):
    # Define keywords related to medicine
    keywords = {
        "Analgesics": "medicine",
        "Antibiotics": "medicine",
        'Antihistamines': "medicine",
        'Antacids': "medicine",
        'Anti-inflammatories': "medicine",
        'Antipyretics': "medicine",
        'Antidiabetics' : "medicine",
        'Bronchodilators': "medicine",
        'Cholesterol-lowering drugs' : "medicine",
        'Antidepressants': "medicine",
        # Add more categories and corresponding keywords as needed
    }
    
    # Get a random image based on the keyword for the category
    if category in keywords:
        keyword = keywords[category]
        response = requests.get(f"https://source.unsplash.com/featured/?{keyword}")
        if response.status_code == 200:
            return response.url
        else:
            # If request fails, return a default image or handle the error accordingly
            return "https://www.vitalmamas.com/wp-content/uploads/2017/09/medicine.jpg"  # Provide a URL to a default image
    else:
        # If category is not found in keywords, return a default image or handle it accordingly
        return "https://www.vitalmamas.com/wp-content/uploads/2017/09/medicine.jpg"  # Provide a URL to a default image

# Simulated user authentication
def authenticate(username, password):
    return True if username == "admin" and password == "password" else False

# Simulated previous orders for users
previous_orders = {
    "admin": [
       
    ],
    "user1": [
        
    ]
}

# Define the list of available medicine categories
medicine_categories = [
    'Analgesics', 'Antibiotics', 'Antihistamines', 'Antacids', 'Anti-inflammatories',
    'Antipyretics', 'Antidiabetics', 'Bronchodilators', 'Cholesterol-lowering drugs', 'Antidepressants',
]

# Define medicine recommendations
medicine_recommendations = {
    "Analgesics": "These medications are commonly used for pain relief. Examples include paracetamol (acetaminophen) and ibuprofen.",
    "Antibiotics": "Used to treat bacterial infections. Common antibiotics include amoxicillin, azithromycin, and ciprofloxacin.",
    "Antihistamines": "Help relieve allergy symptoms such as sneezing, itching, and runny nose. Loratadine and cetirizine are common antihistamines.",
    "Antacids": "Used to neutralize stomach acid and relieve symptoms of heartburn and indigestion. Examples include omeprazole and ranitidine.",
    "Anti-inflammatories": "These medications reduce inflammation and can help with conditions like arthritis. Ibuprofen and naproxen are common examples.",
    "Antipyretics": "Medications that reduce fever. Paracetamol (acetaminophen) is a widely used antipyretic.",
    "Antidiabetics": "Used to manage blood sugar levels in people with diabetes. Examples include metformin, insulin, and glipizide.",
    "Bronchodilators": "Help open up the airways in the lungs, making it easier to breathe. Salbutamol and ipratropium are common bronchodilators.",
    "Cholesterol-lowering drugs": "Medications used to lower cholesterol levels in the blood. Examples include statins like atorvastatin and simvastatin.",
    "Antidepressants": "Prescribed to treat depression and other mood disorders. Common antidepressants include sertraline, fluoxetine, and escitalopram.",
    
}

# Define the Streamlit app layout
def main():
    session_state = st.session_state
    st.image("https://cdn.dribbble.com/users/5874543/screenshots/14201310/mediquik_logo-1_.png", width=250, use_column_width=False)
    st.title("MediQuik - Your Health, Our Priority")
    
    
    st.markdown("""
        <style>
            .reportview-container .main .block-container {
                max-width: 100%;
            }
            .reportview-container .main {
                padding-top: 0rem;
            }
            .reportview-container .main .block-container {
                padding-top: 0rem;
                padding-right: 0rem;
                padding-left: 0rem;
            }
            .reportview-container .main .block-container .block-content {
                padding-right: 0rem;
                padding-left: 0rem;
            }
            .reportview-container .main .block-container .block-content p {
                margin-bottom: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Navigation Bar
    menu_option = st.selectbox("Menu", ["Home", "About", "Login"])

    if menu_option == "Home":
        st.write("Welcome to MediQuik! MediQuik is a comprehensive pharmacy designed to streamline and enhance the operations of pharmacies, ensuring efficient management of medications, prescriptions, inventory, and customer interactions.")
        st.image("https://static.vecteezy.com/system/resources/previews/000/304/305/original/a-set-of-medicine-vector.jpg", width=650, use_column_width=False)
    elif menu_option == "About":
        st.write("About MediQuik: At MediQuik, our mission is to revolutionize pharmacies by delivering comprehensive, intuitive, and scalable solutions that meet the evolving needs of pharmacies and healthcare providers. We are committed to enabling pharmacies to operate more efficiently, improve patient outcomes, and thrive in an increasingly competitive market.")
        st.image("https://medkare.co/wp-content/uploads/2021/05/vector-a-set-of-medicine-and-prescription-removebg-preview-2048x1773.png", width=650, use_column_width=False)
    elif menu_option == "Login":
        st.sidebar.title("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if authenticate(username, password):
                st.sidebar.success("Login successful!")
                session_state.logged_in = True
                session_state.user = username
            else:
                st.sidebar.error("Invalid credentials")

    # Check if the user is logged in before accessing user-specific data
    if session_state.get("logged_in"):
        st.sidebar.subheader(f"Logged in as: {session_state.user}")
        if st.sidebar.button("Logout"):
            session_state.logged_in = False
            session_state.user = None
        
        medicine_categories = {
            "Analgesics": {
                "Paracetamol": { "price": 350, "pack_size": "per pack of 20 tablets", "quantity":100 },
                "Ibuprofen": {"price": 490, "pack_size": "per pack of 24 tablets", "quantity":80},
                "Aspirin": { "price": 280, "pack_size": "per pack of 50 tablets", "quantity":120},
                "Acetaminophen": { "price": 420, "pack_size": "per pack of 30 caplets", "quantity":90},
            },
            "Antibiotics": {
                    "Amoxicillin": {"price": 700, "pack_size":"per bottle of 30 capsules","quantity": 50 },
                    "Azithromycin": {"price": 1050,"pack_size":"per pack of 6 tablets","quantity": 40 },
                    "Cephalexin": {"price": 560,"pack_size":"per bottle of 20 capsules","quantity": 60 },
                    "Doxycycline": {"price": 840,"pack_size":"per pack of 14 tablets","quantity": 70 },
            },
            "Antihistamines": {
                     "Loratadine": {
            "price": 560,
            "pack_size": "per pack of 24 tablets",
            "quantity": 80
        },
        "Cetirizine": {
            "price": 420,
            "pack_size": "per pack of 30 tablets",
            "quantity": 100
        },
        "Diphenhydramine": {
            "price": 350,
            "pack_size": "per pack of 12 caplets",
            "quantity": 120
        },
        "Fexofenadine": {
            "price": 700,
            "pack_size": "per pack of 20 tablets",
            "quantity": 60
        }
    },
    "Antacids": {
        "Tums": {
            "price": 490,
            "pack_size": "per bottle of 60 tablets",
            "quantity": 100
        },
        "Rolaids": {
            "price": 350,
            "pack_size": "per pack of 36 tablets",
            "quantity": 80
        },
        "Maalox": {
            "price": 420,
            "pack_size": "per bottle of 12 fluid ounces",
            "quantity": 70
        },
        "Mylanta": {
            "price": 560,
            "pack_size": "per bottle of 24 caplets",
            "quantity": 90
        }
    },
    "Anti-inflammatories": {
        "Prednisone": {
            "price": 700,
            "pack_size": "per pack of 20 tablets",
            "quantity": 50
        },
        "Naproxen": {
            "price": 560,
            "pack_size": "per pack of 24 tablets",
            "quantity": 70
        },
        "Celecoxib": {
            "price": 840,
            "pack_size": "per pack of 10 capsules",
            "quantity": 40
        },
        "Diclofenac": {
            "price": 630,
            "pack_size": "per pack of 30 tablets",
            "quantity": 60
        }
    },
    "Antipyretics": {
        "Paracetamol": {
            "price": 350,
            "pack_size": "per pack of 20 tablets",
            "quantity": 100
        }
    },
    "Antidiabetics": {
        "Metformin": {
            "price": 1050,
            "pack_size": "per bottle of 60 tablets",
            "quantity": 40
        },
        "Insulin": {
            "price": 1400,
            "pack_size": "per vial",
            "quantity": 50
        },
        "Glipizide": {
            "price": 700,
            "pack_size": "per pack of 30 tablets",
            "quantity": 60
        },
        "Sitagliptin": {
            "price": 1260,
            "pack_size": "per pack of 28 tablets",
            "quantity": 30
        }
    },
    "Bronchodilators": {
        "Albuterol": {
            "price": 1050,
            "pack_size": "per inhaler",
            "quantity": 60
        },
        "Salmeterol": {
            "price": 1400,
            "pack_size": "per inhaler",
            "quantity": 50
        },
        "Formoterol": {
            "price": 1260,
            "pack_size": "per inhaler",
            "quantity": 40
        },
        "Ipratropium": {
            "price": 840,
            "pack_size": "per inhaler",
            "quantity": 70
        }
    },
    "Cholesterol-lowering drugs": {
        "Atorvastatin": {
            "price": 700,
            "pack_size": "per pack of 30 tablets",
            "quantity": 80
        },
        "Simvastatin": {
            "price": 560,
            "pack_size": "per pack of 20 tablets",
            "quantity": 90
        },
        "Rosuvastatin": {
            "price": 840,
            "pack_size": "per pack of 10 tablets",
            "quantity": 60
        },
        "Pravastatin": {
            "price": 630,
            "pack_size": "per pack of 30 tablets",
            "quantity": 70
        }
    },
    "Antidepressants": {
        "Sertraline": {
            "price": 700,
            "pack_size": "per pack of 30 tablets",
            "quantity": 80
        },
        "Fluoxetine": {
            "price": 560,
            "pack_size": "per pack of 20 capsules",
            "quantity": 90
        },
        "Escitalopram": {
            "price": 840,
            "pack_size": "per pack of 28 tablets",
            "quantity": 60
        },
        "Venlafaxine": {
            "price": 1050,
            "pack_size": "per pack of 14 capsules",
            "quantity": 70
        },
            }
        }

        st.markdown("---")
        st.write("### Medicine Categories:")
        st.markdown("---")
        # Medicine Categories with Sub-options
        selected_category = st.sidebar.selectbox("Select a Category", medicine_categories)

        if selected_category:
            st.write(f"## {selected_category}")
            for medicine, details in medicine_categories[selected_category].items():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(get_background_image(selected_category), use_column_width=True)
                with col2:
                    selected = st.checkbox(f"{medicine} - ₹{details['price']} | {details['pack_size']} | Quantity: {details['quantity']}", key=medicine)
                    if selected:
                        selected_medicine = {
                            "medicine": medicine,
                            "category": selected_category,
                            "price": details['price']
                        }
                        if session_state.user in previous_orders:
                            previous_orders[session_state.user].append(selected_medicine)
                        else:
                            previous_orders[session_state.user] = [selected_medicine]
        st.markdown("---")
        st.write("### Selected Medicines:")
        total_cost = 0
        for order in previous_orders.get(session_state.user, []):
            st.write(f"- {order['medicine']} (₹{order['price']})")
            total_cost += order['price']

        st.write(f"### Total Cost: ₹{total_cost}")

        if st.button("Place Order"):
            if len(previous_orders.get(session_state.user, [])) == 0:
                st.error("Please select at least one medicine.")
            else:
                st.success("Order placed successfully!")
                st.write("### Order Summary:")
                st.write("#### Selected Medicines:")
                for order in previous_orders[session_state.user]:
                    st.write(f"- {order['medicine']} (₹{order['price']})")
                    st.write(f"#### Total Cost: ₹{total_cost}")
       

    # Display Previous Orders
    if session_state.get("logged_in"):
        if session_state.user in previous_orders:
            st.write("### Previous Orders:")
            for order in previous_orders[session_state.user]:
                st.write(f"- {order['medicine']} (₹{order['price']})")

    # Display Medicine Recommendations
    st.write("### Medicine Recommendations:")
    for medicine, recommendation in medicine_recommendations.items():
        st.write(f"- {medicine}: {recommendation}")

if __name__ == "__main__":
    main()