import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container styles */
        .stApp {
            font-family: 'Comic Sans MS', 'Helvetica Neue', sans-serif;
            background: linear-gradient(135deg, #B3D9FF 0%, #E2F0CB 100%);
        }

        .styled-button {
        margin-top: 27px;
        }

        /* Baby title styles */
        .baby-title {
            text-align: center;
            padding: 0.5rem 0;
            animation: rainbow 8s infinite;
        }

        .baby-title h1 {
            font-size: 3rem;
            color: #FF9AA2;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
        }

        .subtitle {
            font-size: 1.5rem;
            color: #355070;
            margin-bottom: 2rem;
        }

        /* Welcome message */
        .welcome-message {
            text-align: center;
            font-size: 1.2rem;
            color: #355070;
            margin: 2rem 0;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Enhanced Card styles */
        .activity-card {
            background: linear-gradient(145deg, #ffffff, #f5f5f5);
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1.5rem 0;
            border: 2px solid rgba(255, 154, 162, 0.1);
            transition: transform 0.3s ease;
        }

        .activity-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        }

        .activity-card h3 {
            color: #355070;
            font-size: 1.4rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid rgba(255, 154, 162, 0.2);
            padding-bottom: 0.5rem;
        }

        /* Enhanced List styles */
        .cute-list {
            list-style: none;
            padding-left: 0;
            margin: 1rem 0;
        }

        .cute-list li {
            margin: 0.8rem 0;
            padding: 0.5rem 1rem 0.5rem 2.5rem;
            position: relative;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            transition: all 0.3s ease;
        }

        .cute-list li:hover {
            background: rgba(255, 255, 255, 0.8);
            transform: translateX(5px);
        }

        .cute-list li:before {
            content: "•";
            position: absolute;
            left: 1rem;
            color: #FF9AA2;
            font-size: 1.2rem;
        }

        /* Milestone Cards */
        .milestone-card {
            background: linear-gradient(145deg, #ffffff, #f5f5f5);
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            height: 100%;
            border: 2px solid rgba(255, 154, 162, 0.1);
        }

        .milestone-card h3 {
            color: #FF9AA2;
            font-size: 1.2rem;
            margin-bottom: 1rem;
            text-align: center;
        }

        .next-milestone {
            font-size: 1.1rem;
            color: #355070;
            margin: 1rem 0;
            padding: 0.8rem;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 10px;
            text-align: center;
        }

        .milestone-age {
            font-size: 0.9rem;
            color: #666;
            font-style: italic;
            text-align: center;
            margin-top: 0.5rem;
        }

        /* Tips Cards */
        .tips-card {
            background: linear-gradient(145deg, #E2F0CB, #f9fdf2);
            padding: 1.5rem;
            border-radius: 20px;
            height: 100%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            border-left: 4px solid #FF9AA2;
        }

        .tips-card h3 {
            color: #355070;
            font-size: 1.2rem;
            margin-bottom: 1rem;
            text-align: center;
        }

        /* Safety Guidelines */
        .safety-guidelines {
            background: linear-gradient(to right, #E2F0CB, #f9fdf2);
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
            border-left: 4px solid #FF9AA2;
        }

        .safety-guidelines .cute-list li {
            background: rgba(255, 255, 255, 0.7);
            margin: 1rem 0;
        }

        /* Section Headers */
        .milestone-header, .tips-header, .schedule-header, .safety-header {
            text-align: center;
            margin: 3rem 0 2rem 0;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 15px;
        }

        .milestone-header h2, .tips-header h2, .schedule-header h2, .safety-header h2 {
            color: #355070;
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .milestone-subtitle, .tips-subtitle, .schedule-subtitle, .safety-subtitle {
            color: #666;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        /* Animations */
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @keyframes rainbow {
            0% { color: #FF9AA2; }
            25% { color: #FFB7B2; }
            50% { color: #FFDAC1; }
            75% { color: #E2F0CB; }
            100% { color: #FF9AA2; }
        }

        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            .baby-title h1 {
                font-size: 2rem;
            }

            .subtitle {
                font-size: 1.2rem;
            }

            .activity-card {
                padding: 1rem;
            }

            .milestone-card, .tips-card {
                margin: 0.5rem 0;
            }

            .safety-guidelines {
                padding: 1rem;
            }
        }
        /* Activity History Cards */
        .history-header {
            text-align: center;
            margin: 3rem 0 2rem 0;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 15px;
        }

        .history-subtitle {
            color: #666;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        .history-card {
            background: linear-gradient(145deg, #ffffff, #f5f5f5);
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-left: 4px solid #FF9AA2;
            transition: transform 0.3s ease;
        }

        .history-card:hover {
            transform: translateX(5px);
        }

        .history-card h4 {
            color: #355070;
            margin-bottom: 0.5rem;
        }

        .recent-activities {
            margin: 2rem 0;
        }

        .recent-activities h3 {
            color: #355070;
            text-align: center;
            margin-bottom: 1rem;
        }

        /* Complete Button Styles */
        .stButton button {
            background-color: #E2F0CB;
            color: #355070;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;

            margin-top:27px;
        }

        .stButton button:hover {
            background-color: #FF9AA2;
            color: white;
            transform: translateY(-2px);
        }

        .stAppHeader {
            display: none;
        }

        .stMainBlockContainer {
            padding: 0rem 5rem;
        }

        .st-emotion-cache-x496jl {
            background-color: rgb(226, 240, 203);
        }
        </style>
    """, unsafe_allow_html=True)