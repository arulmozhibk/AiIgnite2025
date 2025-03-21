import streamlit as st
import random
from PIL import Image
from utils import (
    get_activity_recommendations,
    validate_age,
    generate_activity_schedule,
    get_milestones,
    ENVIRONMENT_PHOTOS,
    get_activity_history_summary
)
from styles import apply_custom_styles

# Set page configuration first
st.set_page_config(
    page_title="Baby Activity Recommender",
    page_icon="👶",
    layout="wide"
)

# Apply custom styles
apply_custom_styles()

def display_schedule(schedule, age_months):
    """Display daily or weekly activity schedule with completion tracking"""
    if schedule["type"] == "daily":
        for activity in schedule["activities"]:
            with st.container():
                st.markdown(f"""
                <div class="activity-card">
                    <h3>🌟 {activity['suggested_time']}: {activity['title']}</h3>
                    <p><strong>🎯 Description:</strong> {activity['description']}</p>
                    <p><strong>⏰ Duration:</strong> {activity['duration']}</p>
                    <p><strong>🎨 Materials needed:</strong></p>
                    <ul class="cute-list">
                        {"".join(f"<li>🔸 {item}</li>" for item in activity['materials'])}
                    </ul>
                    <p><strong>✨ Benefits:</strong></p>
                    <ul class="cute-list">
                        {"".join(f"<li>🌈 {item}</li>" for item in activity['benefits'])}
                    </ul>
                    <p><strong>🛡️ Safety Tips:</strong></p>
                    <ul class="cute-list">
                        {"".join(f"<li>✅ {item}</li>" for item in activity['safety_tips'])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    else:  # weekly schedule
        for day, activities in schedule["schedule"].items():
            st.markdown(f"### 📅 {day}")
            for activity in activities:
                with st.container():
                    st.markdown(f"""
                    <div class="activity-card">
                        <h3>🌟 {activity['suggested_time']}: {activity['title']}</h3>
                        <p><strong>🎯 Description:</strong> {activity['description']}</p>
                        <p><strong>⏰ Duration:</strong> {activity['duration']}</p>
                        <p><strong>🎨 Materials needed:</strong></p>
                        <ul class="cute-list">
                            {"".join(f"<li>🔸 {item}</li>" for item in activity['materials'])}
                        </ul>
                        <p><strong>✨ Benefits:</strong></p>
                        <ul class="cute-list">
                            {"".join(f"<li>🌈 {item}</li>" for item in activity['benefits'])}
                        </ul>
                        <p><strong>🛡️ Safety Tips:</strong></p>
                        <ul class="cute-list">
                            {"".join(f"<li>✅ {item}</li>" for item in activity['safety_tips'])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)

def display_activity_history():
    """Display activity history and progress"""
    history_summary = get_activity_history_summary()

    if history_summary:
        st.markdown("""
        <div class="history-header">
            <h2>📚 Activity History</h2>
            <p class="history-subtitle">Track your baby's learning journey!</p>
        </div>
        """, unsafe_allow_html=True)

        # Display stats
        cols = st.columns(3)
        with cols[0]:
            st.metric("Activities Completed", history_summary['total_completed'])
        with cols[1]:
            st.metric("Unique Skills Developed", len(history_summary['unique_skills']))

        # Recent activities
        st.markdown("""
        <div class="recent-activities">
            <h3>🎯 Recently Completed Activities</h3>
        </div>
        """, unsafe_allow_html=True)

        for activity in history_summary['recent_activities']:
            st.markdown(f"""
            <div class="history-card">
                <h4>{activity['activity']['title']}</h4>
                <p><strong>Completed:</strong> {activity['completion_date']}</p>
                <p><strong>Skills:</strong> {', '.join(activity['activity']['benefits'])}</p>
            </div>
            """, unsafe_allow_html=True)


def display_milestones(milestones_data, recommendations):
    """Display milestone tracking information"""
    st.markdown("""
    <div class="milestone-header">
        <h2>🎯 Next Milestones</h2>
        <p class="milestone-subtitle">Here are the exciting developments to look forward to!</p>
    </div>
    """, unsafe_allow_html=True)

    # Display next milestones in columns
    if milestones_data.get("next_milestones"):
        cols = st.columns(3)
        for idx, (category, milestone) in enumerate(milestones_data["next_milestones"].items()):
            with cols[idx]:
                st.markdown(f"""
                <div class="milestone-card">
                    <h3>{category} Development</h3>
                    <p class="next-milestone">{milestone['milestone']}</p>
                    <p class="milestone-age">Typical age: {milestone['typical_age']} months</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No upcoming milestones found for this age group.")

    # Development Tips
    st.markdown("""
    <div class="tips-header">
        <h2>💡 Development Tips</h2>
        <p class="tips-subtitle">Supporting your baby's growth and development</p>
    </div>
    """, unsafe_allow_html=True)

    # Display tips in columns
    if milestones_data.get("development_tips"):
        cols = st.columns(3)
        for idx, (category, tips) in enumerate(milestones_data["development_tips"].items()):
            with cols[idx]:
                tips_html = "".join(f"<li>✨ {tip}</li>" for tip in tips)
                st.markdown(f"""
                <div class="tips-card">
                    <h3>{category} Tips</h3>
                    <ul class="cute-list">
                        {tips_html}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No development tips available for this age group.")

    # Safety Guidelines
    st.markdown("""
    <div class="safety-header">
        <h2>🛡️ General Safety Guidelines</h2>
        <p class="safety-subtitle">Keeping your little one safe while having fun! 💕</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        safety_items = "".join(
            f"<li>💫 {tip}</li>" for tip in recommendations['general_safety_guidelines']
        )
        st.markdown(f"""
        <div class="safety-guidelines">
            <ul class="cute-list">
                {safety_items}
            </ul>
        </div>
        """, unsafe_allow_html=True)

def main():
    # Header with random baby activity photo
    image = Image.open("assets/football.jpeg")  # Replace with actual path

    # Display the image in Streamlit
    st.image(image, use_container_width=True)

    # Cute title and description
    st.markdown("""
    <div class="baby-title">
        <h1>👶 Baby Activity Recommender 🎈</h1>
        <p class="subtitle">🌈 Welcome to your baby's fun learning journey! 🌟</p>
    </div>
    <div class="welcome-message">
        Let's discover exciting, age-appropriate activities that will help your little one grow,
        learn, and have lots of fun! 🎨 🎵 🎮
    </div>
    """, unsafe_allow_html=True)


    # Age input section
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    col1, col2 = st.columns([3.4, 0.6])

    with col1:
        age_months = st.number_input(
            "🎈 How old is your baby? (in months)",
            min_value=0,
            max_value=36,
            value=12,
            step=1,
            help="Enter your baby's age in months (0-36 months)"
        )

    with col2:
        if st.button("✨ Get Activities", type="primary"):
            is_valid, result = validate_age(age_months)

            if not is_valid:
                st.error(result)
            else:
                st.session_state.show_activities = True  # Store state to show the next section

    st.markdown('</div>', unsafe_allow_html=True)

    # 🟢 Row 2: Activity Recommendations (Only show if valid age is entered)
    if st.session_state.get("show_activities", False):
        with st.container():
            with st.expander("🗓️ Want to see a weekly schedule instead?", expanded=False):
                schedule_type = st.radio(
                    "Choose schedule type",
                    ["daily", "weekly"],
                    index=0,
                    horizontal=True,
                    help="Select daily for today's activities or weekly for a full week plan"
                )

            with st.spinner("🌈 Creating magical activities for your baby..."):
                recommendations = get_activity_recommendations(age_months)
                schedule = generate_activity_schedule(age_months, schedule_type)
                milestones_data = get_milestones(age_months)

            if recommendations and schedule and milestones_data:
                display_activity_history()

                # Display schedule with completion tracking
                st.markdown(f"""
                <div class="schedule-header">
                    <h2>🗓️ Your {schedule_type.capitalize()} Activity Schedule</h2>
                    <p class="schedule-subtitle">Fun activities tailored for your {age_months}-month-old! 🎈</p>
                </div>
                """, unsafe_allow_html=True)

                display_schedule(schedule, age_months)

            # Display milestone tracking and safety guidelines
            display_milestones(milestones_data, recommendations)

    # Safe play environment section with cute styling
    st.markdown("""
    <div class="environment-header">
        <h2>🏠 Safe Play Environments</h2>
        <p class="environment-subtitle">Creating perfect spaces for your baby's adventures! 🌈</p>
    </div>
    """, unsafe_allow_html=True)
    cols = st.columns(2)
    for idx, photo_url in enumerate(ENVIRONMENT_PHOTOS):
        with cols[idx % 2]:
            st.image(photo_url, use_container_width=True)

    # Footer with cute styling
    st.markdown("""
    <footer class="baby-footer">
        <br/><p><b>🌟 Remember: Always supervise your baby during activities and consult with your
        pediatrician about age-appropriate activities for your child's specific needs. 💖 <b></p><br/><br/>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()