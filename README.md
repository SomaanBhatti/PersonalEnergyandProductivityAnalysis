# Personal Energy & Productivity Analytics Dashboard
## Project Plan

### 🎯 Project Overview
**Goal**: My goal for this project is to create a web-based data science application that tracks and analyses my personal energy, mood, and productivity patterns to test hypotheses about procrastination. Everybody knows that procrastination is bad, but to understand personally why it's bad for myself has required me to develop this project to convince myself and my brain, that maybe playing games all day isn't a great thing to do. In order for this project to be completed, I've created the following plan. Data collection begins at 9am on 06 August 2025. I'll be completely honest here, most of the plan was created using Claude AI, but it's not perfect so I've made a few ✨Personal✨ touches.

**Time Commitment**: 2 hours/day
**Timeline**: 6-8 weeks
**Target Audience**: Potential employers, friends, and anyone interested in personal productivity insights

---

## 📊 Data Collection Strategy (Google Sheets custom template)

### Hourly Tracking (9am - 12am)
- **Energy Level** (1-10 scale)
- **Mood** (1-10 scale)
- **Procrastination Score** (1-10 scale)
- **Current Activity** (work/study, gaming, creative, reading, exercise, social, rest, procrastinating)
- **Location** (indoors/outdoors, specific room)
- **Productivity Tasks Completed** (count)

### Daily Summary Metrics
- **Sleep Quality** (1-10, logged next morning)
- **Weather Data** (auto-pulled via API: temperature, conditions, humidity)
- **Gaming Time** (total hours, which games)
- **Creative/Productive Time** (art/embroidery hours)
- **Procrastinated time**

---

## 🔬 Hypotheses to Test
1. **Primary**: Procrastination negatively impacts mood and energy levels
2. Weather conditions affect energy levels and mood
3. Creative activities boost subsequent productivity, organically
4. Time spent indoors correlates with lower energy
5. Energy patterns follow predictable daily/weekly cycles

---

## 🛠️ Technical Stack
- **Data Collection**: Google Sheets (mobile-friendly, easy CSV export)
- **Backend**: Python (Pandas, NumPy for data processing)
- **Visualizations**: Plotly, Matplotlib, Seaborn
- **Web Framework**: Streamlit or Flask
- **APIs**: Weather API (OpenWeatherMap or similar)
- **Deployment**: Heroku, Streamlit Cloud, or GitHub Pages

---

## 📅 Phase-by-Phase Implementation

### Phase 1: Setup & Data Collection (Week 1)
**Time: 10-14 hours**

#### Day 1 (4 hours)
- [ ] Create Google Sheets template with all tracking columns
- [ ] Set up hourly reminders (phone alarms/calendar)
- [ ] Test the logging process for 2 days
- [ ] Set up project repository on GitHub

#### Day 2-7 (6-10 hours)
- [ ] Continue daily data collection
- [ ] Research and sign up for weather API
- [ ] Set up Python environment and install required libraries
- [ ] Create initial data import script (Google Sheets → CSV → Pandas)

### Phase 2: Basic Web Application (Week 2-3)
**Time: 20-28 hours**

#### Week 2 (10-14 hours)
- [ ] Build basic web app structure (Streamlit/Flask)
- [ ] Implement CSV data upload functionality
- [ ] Create data cleaning and preprocessing pipeline
- [ ] Build basic summary statistics display
- [ ] Implement weather API integration

#### Week 3 (10-14 hours)
- [ ] Create time series visualizations (energy, mood, productivity over time)
- [ ] Build basic correlation analysis
- [ ] Implement activity breakdown charts
- [ ] Add data filtering capabilities (by date, activity, weather)

### Phase 3: Advanced Analytics (Week 4-5)
**Time: 20-28 hours**

#### Week 4 (10-14 hours)
- [ ] Implement correlation heatmaps
- [ ] Build hypothesis testing framework
- [ ] Create procrastination impact analysis
- [ ] Develop weather vs energy correlation analysis

#### Week 5 (10-14 hours)
- [ ] Build predictive models (energy level prediction)
- [ ] Implement pattern recognition (daily/weekly cycles)
- [ ] Create interactive dashboard with multiple views
- [ ] Add statistical significance testing

### Phase 4: Polish & Enhancement (Week 6-8)
**Time: 20-42 hours**

#### Week 6 (10-14 hours)
- [ ] Enhance UI/UX design
- [ ] Add animations and interactive elements
- [ ] Implement advanced filtering and comparison tools
- [ ] Create executive summary/insights page

#### Week 7 (10-14 hours)
- [ ] Add data export functionality
- [ ] Implement trend forecasting
- [ ] Create personalized recommendations engine
- [ ] Add documentation and code comments

#### Week 8 (0-14 hours - Buffer/Optional)
- [ ] Deploy to web hosting platform
- [ ] Create project portfolio page
- [ ] Add unit tests
- [ ] Performance optimization
- [ ] Additional visualizations based on insights

---

## 📈 Key Features to Showcase

### Data Science Skills
- [ ] Data cleaning and preprocessing
- [ ] Statistical analysis and hypothesis testing
- [ ] Correlation analysis and pattern recognition
- [ ] Predictive modeling
- [ ] Time series analysis

### Technical Skills
- [ ] Python (Pandas, NumPy)
- [ ] Data visualization (Plotly, Matplotlib)
- [ ] API integration
- [ ] Web development
- [ ] Database/file handling
- [ ] Version control (Git)

### Unique Personal Touch
- [ ] Self-quantification methodology
- [ ] Personal hypothesis testing
- [ ] Behavioral insights and recommendations
- [ ] Real-world problem solving

---

## 📋 Weekly Milestones

- **Week 1**: Data collection system operational, 7 days of data collected
- **Week 2**: Basic web app with data import and simple visualizations
- **Week 3**: Interactive dashboard with filtering and basic analytics
- **Week 4**: Advanced correlation analysis and hypothesis testing
- **Week 5**: Predictive modeling and pattern recognition
- **Week 6**: Polished interface with animations and insights
- **Week 7**: Deployment-ready application with documentation
- **Week 8**: Live deployed application ready for portfolio

---

## 🎯 Success Metrics
- **Data Quality**: 80%+ completion rate for hourly tracking
- **Technical**: All planned features implemented and working
- **Insights**: Clear answers to at least 3 of the 5 hypotheses
- **Portfolio Ready**: Professional-looking application suitable for job applications
- **Personal Value**: Actionable insights for improving productivity and energy

---

## 📝 Notes & Considerations
- Start data collection immediately - the more data, the better the insights
- Be consistent with tracking to ensure data quality
- Document interesting findings and patterns as you discover them
- Consider privacy implications when sharing (anonymize if needed)
- Keep code well-commented for portfolio purposes
