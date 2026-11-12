
import streamlit as st

from job_application import JobApplication
from application_manager import ApplicationManager


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Job Application Tracker",
    page_icon="💼",
    layout="wide"
)


# --------------------------------
# CUSTOM DARK THEME CSS
# --------------------------------

st.markdown("""
<style>

    /* Hide Streamlit top header */
    [data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    /* Main background */
    .stApp {
        background-color: #183642;
        color: #EAEAEA;
    }

    /* Main content spacing */
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
    }

    /* Headings */
    h1, h2, h3 {
        color: #EAEAEA !important;
        font-weight: 700;
    }

    /* Normal text */
    p, label {
        color: #CBC5EA;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #313D5A;
        border-right: 1px solid #73628A;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #EAEAEA !important;
    }

    /* Sidebar navigation buttons */
    [data-testid="stSidebar"] .stButton button {
        width: 100%;
        text-align: left;
        padding: 14px 16px;
        border-radius: 12px;
        font-size: 15px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    /* Active navigation button */
    [data-testid="stSidebar"] .stButton button[kind="primary"] {
        background-color: #73628A;
        color: #FFFFFF !important;
        border: 1px solid #CBC5EA;
    }

    /* Inactive navigation buttons */
    [data-testid="stSidebar"] .stButton button[kind="secondary"] {
        background-color: transparent;
        color: #EAEAEA !important;
        border: 1px solid transparent;
    }

    /* Navigation hover effect */
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #73628A;
        color: #FFFFFF !important;
        border: 1px solid #CBC5EA;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #313D5A;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #73628A;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    }

    [data-testid="stMetricLabel"] {
        color: #CBC5EA !important;
    }

    [data-testid="stMetricValue"] {
        color: #EAEAEA !important;
        font-weight: 700;
    }

    /* All buttons - normal state */
    .stButton > button {
        background-color: #73628A;
        color: #FFFFFF !important;
        border-radius: 10px;
        border: 1px solid #73628A;
        padding: 0.55rem 1.2rem;
        font-weight: 600;
    }

    /* Ensure button text stays visible */
    .stButton > button,
    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #FFFFFF !important;
    }

    /* Button hover */
    .stButton > button:hover {
        background-color: #CBC5EA !important;
        border-color: #CBC5EA !important;
        color: #183642 !important;
    }

    /* Hovered button text */
    .stButton > button:hover p,
    .stButton > button:hover span,
    .stButton > button:hover div {
        color: #183642 !important;
    }

    /* Input fields */
    .stTextInput input,
    .stNumberInput input,
    .stDateInput input {
        background-color: #313D5A !important;
        color: #EAEAEA !important;
        border: 1px solid #73628A !important;
        border-radius: 9px;
    }

    /* Select boxes */
    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #313D5A;
        border-color: #73628A;
        color: #EAEAEA;
    }

    /* Information and warning messages */
    [data-testid="stAlert"] {
        background-color: #313D5A !important;
        border: 1px solid #73628A !important;
        border-radius: 12px;
    }

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span {
        color: #EAEAEA !important;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border: 1px solid #73628A;
        border-radius: 12px;
    }

    /* Dividers */
    hr {
        border-color: #73628A;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------
# SESSION STATE
# --------------------------------

if "manager" not in st.session_state:
    st.session_state.manager = ApplicationManager()

if "current_page" not in st.session_state:
    st.session_state.current_page = "Overview"


# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------

st.sidebar.title("💼 JobTrack")
st.sidebar.caption("YOUR CAREER COMPANION")

st.sidebar.divider()

st.sidebar.markdown("### Navigation")


# Overview button
if st.sidebar.button(
    "🏠   Overview",
    use_container_width=True,
    type="primary" if st.session_state.current_page == "Overview" else "secondary"
):
    st.session_state.current_page = "Overview"
    st.rerun()


# Add Application button
if st.sidebar.button(
    "➕   Add Application",
    use_container_width=True,
    type="primary" if st.session_state.current_page == "Add Application" else "secondary"
):
    st.session_state.current_page = "Add Application"
    st.rerun()


# My Applications button
if st.sidebar.button(
    "💼   My Applications",
    use_container_width=True,
    type="primary" if st.session_state.current_page == "My Applications" else "secondary"
):
    st.session_state.current_page = "My Applications"
    st.rerun()


page = st.session_state.current_page


# --------------------------------
# OVERVIEW PAGE
# --------------------------------

if page == "Overview":

    # Welcome banner

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #313D5A, #73628A);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 25px;
        border: 1px solid #73628A;
    ">
        <h1 style="color: #EAEAEA !important; margin: 0;">
            Welcome to JobTrack! 👋
        </h1>
        <p style="color: #CBC5EA; font-size: 16px; margin-top: 10px;">
            Your career journey, organised in one place.
            Keep applying, keep growing!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    applications = st.session_state.manager.applications

    # Calculate dashboard statistics

    total_applications = len(applications)

    interviews = sum(
        1 for app in applications
        if app.status.lower() == "interview"
    )

    selected = sum(
        1 for app in applications
        if app.status.lower() == "selected"
    )

    rejected = sum(
        1 for app in applications
        if app.status.lower() == "rejected"
    )

    # Display metric cards

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Applications", total_applications)

    with col2:
        st.metric("Interviews", interviews)

    with col3:
        st.metric("Selected", selected)

    with col4:
        st.metric("Rejected", rejected)

    # Application status chart

    st.divider()
    st.subheader("Application Status Breakdown")

    status_counts = {
        "Applied": 0,
        "Interview": 0,
        "Selected": 0,
        "Rejected": 0
    }

    for app in applications:

        status = app.status.strip().title()

        if status in status_counts:
            status_counts[status] += 1

    if total_applications == 0:

        st.info("Add applications to see your status breakdown.")

    else:

        st.write("Here's how your applications are distributed.")

        st.bar_chart(status_counts)

    # Recent applications

    st.divider()
    st.subheader("Recent Applications")

    if applications:

        recent_applications = applications[-5:][::-1]

        recent_data = []

        for app in recent_applications:

            recent_data.append({
                "Company": app.company,
                "Position": app.position,
                "Location": app.location,
                "Date": app.app_date,
                "Status": app.status
            })

        st.dataframe(
            recent_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("Your recent applications will appear here.")


# --------------------------------
# ADD APPLICATION PAGE
# --------------------------------

elif page == "Add Application":

    st.title("Add a New Application")
    st.write("Enter the details of the job you applied for.")

    # Display success message

    if st.session_state.get("application_added", False):

        st.success("Application added successfully!")

        st.session_state.application_added = False

    # Application form

    with st.form("application_form"):

        app_id = st.number_input(
            "Application ID",
            min_value=1,
            step=1
        )

        company = st.text_input("Company Name")
        position = st.text_input("Job Position")
        location = st.text_input("Location")
        app_date = st.date_input("Application Date")

        submitted = st.form_submit_button("Add Application")

    # Process submitted application

    if submitted:

        applications = st.session_state.manager.applications

        duplicate = any(
            app.app_id == int(app_id)
            for app in applications
        )

        if duplicate:

            st.error("This Application ID already exists!")

        elif not company.strip() or not position.strip() or not location.strip():

            st.warning("Please fill in all the fields.")

        else:

            application = JobApplication(
                int(app_id),
                company.strip(),
                position.strip(),
                location.strip(),
                str(app_date)
            )

            st.session_state.manager.add_application(application)

            st.session_state.application_added = True

            st.rerun()


# --------------------------------
# MY APPLICATIONS PAGE
# --------------------------------

elif page == "My Applications":

    st.title("My Applications")
    st.write("View and manage all your job applications.")

    applications = st.session_state.manager.applications

    if not applications:

        st.info("No applications added yet.")

    else:

        # Update Application Status

        st.subheader("Update Application Status")

        selected_id = st.selectbox(
            "Select Application",
            [app.app_id for app in applications],
            format_func=lambda app_id: next(
                f"{app.company} (ID: {app.app_id})"
                for app in applications
                if app.app_id == app_id
            )
        )

        new_status = st.selectbox(
            "Choose New Status",
            ["Applied", "Interview", "Selected", "Rejected"]
        )

        if st.button("Update Status"):

            st.session_state.manager.update_application_status(
                selected_id,
                new_status
            )

            st.success("Application status updated!")

        # Delete Application

        st.divider()
        st.subheader("Delete Application")

        delete_id = st.selectbox(
            "Select application to delete",
            [app.app_id for app in applications],
            format_func=lambda app_id: next(
                f"{app.company} (ID: {app.app_id})"
                for app in applications
                if app.app_id == app_id
            ),
            key="delete_id"
        )

        if st.button("Delete Application"):

            st.session_state.manager.delete_application(delete_id)

            st.success("Application deleted successfully!")

        # Search and Filter

        st.divider()
        st.subheader("All Applications")

        search_company = st.text_input("Search by company name")

        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Applied", "Interview", "Selected", "Rejected"]
        )

        # Apply search and status filters

        filtered_applications = []

        for app in applications:

            matches_company = (
                search_company.lower() in app.company.lower()
            )

            matches_status = (
                status_filter == "All"
                or app.status.lower() == status_filter.lower()
            )

            if matches_company and matches_status:

                filtered_applications.append(app)

        # Display application table

        application_data = []

        for app in filtered_applications:

            application_data.append({
                "ID": app.app_id,
                "Company": app.company,
                "Position": app.position,
                "Location": app.location,
                "Application Date": app.app_date,
                "Status": app.status
            })

        if filtered_applications:

            st.dataframe(
                application_data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning("No matching applications found.")
