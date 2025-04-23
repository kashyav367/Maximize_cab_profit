

```markdown
# 🚖 Deep Q-Learning Based Cab Pricing Strategy with Map Visualization

This project demonstrates a **Reinforcement Learning-based cab driver decision system** that uses **Deep Q-Learning** to optimize ride selection and maximize earnings based on real-world cab ride data. It also features a **Streamlit-based web interface** with **interactive route maps**, simulating a real-time Uber-like environment.

---

## 🧠 What’s Inside?

- ✅ Deep Q-Learning implementation from scratch using Keras
- ✅ Custom OpenAI Gym Environment based on cab ride dataset
- ✅ Smart reward system based on ride pricing and surge
- ✅ Streamlit dashboard for:
  - Uploading dataset
  - Training the model
  - Visualizing cab ride decisions
  - Viewing source-to-destination map animations using Folium

---

## 📁 Dataset Columns

| Column Name        | Description                                |
|--------------------|--------------------------------------------|
| `distance`         | Distance of the ride in miles              |
| `cab_type`         | Type of cab service (Uber, Lyft, etc.)     |
| `time_stamp`       | Timestamp of booking                       |
| `destination`      | Destination location                       |
| `source`           | Source location                            |
| `price`            | Final price of the ride                    |
| `surge_multiplier` | Surge rate at the time of booking          |
| `id`               | Ride ID                                    |
| `product_id`       | Product category                           |
| `name`             | Type of cab (e.g., Shared, Lux, etc.)      |

---

## 🚀 Features

- 🧠 **AI-Driven Decision Making:** Uses Deep Q-Learning to decide which rides to accept for maximum earnings
- 🗺️ **Map Visualization:** Shows cab route from source to destination using Folium maps
- 📊 **Training Charts:** Tracks cumulative reward over episodes
- 🛠️ **Custom RL Environment:** Simulates real-world cab scenarios for better policy learning

---

## 🧩 Project Architecture

```
📦 cab_rl_project
├── main_app.py           # Streamlit app interface
├── env_cab_rl.py         # Custom cab driver RL environment
├── agent_dqn.py          # Deep Q-Network agent (Keras)
├── preprocess.py         # Data loading and preprocessing
├── utils_map.py          # Map drawing utilities using Folium
├── data/
│   └── cab_data.csv      # Sample real-world cab data
└── README.md             # GitHub Readme
```

---

## 📸 Demo Screenshots

### 📌 Upload & Train  
![Upload CSV & Train](https://user-images.githubusercontent.com/your-demo-link/train.png)

### 📌 Map View  
![Ride Map](https://user-images.githubusercontent.com/your-demo-link/map.png)

---

## 🛠️ Installation & Setup

### 🔧 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/cab-dqn-rl.git
cd cab-dqn-rl
```

### 📦 Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can use:
```bash
pip install streamlit pandas numpy matplotlib scikit-learn keras tensorflow folium streamlit-folium
```

### 🚀 Step 3: Run the App

```bash
streamlit run main_app.py
```

---

## 📈 Model Training Logic

- **States** → Distance, Cab Type, Source, Destination, Hour, Weekday, Surge
- **Actions** → Accept or Reject the ride
- **Rewards** → Based on price and surge value
- **Goal** → Maximize cumulative reward over episodes (i.e., cab earnings)

---

## 🔍 Future Scope

- Add **Real-Time GPS integration** using live APIs
- Add **Ride Pooling Optimization**
- Add **Multi-agent reinforcement learning** for multiple drivers
- Export trained agent as `.h5` model for reuse

---

## 👨‍💻 Author

**Ajay Kumar Jha**  
🚀 B.Tech | Artificial Intelligence & Machine Learning  
📍 Dr. B C Roy Engineering College, Durgapur  
📫 [LinkedIn](https://www.linkedin.com/in/ajay-kumar-jha-30b612261/) | [GitHub](https://github.com/ajaykumarjha01)

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Show Some Love

If you like this project, leave a ⭐ on the repository — it helps a lot!

```

---

Would you like me to generate the `requirements.txt` file and ZIP the whole structure too?
