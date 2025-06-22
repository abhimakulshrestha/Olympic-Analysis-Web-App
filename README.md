# Olympic Analysis Web App 🏅

A comprehensive web application for analyzing Olympic Games data from 1896 to 2016. This interactive dashboard provides detailed insights into Olympic history, medal statistics, country performance, and athlete demographics using modern data visualization techniques.

## 🌟 Features

### 📊 Medal Tally Analysis
- **Overall Medal Statistics**: View total medals won by each country across all Olympic Games
- **Year-wise Analysis**: Track medal performance of countries over different Olympic years
- **Country-specific Insights**: Detailed breakdown of medals by country with historical trends

### 🌍 Overall Analysis
- **Participating Nations**: Track the growth of Olympic participation over time
- **Events Evolution**: Analyze how the number of events has changed throughout Olympic history
- **Athlete Participation**: Study the growth in athlete participation across different eras
- **Interactive Visualizations**: Dynamic charts showing Olympic trends and patterns

### 🏃‍♂️ Country-wise Analysis
- **Medal Distribution**: Pie charts and bar graphs showing medal breakdowns
- **Sport-wise Performance**: Analyze which sports each country excels in
- **Yearly Performance Trends**: Line charts tracking country performance over time
- **Comparative Analysis**: Compare multiple countries side by side

### 👥 Athlete-wise Analysis
- **Age Distribution**: Analyze the age demographics of Olympic athletes
- **Gender Participation**: Study the evolution of gender participation in Olympics
- **Height & Weight Analysis**: Physical characteristics analysis of athletes across sports
- **Sport-specific Demographics**: Detailed athlete profiles by sport categories

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Seaborn, Matplotlib
- **Data Source**: 120 years of Olympic history dataset

## Working WebSite 
- Chechout the website on : (https://olympic-analysis-web-app-bzxyahtq32kpttv7wgan3n.streamlit.app/)  

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhimakulshrestha/Olympic-Analysis-Web-App.git
   cd Olympic-Analysis-Web-App
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv olympic_env
   source olympic_env/bin/activate  # On Windows: olympic_env\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## 📋 Requirements

```
streamlit>=1.28.0
pandas>=1.3.0
numpy>=1.21.0
plotly>=5.0.0
seaborn>=0.11.0
matplotlib>=3.4.0
```

## 📁 Project Structure

```
Olympic-Analysis-Web-App/
│
├── app.py                 # Main Streamlit application
├── preprocessor.py        # Data preprocessing functions
├── helper.py             # Helper functions for analysis
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
│
├── data/
│   ├── athlete_events.csv    # Main Olympic dataset
│   └── noc_regions.csv       # Country/Region mapping
│
├── assets/
│   └── images/              # Application images and logos
│
└── notebooks/
    └── EDA.ipynb           # Exploratory Data Analysis notebook
```

## 🚀 Usage

### Navigation
The application features a sidebar navigation with four main sections:

1. **Medal Tally**: Explore medal statistics by country and year
2. **Overall Analysis**: View comprehensive Olympic trends and statistics
3. **Country-wise Analysis**: Deep dive into specific country performances
4. **Athlete-wise Analysis**: Analyze athlete demographics and characteristics

### Interactive Features
- **Dropdown Filters**: Select specific countries, years, or sports
- **Dynamic Charts**: Interactive Plotly visualizations
- **Data Tables**: Sortable and filterable data displays
- **Statistical Summaries**: Key metrics and insights

## 📊 Data Sources

- **Primary Dataset**: 120 years of Olympic history: athletes and results
- **Source**: Kaggle Olympic Dataset
- **Coverage**: 1896-2016 Olympic Games
- **Records**: 270,000+ athlete records across Summer and Winter Olympics

## 🔍 Key Insights Available

- Medal trends over 120 years of Olympic history
- Country dominance in specific sports
- Evolution of gender participation
- Physical characteristics of athletes by sport
- Most successful Olympic nations
- Seasonal Olympics comparison (Summer vs Winter)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abhimak Kulshrestha**
- GitHub: [@abhimakulshrestha](https://github.com/abhimakulshrestha)
- LinkedIn: [Connect with me](https://linkedin.com/in/abhimakulshrestha)

## 🙏 Acknowledgments

- Olympic data provided by the International Olympic Committee
- Kaggle community for the comprehensive Olympic dataset
- Streamlit team for the amazing web app framework
- Open source community for the visualization libraries

## 📸 Screenshots
![Screenshot 2025-06-22 152202](https://github.com/user-attachments/assets/77771e87-639d-4127-9185-621050fa9047)
![Screenshot 2025-06-22 152216](https://github.com/user-attachments/assets/9d5c64db-8580-4aed-920a-db4ff8de2714)
![Screenshot 2025-06-22 152228](https://github.com/user-attachments/assets/084631f8-96a5-4182-bb5a-bc682aa3e744)
![Screenshot 2025-06-22 152234](https://github.com/user-attachments/assets/22d1ddce-76fe-4979-ae9b-5483d760f0fb)
![Screenshot 2025-06-22 152240](https://github.com/user-attachments/assets/14c17d44-463c-4300-8bdc-c10ed09fb429)
![Screenshot 2025-06-22 152249](https://github.com/user-attachments/assets/bbbb9938-8553-4970-84ce-c218b06c5c09)
![Screenshot 2025-06-22 152339](https://github.com/user-attachments/assets/965d5ab1-10df-4fa4-bf1c-3495c359da4a)

## 🔮 Future Enhancements

- [ ] Add 2020 Tokyo Olympics data
- [ ] Implement machine learning predictions for medal counts
- [ ] Add more interactive filtering options
- [ ] Create downloadable reports
- [ ] Implement real-time data updates
- [ ] Add mobile-responsive design improvements

---
