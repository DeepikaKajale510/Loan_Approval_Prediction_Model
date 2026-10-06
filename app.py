import streamlit as st
import pandas as pd
import joblib


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Loan Approval AI",
    page_icon="🏦",
    layout="wide"
)


# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():
    return joblib.load("loan_model.pkl")


model = load_model()


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    /* ---------- Main Background ---------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #f5f7fb 0%,
            #eef3ff 50%,
            #f8faff 100%
        );
    }


    /* ---------- Hero ---------- */

    .hero {
        background: linear-gradient(
            135deg,
            #172554,
            #2563eb,
            #4f46e5
        );

        padding: 35px 40px;
        border-radius: 20px;
        margin-bottom: 25px;

        box-shadow:
            0 10px 30px rgba(37, 99, 235, 0.25);
    }

    .hero h1 {
        font-size: 42px;
        font-weight: 800;
        margin: 0;
        padding: 0;
        color: white;
    }

    .hero p {
        font-size: 18px;
        margin: 8px 0 0 0;
        padding: 0;
        color: white;
        opacity: 0.92;
    }


    /* ---------- Section Titles ---------- */

    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #172554;
        margin-top: 15px;
        margin-bottom: 15px;
    }


    /* ---------- Snapshot Cards ---------- */

    .feature-card {
        background: white;
        padding: 18px;

        border-radius: 15px;

        border: 1px solid #e5e7eb;

        text-align: center;

        box-shadow:
            0 4px 15px rgba(0, 0, 0, 0.04);
    }

    .feature-icon {
        font-size: 28px;
    }

    .feature-title {
        font-size: 14px;
        color: #64748b;
        margin-top: 5px;
    }

    .feature-value {
        font-size: 21px;
        font-weight: 750;
        color: #172554;
    }


    /* ---------- Result Card ---------- */

    .result-card {
        background: white;

        border-radius: 20px;

        padding: 30px;

        text-align: center;

        border: 1px solid #e5e7eb;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.08);

        margin-top: 20px;
        margin-bottom: 25px;
    }

    .result-icon {
        font-size: 55px;
    }

    .result-title {
        font-size: 32px;
        font-weight: 800;
        color: #172554;
    }

    .result-label {
        color: #64748b;
        font-size: 16px;
    }

    .result-probability {
        font-size: 48px;
        font-weight: 800;
        color: #2563eb;
        margin-top: 5px;
    }


    /* ---------- Buttons ---------- */

    .stButton > button {
        border-radius: 12px;

        font-weight: 700;

        min-height: 48px;

        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 6px 15px rgba(37, 99, 235, 0.20);
    }


    /* ---------- Footer ---------- */

    .footer {
        text-align: center;

        color: #64748b;

        padding: 25px;

        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# HERO HEADER
# ==========================================================

st.markdown(
    '<div class="hero">'
    '<h1>🏦 Loan Approval AI</h1>'
    '<p>Intelligent loan approval prediction powered by Machine Learning</p>'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================================
# ABOUT THE MODEL
# ==========================================================

with st.expander("🤖 About This AI Model"):

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 🧠 Algorithm")

        st.write("Logistic Regression")


    with col2:

        st.markdown("### ⚙️ Preprocessing")

        st.write(
            "One-Hot Encoding + Standardization"
        )


    with col3:

        st.markdown("### 🎯 Output")

        st.write(
            "Prediction + Approval Probability"
        )


    st.divider()

    st.write(
        "This application uses a Logistic Regression "
        "machine learning model to estimate whether a "
        "loan application is likely to be approved."
    )

    st.write(
        "The model considers applicant income, credit score, "
        "employment experience, loan amount, interest rate, "
        "loan purpose, education, home ownership and "
        "previous loan history."
    )


# ==========================================================
# APPLICANT PROFILE
# ==========================================================

st.markdown(
    '<div class="section-title">👤 Applicant Profile</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# ---------- Column 1 ----------

with col1:

    gender = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    age = st.slider(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    education = st.selectbox(
        "Education",
        [
            "Bachelor",
            "Associate",
            "High School",
            "Master",
            "Doctorate"
        ]
    )


# ---------- Column 2 ----------

with col2:

    person_income = st.number_input(
        "Annual Income (₹)",
        min_value=0,
        value=50000,
        step=5000
    )

    employee_experience = st.slider(
        "Employment Experience (Years)",
        min_value=0,
        max_value=50,
        value=2
    )

    home_onwership = st.selectbox(
        "Home Ownership",
        [
            "RENT",
            "MORTGAGE",
            "OWN",
            "OTHER"
        ]
    )


# ---------- Column 3 ----------

with col3:

    credit_score = st.slider(
        "Credit Score",
        min_value=300,
        max_value=850,
        value=650
    )

    credit_history = st.number_input(
        "Credit History",
        min_value=0,
        value=3,
        step=1
    )

    previous_loan = st.selectbox(
        "Previous Loan",
        ["Yes", "No"]
    )


# ==========================================================
# LOAN DETAILS
# ==========================================================

st.divider()

st.markdown(
    '<div class="section-title">💰 Loan Details</div>',
    unsafe_allow_html=True
)

col4, col5, col6 = st.columns(3)


# ---------- Loan Amount ----------

with col4:

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        min_value=0,
        value=10000,
        step=1000
    )


# ---------- Interest Rate ----------

with col5:

    loan_interest_rate = st.slider(
        "Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=10.0,
        step=0.1
    )


# ---------- Loan Purpose ----------

with col6:

    loan_intent = st.selectbox(
        "Loan Purpose",
        [
            "EDUCATION",
            "MEDICAL",
            "VENTURE",
            "PERSONAL",
            "DEBTCONSOLIDATION",
            "HOMEIMPROVEMENT"
        ]
    )


# ==========================================================
# LOAN TO INCOME RATIO
# ==========================================================

if person_income > 0:

    loan_percentage = (
        loan_amount / person_income
    )

else:

    loan_percentage = 0


ratio_col1, ratio_col2 = st.columns([2, 1])


with ratio_col1:

    st.info(
        f"📊 **Loan-to-Income Ratio:** "
        f"{loan_percentage:.2f} "
        f"({loan_percentage * 100:.1f}%)"
    )


with ratio_col2:

    if loan_percentage <= 0.20:

        st.success(
            "🟢 Low Loan Burden"
        )

    elif loan_percentage <= 0.50:

        st.warning(
            "🟡 Moderate Loan Burden"
        )

    else:

        st.error(
            "🔴 High Loan Burden"
        )


# ==========================================================
# APPLICATION SNAPSHOT
# ==========================================================

st.divider()

st.markdown(
    '<div class="section-title">📋 Application Snapshot</div>',
    unsafe_allow_html=True
)

snap1, snap2, snap3, snap4 = st.columns(4)


with snap1:

    st.markdown(
        f'<div class="feature-card">'
        f'<div class="feature-icon">💵</div>'
        f'<div class="feature-title">Annual Income</div>'
        f'<div class="feature-value">₹{person_income:,.0f}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with snap2:

    st.markdown(
        f'<div class="feature-card">'
        f'<div class="feature-icon">💰</div>'
        f'<div class="feature-title">Loan Amount</div>'
        f'<div class="feature-value">₹{loan_amount:,.0f}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with snap3:

    st.markdown(
        f'<div class="feature-card">'
        f'<div class="feature-icon">📈</div>'
        f'<div class="feature-title">Credit Score</div>'
        f'<div class="feature-value">{credit_score}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with snap4:

    st.markdown(
        f'<div class="feature-card">'
        f'<div class="feature-icon">💼</div>'
        f'<div class="feature-title">Experience</div>'
        f'<div class="feature-value">{employee_experience} years</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ==========================================================
# PREDICT BUTTON
# ==========================================================

st.write("")

button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)


with button_col2:

    predict_button = st.button(
        "🚀 Predict Loan Approval",
        use_container_width=True
    )


# ==========================================================
# RESET BUTTON
# ==========================================================

reset_col1, reset_col2, reset_col3 = st.columns(
    [1, 2, 1]
)


with reset_col2:

    reset_button = st.button(
        "🔄 Reset Application",
        use_container_width=True
    )


if reset_button:

    st.rerun()


# ==========================================================
# PREDICTION
# ==========================================================

if predict_button:

    # ------------------------------------------------------
    # VALIDATION
    # ------------------------------------------------------

    if person_income <= 0:

        st.warning(
            "⚠️ Please enter a valid annual income."
        )

        st.stop()


    if loan_amount <= 0:

        st.warning(
            "⚠️ Please enter a valid loan amount."
        )

        st.stop()


    # ------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # ------------------------------------------------------

    input_data = pd.DataFrame({

        "gender": [gender],

        "education": [education],

        "person_income": [person_income],

        "employee_experience": [employee_experience],

        "home_onwership": [home_onwership],

        "loan_amount": [loan_amount],

        "loan_intent": [loan_intent],

        "loan_interest_rate": [loan_interest_rate],

        "loan_percentage": [loan_percentage],

        "credit_history": [credit_history],

        "credit_score": [credit_score],

        "previous_loan": [previous_loan],

        "age": [age]

    })


    # ------------------------------------------------------
    # PREDICTION
    # ------------------------------------------------------

    prediction = model.predict(
        input_data
    )[0]


    probability = model.predict_proba(
        input_data
    )[0][1]


    probability_percentage = (
        probability * 100
    )


    # ======================================================
    # PREDICTION RESULT
    # ======================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🎯 Prediction Result'
        '</div>',
        unsafe_allow_html=True
    )


    if prediction == 1:

        result_icon = "🎉"

        result_text = "Loan Approved"

        result_message = (
            "The model predicts a positive loan approval outcome."
        )

    else:

        result_icon = "⚠️"

        result_text = "Loan Not Approved"

        result_message = (
            "The model predicts a negative loan approval outcome."
        )


    # ------------------------------------------------------
    # RESULT CARD
    # ------------------------------------------------------

    st.markdown(
        f'<div class="result-card">'
        f'<div class="result-icon">{result_icon}</div>'
        f'<div class="result-title">{result_text}</div>'
        f'<div class="result-label">{result_message}</div>'
        f'<br>'
        f'<div class="result-label">'
        f'Estimated Approval Probability'
        f'</div>'
        f'<div class="result-probability">'
        f'{probability_percentage:.2f}%'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


    # ------------------------------------------------------
    # PROGRESS BAR
    # ------------------------------------------------------

    st.progress(
        probability,
        text=(
            f"Approval Probability: "
            f"{probability_percentage:.2f}%"
        )
    )


    # ------------------------------------------------------
    # PROBABILITY INTERPRETATION
    # ------------------------------------------------------

    if probability_percentage >= 80:

        st.success(
            "🟢 **High Confidence:** "
            "The model estimates a strong likelihood of approval."
        )

    elif probability_percentage >= 50:

        st.warning(
            "🟡 **Moderate Confidence:** "
            "The application is near the model's decision boundary."
        )

    else:

        st.error(
            "🔴 **Low Confidence:** "
            "The model estimates a lower likelihood of approval."
        )


    # ======================================================
    # KEY METRICS
    # ======================================================

    st.markdown(
        '<div class="section-title">'
        '📊 Key Application Metrics'
        '</div>',
        unsafe_allow_html=True
    )


    metric1, metric2, metric3, metric4 = st.columns(4)


    with metric1:

        st.metric(
            "Credit Score",
            credit_score
        )


    with metric2:

        st.metric(
            "Annual Income",
            f"₹{person_income:,.0f}"
        )


    with metric3:

        st.metric(
            "Loan Amount",
            f"₹{loan_amount:,.0f}"
        )


    with metric4:

        st.metric(
            "Loan / Income",
            f"{loan_percentage:.2f}"
        )


    # ======================================================
    # WHY DID THE MODEL MAKE THIS PREDICTION?
    # ======================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '💡 Why Did the Model Predict This?'
        '</div>',
        unsafe_allow_html=True
    )


    st.write(
        "The following factors had the strongest influence "
        "on this individual prediction according to the "
        "Logistic Regression model."
    )


    # ------------------------------------------------------
    # GET PIPELINE COMPONENTS
    # ------------------------------------------------------

    preprocessor = model.named_steps[
        "preprocessor"
    ]

    classifier = model.named_steps[
        "classifier"
    ]


    # ------------------------------------------------------
    # TRANSFORM INPUT
    # ------------------------------------------------------

    transformed_input = (
        preprocessor.transform(input_data)
    )


    if hasattr(
        transformed_input,
        "toarray"
    ):

        transformed_input = (
            transformed_input.toarray()
        )


    # ------------------------------------------------------
    # FEATURE NAMES
    # ------------------------------------------------------

    feature_names = (
        preprocessor
        .get_feature_names_out()
    )


    # ------------------------------------------------------
    # CONTRIBUTIONS
    # ------------------------------------------------------

    coefficients = (
        classifier.coef_[0]
    )


    contributions = (
        transformed_input[0]
        * coefficients
    )


    explanation_df = pd.DataFrame({

        "Feature": feature_names,

        "Contribution": contributions

    })


    # ------------------------------------------------------
    # POSITIVE CONTRIBUTIONS
    # ------------------------------------------------------

    positive_features = (
        explanation_df[
            explanation_df["Contribution"] > 0
        ]
        .sort_values(
            "Contribution",
            ascending=False
        )
        .head(5)
    )


    # ------------------------------------------------------
    # NEGATIVE CONTRIBUTIONS
    # ------------------------------------------------------

    negative_features = (
        explanation_df[
            explanation_df["Contribution"] < 0
        ]
        .sort_values(
            "Contribution",
            ascending=True
        )
        .head(5)
    )


    reason_col1, reason_col2 = st.columns(2)


    # ======================================================
    # SUPPORTING FACTORS
    # ======================================================

    with reason_col1:

        st.markdown(
            "### 🟢 Supporting Factors"
        )


        if len(positive_features) == 0:

            st.write(
                "No strong positive factors were identified."
            )

        else:

            for _, row in (
                positive_features.iterrows()
            ):

                st.success(
                    f"**{row['Feature']}**  \n"
                    f"Contribution: "
                    f"+{row['Contribution']:.3f}"
                )


    # ======================================================
    # OPPOSING FACTORS
    # ======================================================

    with reason_col2:

        st.markdown(
            "### 🔴 Opposing Factors"
        )


        if len(negative_features) == 0:

            st.write(
                "No strong negative factors were identified."
            )

        else:

            for _, row in (
                negative_features.iterrows()
            ):

                st.error(
                    f"**{row['Feature']}**  \n"
                    f"Contribution: "
                    f"{row['Contribution']:.3f}"
                )


    # ======================================================
    # COMPLETE APPLICATION DETAILS
    # ======================================================

    with st.expander(
        "🔎 View Complete Application Details"
    ):

        display_data = pd.DataFrame({

            "Feature": [

                "Gender",
                "Age",
                "Education",
                "Annual Income",
                "Employment Experience",
                "Home Ownership",
                "Loan Amount",
                "Loan Intent",
                "Interest Rate",
                "Loan Percentage",
                "Credit History",
                "Credit Score",
                "Previous Loan"

            ],

            "Value": [

                gender,
                age,
                education,
                f"₹{person_income:,.0f}",
                f"{employee_experience} years",
                home_onwership,
                f"₹{loan_amount:,.0f}",
                loan_intent,
                f"{loan_interest_rate:.2f}%",
                f"{loan_percentage:.2f}",
                credit_history,
                credit_score,
                previous_loan

            ]

        })


        st.dataframe(
            display_data,
            use_container_width=True,
            hide_index=True
        )


    # ======================================================
    # DISCLAIMER
    # ======================================================

    st.info(
        "ℹ️ **Note:** This prediction is generated by a "
        "machine learning model based on patterns in the "
        "training data. It should not be treated as a real "
        "financial or lending decision."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    '<div class="footer">'
    '🤖 <b>Loan Approval AI</b>'
    '<br>'
    'Machine Learning • Logistic Regression • Streamlit'
    '<br><br>'
    'Built as a Machine Learning Project'
    '</div>',
    unsafe_allow_html=True
)