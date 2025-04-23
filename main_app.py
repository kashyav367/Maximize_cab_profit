# main_app.py

import streamlit as st
from preprocess import load_and_preprocess_data
from env_cab_rl import CabEnvRL
from agent_dqn import DQNAgent
from utils_map import draw_route, st_folium

st.set_page_config(layout="wide")
st.title("🚖 Maximize Cab Driver Profit using Deep Q-Learning (Real Cab Data)")

# Upload CSV
csv_file = st.file_uploader("Upload Cab Ride CSV", type="csv")
if csv_file:
    features, rewards, encoders, df = load_and_preprocess_data(csv_file)

    env = CabEnvRL(features, rewards)
    agent = DQNAgent(state_size=features.shape[1], action_size=2)

    if st.button("🚀 Train Model"):
        rewards_over_episodes = []
        for episode in range(100):
            total_reward = 0
            for _ in range(50):
                state = env.reset()
                action = agent.act(state)
                next_state, reward, done, _ = env.step(action)
                agent.remember(state, action, reward, next_state, done)
                total_reward += reward
                agent.replay(32)
            rewards_over_episodes.append(total_reward)
            st.write(f"Episode {episode+1}: Total Reward = {total_reward}")

        st.line_chart(rewards_over_episodes)

    st.subheader("🗺️ Ride Path Map")
    index = st.slider("Select a Ride Index", 0, len(df) - 1, 0)
    row = df.iloc[index]
    folium_map = draw_route(row['source'], row['destination'], encoders)
    st_data = st_folium(folium_map, width=700, height=500)
