import json
import os
import random
import streamlit as st
from datetime import datetime, timedelta

# Adding milestone data structure
MILESTONES_BY_AGE = {
    "0-3": {
        "Physical": [
            {"milestone": "Raises head and chest when lying on stomach", "typical_age": 2},
            {"milestone": "Stretches legs out and kicks when lying on back", "typical_age": 2},
            {"milestone": "Opens and shuts hands", "typical_age": 2},
            {"milestone": "Pushes down on legs when feet are on a hard surface", "typical_age": 3}
        ],
        "Social": [
            {"milestone": "Begins to smile at people", "typical_age": 2},
            {"milestone": "Tries to look at parent", "typical_age": 2},
            {"milestone": "Coos, makes gurgling sounds", "typical_age": 2},
            {"milestone": "Turns head toward sounds", "typical_age": 2}
        ],
        "Cognitive": [
            {"milestone": "Pays attention to faces", "typical_age": 2},
            {"milestone": "Begins to follow things with eyes", "typical_age": 2},
            {"milestone": "Recognizes familiar people at a distance", "typical_age": 3},
            {"milestone": "Shows boredom (cries, fussy) if activity doesn't change", "typical_age": 3}
        ]
    },
    "4-6": {
        "Physical": [
            {"milestone": "Holds head steady, unsupported", "typical_age": 4},
            {"milestone": "Pushes down on legs when feet are on a hard surface", "typical_age": 4},
            {"milestone": "May be able to roll over both ways", "typical_age": 6},
            {"milestone": "Brings hands to mouth", "typical_age": 4}
        ],
        "Social": [
            {"milestone": "Smiles spontaneously at people", "typical_age": 4},
            {"milestone": "Likes to play with people", "typical_age": 4},
            {"milestone": "Copies some movements and facial expressions", "typical_age": 6}
        ],
        "Cognitive": [
            {"milestone": "Lets you know if they are happy or sad", "typical_age": 5},
            {"milestone": "Responds to affection", "typical_age": 4},
            {"milestone": "Reaches for toy with one hand", "typical_age": 5},
            {"milestone": "Uses hands and eyes together", "typical_age": 4}
        ]
    },
    "7-12": {
        "Physical": [
            {"milestone": "Stands holding on", "typical_age": 7},
            {"milestone": "Can get into sitting position", "typical_age": 8},
            {"milestone": "Crawls forward on belly", "typical_age": 9},
            {"milestone": "Pulls to stand", "typical_age": 11}
        ],
        "Social": [
            {"milestone": "May be afraid of strangers", "typical_age": 8},
            {"milestone": "May be clingy with familiar adults", "typical_age": 8},
            {"milestone": "Has favorite toys", "typical_age": 10}
        ],
        "Cognitive": [
            {"milestone": "Understands 'no'", "typical_age": 7},
            {"milestone": "Makes a lot of different sounds", "typical_age": 8},
            {"milestone": "Copies sounds and gestures", "typical_age": 9},
            {"milestone": "Finds hidden things easily", "typical_age": 10}
        ]
    },
    "13-24": {
        "Physical": [
            {"milestone": "Walks alone", "typical_age": 13},
            {"milestone": "May walk up steps and run", "typical_age": 18},
            {"milestone": "Pulls toys while walking", "typical_age": 15},
            {"milestone": "Begins to sort shapes and colors", "typical_age": 20}
        ],
        "Social": [
            {"milestone": "Shows affection to familiar people", "typical_age": 14},
            {"milestone": "Plays simple pretend", "typical_age": 18},
            {"milestone": "May have temper tantrums", "typical_age": 16},
            {"milestone": "Shows increasing independence", "typical_age": 22}
        ],
        "Cognitive": [
            {"milestone": "Says several single words", "typical_age": 15},
            {"milestone": "Follows simple instructions", "typical_age": 18},
            {"milestone": "Begins to use objects correctly", "typical_age": 20},
            {"milestone": "Points to things when named", "typical_age": 16}
        ]
    },
    "25-36": {
        "Physical": [
            {"milestone": "Climbs well", "typical_age": 26},
            {"milestone": "Runs easily", "typical_age": 28},
            {"milestone": "Pedals a tricycle", "typical_age": 32},
            {"milestone": "Walks up and down stairs", "typical_age": 30}
        ],
        "Social": [
            {"milestone": "Copies adults and friends", "typical_age": 28},
            {"milestone": "Shows a wide range of emotions", "typical_age": 30},
            {"milestone": "Takes turns in games", "typical_age": 32},
            {"milestone": "Shows concern for crying friend", "typical_age": 34}
        ],
        "Cognitive": [
            {"milestone": "Can name most familiar things", "typical_age": 26},
            {"milestone": "Understands words like 'in,' 'on,' and 'under'", "typical_age": 30},
            {"milestone": "Says words like 'I,' 'me,' 'we,' and 'you'", "typical_age": 32},
            {"milestone": "Plays make-believe with dolls, animals, and people", "typical_age": 34}
        ]
    }
}

# Predefined age-appropriate activities
ACTIVITIES_BY_AGE = {
    "0-3": [
        {
            "title": "Tummy Time Fun",
            "description": "Place baby on their tummy to strengthen neck and shoulder muscles",
            "duration": "5-10 minutes",
            "materials": ["Soft blanket", "Small toys"],
            "benefits": ["Neck strength", "Motor development", "Visual tracking"],
            "safety_tips": ["Never leave baby unattended", "Stop if baby becomes upset"]
        },
        {
            "title": "Mirror Play",
            "description": "Show baby their reflection in a baby-safe mirror",
            "duration": "5-15 minutes",
            "materials": ["Unbreakable mirror"],
            "benefits": ["Self-recognition", "Visual development", "Social skills"],
            "safety_tips": ["Use only unbreakable mirrors", "Keep clean and sanitized"]
        },
        {
            "title": "Soft Toy Tracking",
            "description": "Move colorful toys slowly from side to side for baby to follow",
            "duration": "3-5 minutes",
            "materials": ["Colorful soft toys"],
            "benefits": ["Visual tracking", "Attention span", "Neck control"],
            "safety_tips": ["Keep toys at a comfortable distance", "Take breaks if baby loses interest"]
        }
    ],
    "4-6": [
        {
            "title": "Reach and Grab",
            "description": "Dangle safe toys within reaching distance for baby to grasp",
            "duration": "10-15 minutes",
            "materials": ["Baby-safe toys", "Play mat"],
            "benefits": ["Hand-eye coordination", "Grasping skills", "Motor planning"],
            "safety_tips": ["Use lightweight toys", "Ensure toys are age-appropriate"]
        },
        {
            "title": "Musical Movements",
            "description": "Play gentle music and help baby move their arms and legs to the rhythm",
            "duration": "5-10 minutes",
            "materials": ["Baby music", "Soft mat"],
            "benefits": ["Rhythm awareness", "Motor development", "Sensory processing"],
            "safety_tips": ["Keep volume moderate", "Follow baby's cues"]
        },
        {
            "title": "Rolling Games",
            "description": "Encourage rolling by placing toys slightly out of reach",
            "duration": "10-15 minutes",
            "materials": ["Favorite toys", "Soft blanket"],
            "benefits": ["Gross motor skills", "Spatial awareness", "Core strength"],
            "safety_tips": ["Use a soft surface", "Support head and neck"]
        }
    ],
    "7-12": [
        {
            "title": "Peek-a-Boo",
            "description": "Play peek-a-boo using hands or soft cloths",
            "duration": "5-10 minutes",
            "materials": ["Small blanket or cloth"],
            "benefits": ["Object permanence", "Social interaction", "Emotional development"],
            "safety_tips": ["Use breathable fabrics", "Watch for signs of overstimulation"]
        },
        {
            "title": "Crawling Adventure",
            "description": "Create a safe obstacle course for crawling exploration",
            "duration": "15-20 minutes",
            "materials": ["Cushions", "Tunnels", "Toys"],
            "benefits": ["Gross motor skills", "Problem solving", "Spatial awareness"],
            "safety_tips": ["Pad hard surfaces", "Remove sharp objects", "Supervise constantly"]
        },
        {
            "title": "Container Play",
            "description": "Practice putting objects in and out of containers",
            "duration": "10-15 minutes",
            "materials": ["Large container", "Safe objects to place inside"],
            "benefits": ["Fine motor skills", "Understanding spatial relationships", "Cause and effect"],
            "safety_tips": ["Use items larger than mouth", "Check for sharp edges"]
        }
    ],
    "13-24": [
        {
            "title": "Block Building",
            "description": "Stack and knock down soft blocks",
            "duration": "15-20 minutes",
            "materials": ["Soft blocks", "Clear space"],
            "benefits": ["Fine motor skills", "Problem solving", "Spatial awareness"],
            "safety_tips": ["Use age-appropriate blocks", "Play on a soft surface"]
        },
        {
            "title": "Simple Puzzles",
            "description": "Introduce basic shape-sorting toys and simple puzzles",
            "duration": "10-15 minutes",
            "materials": ["Shape sorter", "Simple puzzles"],
            "benefits": ["Problem solving", "Shape recognition", "Hand-eye coordination"],
            "safety_tips": ["Check for loose pieces", "Supervise puzzle time"]
        },
        {
            "title": "Action Songs",
            "description": "Sing songs with actions like 'Head, Shoulders, Knees and Toes'",
            "duration": "10-15 minutes",
            "materials": ["None needed"],
            "benefits": ["Language development", "Body awareness", "Memory skills"],
            "safety_tips": ["Keep movements gentle", "Ensure adequate space"]
        }
    ],
    "25-36": [
        {
            "title": "Art Exploration",
            "description": "Finger painting or coloring with chunky crayons",
            "duration": "20-30 minutes",
            "materials": ["Finger paint", "Large paper", "Chunky crayons"],
            "benefits": ["Creativity", "Fine motor skills", "Color recognition"],
            "safety_tips": ["Use non-toxic materials", "Supervise art time", "Wear old clothes"]
        },
        {
            "title": "Active Stories",
            "description": "Read stories and act out different characters",
            "duration": "15-20 minutes",
            "materials": ["Picture books", "Props (optional)"],
            "benefits": ["Language skills", "Imagination", "Social-emotional development"],
            "safety_tips": ["Use durable board books", "Keep props age-appropriate"]
        },
        {
            "title": "Ball Play",
            "description": "Roll, throw, and kick soft balls",
            "duration": "20-30 minutes",
            "materials": ["Soft balls of different sizes"],
            "benefits": ["Gross motor skills", "Hand-eye coordination", "Social interaction"],
            "safety_tips": ["Use lightweight balls", "Clear the play area", "Play on level ground"]
        }
    ]
}

def get_milestones(age_months):
    """Get age-appropriate milestones and track progress"""
    age_group = get_age_group(age_months)
    milestones = MILESTONES_BY_AGE[age_group]

    upcoming_milestones = {
        category: [
            milestone for milestone in milestones[category]
            if milestone["typical_age"] >= age_months
        ]
        for category in milestones
    }

    achieved_milestones = {
        category: [
            milestone for milestone in milestones[category]
            if milestone["typical_age"] < age_months
        ]
        for category in milestones
    }

    return {
        "upcoming": upcoming_milestones,
        "achieved": achieved_milestones,
        "next_milestones": get_next_milestones(age_months, upcoming_milestones),
        "development_tips": get_development_tips(age_months, upcoming_milestones)
    }

def get_next_milestones(age_months, upcoming_milestones):
    """Get the next immediate milestones for each category"""
    next_milestones = {}
    for category, milestones in upcoming_milestones.items():
        if milestones:
            # Sort by typical age and get the closest upcoming milestone
            sorted_milestones = sorted(milestones, key=lambda x: x["typical_age"])
            if sorted_milestones:  # Add check for empty list
                next_milestones[category] = sorted_milestones[0]

    # Ensure we have all three categories represented
    for category in ["Physical", "Social", "Cognitive"]:
        if category not in next_milestones:
            next_milestones[category] = {
                "milestone": "All milestones achieved for this category!",
                "typical_age": age_months
            }

    return next_milestones

def get_development_tips(age_months, upcoming_milestones):
    """Generate development tips based on upcoming milestones"""
    tips = {
        "Physical": [
            "Create a safe space for movement exploration",
            "Provide age-appropriate toys that encourage reaching and grasping",
            "Support tummy time and crawling activities",
            "Encourage physical play with supervision"
        ],
        "Social": [
            "Engage in face-to-face interactions",
            "Play simple games like peek-a-boo",
            "Respond positively to their attempts at communication",
            "Create opportunities for safe social interactions"
        ],
        "Cognitive": [
            "Read books together daily",
            "Sing songs and play with rhymes",
            "Provide toys with different colors and textures",
            "Name objects and describe activities during daily routines"
        ]
    }

    relevant_tips = {}
    # Ensure we always have tips for all three categories
    for category in ["Physical", "Social", "Cognitive"]:
        # Always provide at least 2 tips per category
        relevant_tips[category] = random.sample(tips[category], 2)

    return relevant_tips

ENVIRONMENT_PHOTOS = [
    "https://images.unsplash.com/photo-1526992430293-51554a151122",
    "https://images.unsplash.com/photo-1472586662442-3eec04b9dbda"
]

def get_age_group(age_months):
    """Determine the appropriate age group for activities"""
    if age_months <= 3:
        return "0-3"
    elif age_months <= 6:
        return "4-6"
    elif age_months <= 12:
        return "7-12"
    elif age_months <= 24:
        return "13-24"
    else:
        return "25-36"

def initialize_activity_history():
    """Initialize activity history in session state if not present"""
    if 'activity_history' not in st.session_state:
        st.session_state.activity_history = {
            'completed_activities': [],
            'favorite_activities': [],
            'last_completed_date': {}
        }

def mark_activity_completed(activity, age_months):
    """Mark an activity as completed and update history"""
    initialize_activity_history()

    activity_id = f"{activity['title']}_{age_months}"
    completion_data = {
        'activity': activity,
        'age_months': age_months,
        'completion_date': datetime.now().strftime('%Y-%m-%d'),
        'activity_id': activity_id
    }

    # Add to completed activities if not already present
    if activity_id not in [a['activity_id'] for a in st.session_state.activity_history['completed_activities']]:
        st.session_state.activity_history['completed_activities'].append(completion_data)

    # Update last completed date
    st.session_state.activity_history['last_completed_date'][activity_id] = datetime.now().strftime('%Y-%m-%d')

def get_activity_recommendations(age_months):
    """Get age-appropriate activities based on the baby's age and history"""
    initialize_activity_history()
    age_group = get_age_group(age_months)
    all_activities = ACTIVITIES_BY_AGE[age_group]

    # Get completed activities for filtering
    completed_ids = [a['activity_id'] for a in st.session_state.activity_history['completed_activities']]

    # Filter out recently completed activities
    available_activities = [
        activity for activity in all_activities
        if f"{activity['title']}_{age_months}" not in completed_ids
    ]

    # If all activities completed, reset the list
    if not available_activities:
        available_activities = all_activities

    # Prioritize activities that complement completed ones
    if st.session_state.activity_history['completed_activities']:
        # Get skills from completed activities
        completed_benefits = []
        for completed in st.session_state.activity_history['completed_activities']:
            completed_benefits.extend(completed['activity']['benefits'])

        # Sort activities to balance different skills
        available_activities.sort(key=lambda x: 
            len(set(x['benefits']).difference(completed_benefits)), 
            reverse=True
        )

    return {
        "activities": available_activities[:3],  # Return top 3 recommended activities
        "general_safety_guidelines": [
            "Always supervise your baby during activities",
            "Stop any activity if baby shows signs of distress or fatigue",
            "Ensure play area is clean and free of hazards",
            "Check all toys and materials for damage before use",
            "Keep emergency contact numbers handy",
            "Follow age recommendations for all toys and activities"
        ]
    }

def get_activity_history_summary():
    """Get a summary of completed activities and progress"""
    initialize_activity_history()
    history = st.session_state.activity_history

    if not history['completed_activities']:
        return None

    return {
        'total_completed': len(history['completed_activities']),
        'recent_activities': sorted(
            history['completed_activities'],
            key=lambda x: x['completion_date'],
            reverse=True
        )[:5],
        'unique_skills': list(set(
            benefit
            for activity in history['completed_activities']
            for benefit in activity['activity']['benefits']
        ))
    }

def validate_age(age):
    """Validate the input age in months"""
    try:
        age = int(age)
        if age < 0 or age > 36:
            return False, "Please enter an age between 0 and 36 months"
        return True, age
    except ValueError:
        return False, "Please enter a valid number"

def generate_activity_schedule(age_months, schedule_type="daily"):
    """Generate a daily or weekly activity schedule"""
    age_group = get_age_group(age_months)
    activities = ACTIVITIES_BY_AGE[age_group]

    if schedule_type == "daily":
        # Generate 3 activities for the day
        daily_schedule = random.sample(activities, min(3, len(activities)))
        return {
            "type": "daily",
            "activities": [
                {
                    **activity,
                    "suggested_time": "Morning" if i == 0 else "Afternoon" if i == 1 else "Evening"
                }
                for i, activity in enumerate(daily_schedule)
            ]
        }
    else:  # weekly
        # Generate activities for each day of the week
        week_schedule = {}
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in days:
            # Pick 2-3 activities for each day
            num_activities = random.randint(2, 3)
            daily_activities = random.sample(activities, min(num_activities, len(activities)))
            week_schedule[day] = [
                {
                    **activity,
                    "suggested_time": "Morning" if i == 0 else "Afternoon" if i == 1 else "Evening"
                }
                for i, activity in enumerate(daily_activities)
            ]

        return {
            "type": "weekly",
            "schedule": week_schedule
        }