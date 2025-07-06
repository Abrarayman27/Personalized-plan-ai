import pandas as pd
df = pd.read_csv('wellbeing_data.csv')
mismatches = []
for _, row in df.iterrows():
        gad7, who5, cesdr10, plan = row['gad7'], row['who5'], row['cesdr10'], row['recommended_plan']
        expected = (
            'Therapist, Meditation, Reading about the illness, Journaling' if gad7 >= 15 or cesdr10 >= 20 else
            'Therapist, Reading about the illness, Mood tracking, Taking another test' if cesdr10 >= 15 else
            'Talking with chatbot, Reading quotes, Meditation, Journaling' if gad7 >= 10 else
            'Journaling, Mood tracking, Community events, Music' if who5 <= 25 else
            'Meditation, Reading quotes, Mood tracking' if gad7 >= 5 or cesdr10 >= 10 else
            'Music, Community events, Taking another test, Reading quotes' if who5 >= 75 else
            'Journaling, Meditation, Music'
        )
        if plan != expected:
            mismatches.append(f"gad7={gad7}, who5={who5}, cesdr10={cesdr10}, Plan={plan}, Expected={expected}")
print(f"Mismatches found: {len(mismatches)}")
if mismatches:
        print("\nFirst 5 mismatches:")
        print("\n".join(mismatches[:5]))