# Personal Energy & Productivity Analytics Dashboard
## Project Plan

### 🎯 Project Overview
**Goal**: My goal for this project is to that track and analyse my personal energy, mood, and productivity patterns to test hypotheses about procrastination. Everybody knows that procrastination is bad, but to understand personally why it's bad for myself has required me to develop this project to convince myself and my brain, that maybe playing games all day isn't a great thing to do. In order for this project to be completed, I've created the following plan. Data collection begins at 9am on 06 August 2025. I'll be completely honest here, most of the plan was created using Claude AI, but it's not perfect so I've made a few ✨Personal✨ touches.

**Time Commitment**: 2 hours/day
**Timeline**: 6-8 weeks
**Target Audience**: Potential employers, friends, and anyone interested in personal productivity insights

--- 
** Summary of findings: **
- There seems to be no correlation personally between energy level and procrastination score.
- My energy seems to peak one hour after I wake up, with a second peak around 9pm.
- My most consistently productive days are Tuesdays, Wednesdays and Fridays.
- My energy stays fairly consistent regardless of a weekday or weekend.

---

## 📊 Data Collection Strategy (Google Sheets custom template)

### Hourly Tracking (9am - 12am)
- **Energy Level** (1-10 scale)
- **Mood** (1-10 scale)
- **Procrastination Score** (1-10 scale)
- **Current Activity** (work/study, gaming, creative, reading, exercise, social, rest, procrastinating)
- **Location** (indoors/outdoors, specific room)
- **Productive Tasks Completed** (count)

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
- **Backend**: Python (Pandas, NumPy for data processing, PrettyTable for pretty tables (obviously), sklearn for ML, scipy for statistical analysis tools.)
- **Visualizations**: Matplotlib, Seaborn
- **APIs**: Weather API (OpenWeatherMap or similar) Open-Meteo.com seems like a good one and we can export the result as a csv file.

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
- **Week 2**: Basic scripts with data import and simple visualizations
- **Week 3**: Dashboard with filtering and basic analytics
- **Week 4**: Advanced correlation analysis and hypothesis testing
- **Week 5**: Deployment-ready application

---

## 🎯 Success Metrics
- **Data Quality**: 80%+ completion rate for hourly tracking
- **Technical**: All planned features implemented and working
- **Insights**: Clear answers to at least 3 hypotheses
- **Portfolio Ready**: Professional-looking application suitable for job applications
- **Personal Value**: Actionable insights for improving productivity and energy

---

## 📝 Notes & Considerations
- Start data collection immediately - the more data, the better the insights
- Be consistent with tracking to ensure data quality
- Document interesting findings and patterns as you discover them
- Consider privacy implications when sharing (anonymize if needed)
- Keep code well-commented for portfolio purposes

A Short Discussion of Findings:
- There seems to be no correlation personally between energy level and procrastination score.
Now this is interesting. I wanted to discover if there was a correlation as I had a hunch that if I felt I was low in energy, then I would be more likely to procrastinate.
I was also surprised to see that if I was excited to work or had a high energy level, if that would mean I would be more likely to work.
This doesn't seem to be the case.
  
- My energy seems to peak one hour after I wake up, with a second peak around 9pm.
This makes sense. Straight after I wake up, I definitely don't want to go straight to my laptop and begin working. It takes time for the cogs to get going and this checks out.
  
- My most consistently productive days are Tuesdays, Wednesdays and Fridays.
I did have a feeling that midweek would be my most productive days. It's quite a popular opinion that Mondays often feel unproductive due to a combination of 
sleep disruptions from weekend changes, the emotional weight of the upcoming week, and a cultural tendency to anticipate Monday as a difficult day.
It would be really interesting to see how this trend is shown in other companies too. What is surprising though is Friday being up there. I didn't anticipate it but can understand as the last day of the working week, I am usually excited for the weekend and that perhaps increases my drive to work on a Friday.
  
- My energy stays fairly consistent regardless of a weekday or weekend.
I didn't anticipate this. I would've thought that there would be some changes here and honestly, I don't understand why. The only difference is that the lowest energy levels are 3 and 4 for Weekdays and Weekends Respectively. Otherwise the boxplots are identica. This would require some further investigation.

--- 
## Points for Further Investigation
- Why is my energy constant between Weekdays and Weekends.
