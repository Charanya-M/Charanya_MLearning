import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

jobsData = pd.read_csv('AI_ImpactOnJobs.csv')

## Data bar of salary based on Experience using seaborn
plt.figure(figsize=(8, 4))
sb.barplot(data=jobsData, x="Years_Experience", y="Average_Salary", palette="viridis", hue="Years_Experience")
plt.ylim(bottom=30000)
plt.title("Avg. Salary based on Experience")
plt.show()

# Data plotting Job_Title vs Risk Category using scatter
plt.figure(figsize=(10,5))
subset = jobsData.iloc[0:25]
plt.scatter(subset["Job_Title"], subset["Risk_Category"], marker="*")
plt.title("Job Risk based on Job_Title")
plt.ylabel("Job_Title")
plt.xlabel("Risk_Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()



