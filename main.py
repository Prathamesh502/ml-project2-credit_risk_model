import streamlit as st

st.set_page_config(
    page_title="Credit Risk Modeling App",
    page_icon="💳",
    layout="wide"
)

# --- Inject JavaScript to detect screen width ---
st.markdown(
    """
    <script>
        const width = window.innerWidth;
        const url = new URL(window.location.href);
        url.searchParams.set("w", width);
        window.location.href = url.href;
    </script>
    """,
    unsafe_allow_html=True
)

# --- Read width param set by JS ---
params = st.query_params
w = params.get("w", [None])[0] if isinstance(params.get("w"), list) else params.get("w")
try:
    width = int(w) if w is not None else None
except:
    width = None

is_mobile = (width is not None and width < 768)  # breakpoint for mobile


# --- Common Title ---
st.markdown(
    "<div style='text-align:center; font-size:2em; font-weight:800; "
    "background:linear-gradient(90deg,#ff6a00,#ee0979); "
    "-webkit-background-clip:text; -webkit-text-fill-color:transparent;'>"
    "💳 Credit Risk Modeling App 🚀</div>",
    unsafe_allow_html=True
)


# --- UI Logic ---
if not is_mobile:
    # ========== DESKTOP UI ==========
    st.subheader("🖥️ Desktop View")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.number_input("Age", 18, 100, 30)
    with col2:
        income = st.number_input("Income", 0, 1000000, 50000, step=1000)
    with col3:
        loan_amount = st.number_input("Loan Amount", 0, 10000000, 100000, step=1000)
    with col4:
        loan_tenure_month = st.number_input("Loan Tenure (Months)", 1, 360, 24)

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        avg_dpd = st.number_input("Avg DPD", 0, 365, 0)
    with col6:
        credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", 0, 100)
    with col7:
        residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])
    with col8:
        loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])

    col9, col10, col11, col12 = st.columns(4)
    with col9:
        loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])
    with col10:
        delinquency_ratio = st.number_input("Delinquency Ratio (%)", 0, 100)
    with col11:
        open_loan_accounts = st.number_input("Open Loan Accounts", 0, 100, 1)
    with col12:
        loan_to_income_ratio = loan_amount / income if income > 0 else 0
        st.metric("Loan-to-Income Ratio", f"{loan_to_income_ratio*100:.2f}%")


else:
    # ========== MOBILE UI ==========
    st.subheader("📱 Mobile View")

    with st.expander("📌 Basic Details", expanded=True):
        age = st.number_input("Age", 18, 100, 30)
        income = st.number_input("Income", 0, 1000000, 50000, step=1000)
        loan_amount = st.number_input("Loan Amount", 0, 10000000, 100000, step=1000)
        loan_tenure_month = st.number_input("Loan Tenure (Months)", 1, 360, 24)

    with st.expander("📊 Credit Behavior", expanded=True):
        avg_dpd = st.number_input("Avg DPD", 0, 365, 0)
        credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", 0, 100)
        delinquency_ratio = st.number_input("Delinquency Ratio (%)", 0, 100)
        open_loan_accounts = st.number_input("Open Loan Accounts", 0, 100, 1)

    with st.expander("🏠 Loan & Residence", expanded=True):
        residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])
        loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])
        loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])

    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    st.metric("Loan-to-Income Ratio", f"{loan_to_income_ratio*100:.2f}%")


# --- Prediction Button (common backend) ---
if st.button("🚀 Predict Credit Risk"):
    from prediction_helper import predict
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_month, avg_dpd,
        credit_utilization_ratio, open_loan_accounts,
        delinquency_ratio, residence_type, loan_purpose,
        loan_type, loan_to_income_ratio
    )
    st.success(f"📊 Probability of default: {probability:.2f}%")
    st.info(f"💳 Credit Score: {credit_score}")
    st.warning(f"⭐ Rating: {rating}")
