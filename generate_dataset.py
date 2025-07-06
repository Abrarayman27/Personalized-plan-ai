import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)
n_samples = 10000  # Total samples
n_plans = 7  # Number of plans
samples_per_plan = n_samples // n_plans  # ~1428 samples per plan

# Define plans with 3-4 activities
plans = [
    'Therapist, Meditation, Reading about the illness, Journaling',
    'Therapist, Reading about the illness, Mood tracking, Taking another test',
    'Talking with chatbot, Reading quotes, Meditation, Journaling',
    'Journaling, Mood tracking, Community events, Music',
    'Meditation, Reading quotes, Mood tracking',
    'Music, Community events, Taking another test, Reading quotes',
    'Journaling, Meditation, Music'
]

# Initialize data lists
data = {
    'gad7': [],
    'who5': [],
    'cesdr10': [],
    'loc': [],
    'swls': [],
    'scs': [],
    'recommended_plan': []
}

# Generate balanced samples for each plan
for plan in plans:
    for _ in range(samples_per_plan):
        if plan == 'Therapist, Meditation, Reading about the illness, Journaling':
            gad7 = np.random.randint(15, 22) if np.random.rand() > 0.5 else np.random.randint(0, 22)
            cesdr10 = np.random.randint(20, 31) if np.random.rand() > 0.5 else np.random.randint(0, 31)
            who5 = np.random.randint(0, 101)
        elif plan == 'Therapist, Reading about the illness, Mood tracking, Taking another test':
            gad7 = np.random.randint(0, 15)
            cesdr10 = np.random.randint(15, 20)
            who5 = np.random.randint(0, 101)
        elif plan == 'Talking with chatbot, Reading quotes, Meditation, Journaling':
            gad7 = np.random.randint(10, 15)
            cesdr10 = np.random.randint(0, 15)
            who5 = np.random.randint(0, 101)
        elif plan == 'Journaling, Mood tracking, Community events, Music':
            gad7 = np.random.randint(0, 10)
            cesdr10 = np.random.randint(0, 15)
            who5 = np.random.randint(0, 26)
        elif plan == 'Meditation, Reading quotes, Mood tracking':
            gad7 = np.random.randint(5, 10) if np.random.rand() > 0.5 else np.random.randint(0, 5)
            cesdr10 = np.random.randint(10, 15) if np.random.rand() > 0.5 else np.random.randint(0, 10)
            who5 = np.random.randint(26, 75)
        elif plan == 'Music, Community events, Taking another test, Reading quotes':
            gad7 = np.random.randint(0, 5)
            cesdr10 = np.random.randint(0, 10)
            who5 = np.random.randint(75, 101)
        elif plan == 'Journaling, Meditation, Music':
            gad7 = np.random.randint(0, 5)
            cesdr10 = np.random.randint(0, 10)
            who5 = np.random.randint(26, 75)

        # Generate other features
        loc = np.random.randint(0, 25)
        swls = np.random.randint(5, 36)
        scs = np.random.randint(12, 61)

        # Append to data
        data['gad7'].append(gad7)
        data['who5'].append(who5)
        data['cesdr10'].append(cesdr10)
        data['loc'].append(loc)
        data['swls'].append(swls)
        data['scs'].append(scs)
        data['recommended_plan'].append(plan)

# Handle remaining samples to reach n_samples
remaining = n_samples - len(data['gad7'])
for _ in range(remaining):
    gad7 = np.random.randint(0, 22)
    who5 = np.random.randint(0, 101)
    cesdr10 = np.random.randint(0, 31)
    loc = np.random.randint(0, 25)
    swls = np.random.randint(5, 36)
    scs = np.random.randint(12, 61)

    # Assign plan based on rules
    if gad7 >= 15 or cesdr10 >= 20:
        plan = 'Therapist, Meditation, Reading about the illness, Journaling'
    elif cesdr10 >= 15:
        plan = 'Therapist, Reading about the illness, Mood tracking, Taking another test'
    elif gad7 >= 10:
        plan = 'Talking with chatbot, Reading quotes, Meditation, Journaling'
    elif who5 <= 25:
        plan = 'Journaling, Mood tracking, Community events, Music'
    elif gad7 >= 5 or cesdr10 >= 10:
        plan = 'Meditation, Reading quotes, Mood tracking'
    elif who5 >= 75:
        plan = 'Music, Community events, Taking another test, Reading quotes'
    else:
        plan = 'Journaling, Meditation, Music'

    data['gad7'].append(gad7)
    data['who5'].append(who5)
    data['cesdr10'].append(cesdr10)
    data['loc'].append(loc)
    data['swls'].append(swls)
    data['scs'].append(scs)
    data['recommended_plan'].append(plan)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = 'wellbeing_data.csv'
df.to_csv(output_file, index=False)

# Print summary
print(f"Dataset generated with {n_samples} samples and saved as {output_file}")
print("\nColumn names:", df.columns.tolist())
print("\nRecommended plan distribution:")
print(df['recommended_plan'].value_counts())
print("\nData preview:")
print(df.head())